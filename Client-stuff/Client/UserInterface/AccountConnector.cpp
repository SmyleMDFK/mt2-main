#include "StdAfx.h"
#include "AccountConnector.h"
#include "Packet.h"
#include "PythonNetworkStream.h"
#include "../EterBase/tea.h"
#include "../EterPack/EterPackManager.h"

// CHINA_CRYPT_KEY
extern DWORD g_adwEncryptKey[4];
extern DWORD g_adwDecryptKey[4];
// END_OF_CHINA_CRYPT_KEY

#ifdef USE_OPENID
extern int openid_test;
#endif

void CAccountConnector::SetHandler(PyObject* poHandler)
{
	m_poHandler = poHandler;
}

void CAccountConnector::SetLoginInfo(const char * c_szName, const char * c_szPwd
#if defined(INGAME_REGISTER)
, bool bRegister, std::string email, std::string social
#endif
)
{
	m_strID = c_szName;
	m_strPassword = c_szPwd;
#if defined(INGAME_REGISTER)
	m_register = bRegister;
	m_email = email;
	m_social = social;
#endif
}


void CAccountConnector::ClearLoginInfo( void )
{
	m_strPassword = "";
}

bool CAccountConnector::Connect(const char * c_szAddr, int iPort, const char * c_szAccountAddr, int iAccountPort)
{
#ifndef _IMPROVED_PACKET_ENCRYPTION_
	__BuildClientKey();
#endif

	m_strAddr = c_szAddr;
	m_iPort = iPort;

	__OfflineState_Set();

	// CHINA_CRYPT_KEY
	if (LocaleService_IsYMIR())
	{
	}
	else
	{
		__BuildClientKey_20050304Myevan();
	}
	// END_OF_CHINA_CRYPT_KEY

	return CNetworkStream::Connect(c_szAccountAddr, iAccountPort);
}

void CAccountConnector::Disconnect()
{
	CNetworkStream::Disconnect();
	__OfflineState_Set();
}

void CAccountConnector::Process()
{
	CNetworkStream::Process();

	if (!__StateProcess())
	{
		__OfflineState_Set();
		Disconnect();
	}
}

bool CAccountConnector::__StateProcess()
{
	switch (m_eState)
	{
		case STATE_HANDSHAKE:
			return __HandshakeState_Process();
			break;
		case STATE_AUTH:
			return __AuthState_Process();
			break;
	}

	return true;
}

bool CAccountConnector::__HandshakeState_Process()
{
	if (!__AnalyzePacket(HEADER_GC_PHASE, sizeof(TPacketGCPhase), &CAccountConnector::__AuthState_RecvPhase))
		return false;

	if (!__AnalyzePacket(HEADER_GC_HANDSHAKE, sizeof(TPacketGCHandshake), &CAccountConnector::__AuthState_RecvHandshake))
		return false;

	if (!__AnalyzePacket(HEADER_GC_PING, sizeof(TPacketGCPing), &CAccountConnector::__AuthState_RecvPing))
		return false;

#ifdef _IMPROVED_PACKET_ENCRYPTION_
	if (!__AnalyzePacket(HEADER_GC_KEY_AGREEMENT, sizeof(TPacketKeyAgreement), &CAccountConnector::__AuthState_RecvKeyAgreement))
		return false;

	if (!__AnalyzePacket(HEADER_GC_KEY_AGREEMENT_COMPLETED, sizeof(TPacketKeyAgreementCompleted), &CAccountConnector::__AuthState_RecvKeyAgreementCompleted))
		return false;
#endif

	return true;
}

bool CAccountConnector::__AuthState_Process()
{
	if (!__AnalyzePacket(0, sizeof(BYTE), &CAccountConnector::__AuthState_RecvEmpty))
		return true;

	if (!__AnalyzePacket(HEADER_GC_PHASE, sizeof(TPacketGCPhase), &CAccountConnector::__AuthState_RecvPhase))
		return false;

	if (!__AnalyzePacket(HEADER_GC_PING, sizeof(TPacketGCPing), &CAccountConnector::__AuthState_RecvPing))
		return false;

	if (!__AnalyzePacket(HEADER_GC_AUTH_SUCCESS, sizeof(TPacketGCAuthSuccess), &CAccountConnector::__AuthState_RecvAuthSuccess))
		return true;

#ifdef USE_OPENID
	if (!__AnalyzePacket(HEADER_GC_AUTH_SUCCESS_OPENID, sizeof(TPacketGCAuthSuccess), &CAccountConnector::__AuthState_RecvAuthSuccess_OpenID))
		return true;
#endif /* USE_OPENID */

	if (!__AnalyzePacket(HEADER_GC_LOGIN_FAILURE, sizeof(TPacketGCAuthSuccess), &CAccountConnector::__AuthState_RecvAuthFailure))
		return true;

#if defined(INGAME_REGISTER)
	if (!__AnalyzePacket(HEADER_GC_REGISTER_FAIL, sizeof(TPacketGCRegisterFail), &CAccountConnector::__AuthState_RecvRegisterFail)) {
		return true;
	}

	if (!__AnalyzePacket(HEADER_GC_REGISTER_SUCCESS, sizeof(TPacketEmpty), &CAccountConnector::__AuthState_RecvRegisterSuccess)) {
		return true;
	}
#endif

	if (!__AnalyzePacket(HEADER_GC_HANDSHAKE, sizeof(TPacketGCHandshake), &CAccountConnector::__AuthState_RecvHandshake))
		return false;

#ifdef _IMPROVED_PACKET_ENCRYPTION_
	if (!__AnalyzePacket(HEADER_GC_KEY_AGREEMENT, sizeof(TPacketKeyAgreement), &CAccountConnector::__AuthState_RecvKeyAgreement))
		return false;

	if (!__AnalyzePacket(HEADER_GC_KEY_AGREEMENT_COMPLETED, sizeof(TPacketKeyAgreementCompleted), &CAccountConnector::__AuthState_RecvKeyAgreementCompleted))
		return false;
#endif

	return true;
}

bool CAccountConnector::__AuthState_RecvEmpty()
{
	BYTE byEmpty;
	Recv(sizeof(BYTE), &byEmpty);
	return true;
}

bool CAccountConnector::__AuthState_RecvPhase()
{
	TPacketGCPhase kPacketPhase;
	if (!Recv(sizeof(kPacketPhase), &kPacketPhase))
		return false;

	if (kPacketPhase.phase == PHASE_HANDSHAKE)
	{
		__HandshakeState_Set();
	}
	else if (kPacketPhase.phase == PHASE_AUTH)
	{
#ifndef _IMPROVED_PACKET_ENCRYPTION_
		const char* key = LocaleService_GetSecurityKey();
		SetSecurityMode(true, key);
#endif

#ifdef USE_OPENID
		if (!openid_test)
		{
			//2012.07.19 OpenID : ??????
			//Ongoing : ???? ?????? ????-> TPacketCGLogin5
			//?????? ?????? ???? ?????????? ?????? ????????.

			//const char* tempAuthKey = "d4025bc1f752b64fe5d51ae575ec4730"; //???????? ???? 32
			TPacketCGLogin5 LoginPacket;
			LoginPacket.header = HEADER_CG_LOGIN5_OPENID;

			strncpy(LoginPacket.authKey, LocaleService_GetOpenIDAuthKey(), OPENID_AUTHKEY_LEN);
			LoginPacket.authKey[OPENID_AUTHKEY_LEN] = '\0';

			for (DWORD i = 0; i < 4; ++i)
				LoginPacket.adwClientKey[i] = g_adwEncryptKey[i];

			if (!Send(sizeof(LoginPacket), &LoginPacket))
			{
				Tracen(" CAccountConnector::__AuthState_RecvPhase - SendLogin5 Error");
				return false;
			}

			if (!SendSequence())
			{
				return false;
			}
		}
		else
		{
			TPacketCGLogin3 LoginPacket;
			LoginPacket.header = HEADER_CG_LOGIN3;

			strncpy(LoginPacket.name, m_strID.c_str(), ID_MAX_NUM);
			strncpy(LoginPacket.pwd, m_strPassword.c_str(), PASS_MAX_NUM);
			LoginPacket.name[ID_MAX_NUM] = '\0';
			LoginPacket.pwd[PASS_MAX_NUM] = '\0';

			// ?????????? ???????? ???? ???? ???? ?????? ??????, ???? ???? ?????? ?????? ????
			ClearLoginInfo();
			CPythonNetworkStream& rkNetStream=CPythonNetworkStream::Instance();
			rkNetStream.ClearLoginInfo();

			m_strPassword = "";

			for (DWORD i = 0; i < 4; ++i)
				LoginPacket.adwClientKey[i] = g_adwEncryptKey[i];

			if (!Send(sizeof(LoginPacket), &LoginPacket))
			{
				Tracen(" CAccountConnector::__AuthState_RecvPhase - SendLogin3 Error");
				return false;
			}

			if (!SendSequence())
			{
				return false;
			}
		}
#else /* USE_OPENID */

#if defined(INGAME_REGISTER)
		if (m_register)
		{
			m_register = false;

			TPacketCGRegister p;

			p.header = HEADER_CG_REGISTER;
			strncpy(p.username, m_strID.c_str(), ID_MAX_NUM);
			p.username[ID_MAX_NUM] = '\0';
			strncpy(p.password, m_strPassword.c_str(), PASS_MAX_NUM);
			p.password[PASS_MAX_NUM] = '\0';
			strncpy(p.email, m_email.c_str(), EMAIL_MAX_LEN);
			p.email[EMAIL_MAX_LEN] = '\0';
			strncpy(p.socialid, m_social.c_str(), SOCIAL_ID_LEN);
			p.socialid[SOCIAL_ID_LEN] = '\0';

			m_strID = "";
			m_strPassword = "";
			m_email = "";
			m_social = "";

			CPythonNetworkStream::Instance().ClearLoginInfo();

			if (!Send(sizeof(p), &p)) {
				Tracen(" CAccountConnector::__AuthState_RecvPhase - SendRegister Error");
				return false;
			}

			if (!SendSequence()) {
				return false;
			}

			__AuthState_Set();

			return true;
		}
#endif

		TPacketCGLogin3 LoginPacket;
		LoginPacket.header = HEADER_CG_LOGIN3;

		strncpy(LoginPacket.name, m_strID.c_str(), ID_MAX_NUM);
		strncpy(LoginPacket.pwd, m_strPassword.c_str(), PASS_MAX_NUM);
		LoginPacket.name[ID_MAX_NUM] = '\0';
		LoginPacket.pwd[PASS_MAX_NUM] = '\0';

		// ?????????? ???????? ???? ???? ???? ?????? ??????, ???? ???? ?????? ?????? ????
		ClearLoginInfo();
		CPythonNetworkStream& rkNetStream=CPythonNetworkStream::Instance();
		rkNetStream.ClearLoginInfo();

		m_strPassword = "";

		for (DWORD i = 0; i < 4; ++i)
			LoginPacket.adwClientKey[i] = g_adwEncryptKey[i];

		if (!Send(sizeof(LoginPacket), &LoginPacket))
		{
			Tracen(" CAccountConnector::__AuthState_RecvPhase - SendLogin3 Error");
			return false;
		}

		if (!SendSequence())
		{
			return false;
		}
#endif /* USE_OPENID */

		__AuthState_Set();
	}

	return true;
}

bool CAccountConnector::__AuthState_RecvHandshake()
{
	TPacketGCHandshake kPacketHandshake;
	if (!Recv(sizeof(kPacketHandshake), &kPacketHandshake))
		return false;

	// HandShake
	{
		Tracenf("HANDSHAKE RECV %u %d", kPacketHandshake.dwTime, kPacketHandshake.lDelta);

		ELTimer_SetServerMSec(kPacketHandshake.dwTime+ kPacketHandshake.lDelta);

		//DWORD dwBaseServerTime = kPacketHandshake.dwTime+ kPacketHandshake.lDelta;
		//DWORD dwBaseClientTime = ELTimer_GetMSec();

		kPacketHandshake.dwTime = kPacketHandshake.dwTime + kPacketHandshake.lDelta + kPacketHandshake.lDelta;
		kPacketHandshake.lDelta = 0;

		Tracenf("HANDSHAKE SEND %u", kPacketHandshake.dwTime);

		if (!Send(sizeof(kPacketHandshake), &kPacketHandshake))
		{
			Tracen(" CAccountConnector::__AuthState_RecvHandshake - SendHandshake Error");
			return false;
		}
	}

	return true;
}

bool CAccountConnector::__AuthState_RecvPing()
{
	TPacketGCPing kPacketPing;
	if (!Recv(sizeof(kPacketPing), &kPacketPing))
		return false;

	__AuthState_SendPong();

	return true;
}

bool CAccountConnector::__AuthState_SendPong()
{
	TPacketCGPong kPacketPong;
	kPacketPong.bHeader = HEADER_CG_PONG;
	if (!Send(sizeof(kPacketPong), &kPacketPong))
		return false;

	if (IsSecurityMode())
		return SendSequence();

	return true;
}

#if defined(INGAME_REGISTER)
bool CAccountConnector::__AuthState_RecvRegisterFail() {
	TPacketGCRegisterFail p;
	if (!Recv(sizeof(p), &p)) {
		return false;
	}

	if (m_poHandler) {
		PyCallClassMemberFunc(m_poHandler, "OnRegisterFail", Py_BuildValue("(ii)", p.error, p.arg));
	}
#ifdef _DEBUG
	Tracef(" __AuthState_RecvRegisterFail : [%s]\n", packet_failure.error);
#endif

	Disconnect();
	SetLoginInfo("", "", false, "", "");

	return true;
}

bool CAccountConnector::__AuthState_RecvRegisterSuccess() {
	TPacketEmpty p;
	if (!Recv(sizeof(p), &p)) {
		return false;
	}

	if (m_poHandler) {
		PyCallClassMemberFunc(m_poHandler, "OnRegisterSuccess", Py_BuildValue("()"));
	}
#ifdef _DEBUG
	Tracef(" __AuthState_RecvRegisterSuccess\n");
#endif

	Disconnect();
	SetLoginInfo("", "", false, "", "");

	return true;
}
#endif

bool CAccountConnector::__AuthState_RecvAuthSuccess()
{
	TPacketGCAuthSuccess kAuthSuccessPacket;
	if (!Recv(sizeof(kAuthSuccessPacket), &kAuthSuccessPacket))
		return false;

	if (!kAuthSuccessPacket.bResult)
	{
		if (m_poHandler)
			PyCallClassMemberFunc(m_poHandler, "OnLoginFailure", Py_BuildValue("(s)", "BESAMEKEY"));
	}
	else
	{
		CPythonNetworkStream & rkNet = CPythonNetworkStream::Instance();
		rkNet.SetLoginKey(kAuthSuccessPacket.dwLoginKey);
		rkNet.Connect(m_strAddr.c_str(), m_iPort);
	}

	Disconnect();
	__OfflineState_Set();

	return true;
}

#ifdef USE_OPENID
bool CAccountConnector::__AuthState_RecvAuthSuccess_OpenID()
{
	TPacketGCAuthSuccessOpenID kAuthSuccessOpenIDPacket;
	if (!Recv(sizeof(kAuthSuccessOpenIDPacket), &kAuthSuccessOpenIDPacket))
		return false;

	if (!kAuthSuccessOpenIDPacket.bResult)
	{
		if (m_poHandler)
			PyCallClassMemberFunc(m_poHandler, "OnLoginFailure", Py_BuildValue("(s)", "BESAMEKEY"));
	}
	else
	{
		CPythonNetworkStream & rkNet = CPythonNetworkStream::Instance();
		rkNet.SetLoginInfo(kAuthSuccessOpenIDPacket.login, "0000");		//OpenID ???? ???????? ?????????? ???????? ??????.
		rkNet.SetLoginKey(kAuthSuccessOpenIDPacket.dwLoginKey);
		rkNet.Connect(m_strAddr.c_str(), m_iPort);
	}

	Disconnect();
	__OfflineState_Set();

	return true;
}
#endif /* USE_OPENID */


bool CAccountConnector::__AuthState_RecvAuthFailure()
{
	TPacketGCLoginFailure packet_failure;
	if (!Recv(sizeof(TPacketGCLoginFailure), &packet_failure))
		return false;

	if (m_poHandler)
		PyCallClassMemberFunc(m_poHandler, "OnLoginFailure", Py_BuildValue("(s)", packet_failure.szStatus));

//	__OfflineState_Set();

	return true;
}

#ifdef _IMPROVED_PACKET_ENCRYPTION_
bool CAccountConnector::__AuthState_RecvKeyAgreement()
{
	TPacketKeyAgreement packet;
	if (!Recv(sizeof(packet), &packet))
	{
		return false;
	}

	Tracenf("KEY_AGREEMENT RECV %u", packet.wDataLength);

	TPacketKeyAgreement packetToSend;
	size_t dataLength = TPacketKeyAgreement::MAX_DATA_LEN;
	size_t agreedLength = Prepare(packetToSend.data, &dataLength);
	if (agreedLength == 0)
	{
		// ?????? ????
		Disconnect();
		return false;
	}
	assert(dataLength <= TPacketKeyAgreement::MAX_DATA_LEN);

	if (Activate(packet.wAgreedLength, packet.data, packet.wDataLength))
	{
		// Key agreement ????, ???? ????
		packetToSend.bHeader = HEADER_CG_KEY_AGREEMENT;
		packetToSend.wAgreedLength = (WORD)agreedLength;
		packetToSend.wDataLength = (WORD)dataLength;

		if (!Send(sizeof(packetToSend), &packetToSend))
		{
			Tracen(" CAccountConnector::__AuthState_RecvKeyAgreement - SendKeyAgreement Error");
			return false;
		}
		Tracenf("KEY_AGREEMENT SEND %u", packetToSend.wDataLength);
	}
	else
	{
		// ?? ???? ????
		Disconnect();
		return false;
	}
	return true;
}

bool CAccountConnector::__AuthState_RecvKeyAgreementCompleted()
{
	TPacketKeyAgreementCompleted packet;
	if (!Recv(sizeof(packet), &packet))
	{
		return false;
	}

	Tracenf("KEY_AGREEMENT_COMPLETED RECV");

	ActivateCipher();

	return true;
}
#endif // _IMPROVED_PACKET_ENCRYPTION_

bool CAccountConnector::__AnalyzePacket(UINT uHeader, UINT uPacketSize, bool (CAccountConnector::*pfnDispatchPacket)())
{
	BYTE bHeader;
	if (!Peek(sizeof(bHeader), &bHeader))
		return true;

	if (bHeader!=uHeader)
		return true;

	if (!Peek(uPacketSize))
		return true;

	return (this->*pfnDispatchPacket)();
}

bool CAccountConnector::__AnalyzeVarSizePacket(UINT uHeader, bool (CAccountConnector::*pfnDispatchPacket)(int))
{
	BYTE bHeader;
	if (!Peek(sizeof(bHeader), &bHeader))
		return true;

	if (bHeader!=uHeader)
		return true;

	TDynamicSizePacketHeader dynamicHeader;

	if (!Peek(sizeof(dynamicHeader), &dynamicHeader))
		return true;

	if (!Peek(dynamicHeader.size))
		return true;

	return (this->*pfnDispatchPacket)(dynamicHeader.size);
}


void CAccountConnector::__OfflineState_Set()
{
	__Inialize();
}

void CAccountConnector::__HandshakeState_Set()
{
	m_eState=STATE_HANDSHAKE;
}

void CAccountConnector::__AuthState_Set()
{
	m_eState=STATE_AUTH;
}

void CAccountConnector::OnConnectFailure()
{
	if (m_poHandler)
		PyCallClassMemberFunc(m_poHandler, "OnConnectFailure", Py_BuildValue("()"));

	__OfflineState_Set();
}

void CAccountConnector::OnConnectSuccess()
{
	m_eState = STATE_HANDSHAKE;
}

void CAccountConnector::OnRemoteDisconnect()
{
	__OfflineState_Set();
}

void CAccountConnector::OnDisconnect()
{
	__OfflineState_Set();
}

#ifndef _IMPROVED_PACKET_ENCRYPTION_
void CAccountConnector::__BuildClientKey()
{
	for (DWORD i = 0; i < 4; ++i)
		g_adwEncryptKey[i] = random();

	const BYTE * c_pszKey = (const BYTE *) "JyTxtHljHJlVJHorRM301vf@4fvj10-v";
	tea_encrypt((DWORD *) g_adwDecryptKey, (const DWORD *) g_adwEncryptKey, (const DWORD *) c_pszKey, 16);
}
#endif

void CAccountConnector::__Inialize()
{
	m_eState=STATE_OFFLINE;
}

CAccountConnector::CAccountConnector()
{
	m_poHandler = NULL;
	m_strAddr = "";
	m_iPort = 0;

	SetLoginInfo("", ""
#if defined(INGAME_REGISTER)
, false, "", ""
#endif
	);
	SetRecvBufferSize(1024 * 128);
	SetSendBufferSize(2048);
	__Inialize();
}

CAccountConnector::~CAccountConnector()
{
	__OfflineState_Set();
}
