#pragma once

//////////////////////////////////////////////////////////////////////////
// ### Default Ymir Macros ###
#define LOCALE_SERVICE_EUROPE
#define ENABLE_COSTUME_SYSTEM
#define ENABLE_ENERGY_SYSTEM
#define ENABLE_DRAGON_SOUL_SYSTEM
#define ENABLE_NEW_EQUIPMENT_SYSTEM
// ### Default Ymir Macros ###
//////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////
// ### New From LocaleInc ###
#define ENABLE_PACK_GET_CHECK
#define ENABLE_CANSEEHIDDENTHING_FOR_GM
#define ENABLE_PROTOSTRUCT_AUTODETECT

#define ENABLE_PLAYER_PER_ACCOUNT5
#define ENABLE_LEVEL_IN_TRADE
#define ENABLE_DICE_SYSTEM
//#define ENABLE_EXTEND_INVEN_SYSTEM
#define ENABLE_LVL115_ARMOR_EFFECT
#define ENABLE_SLOT_WINDOW_EX
#define ENABLE_TEXT_LEVEL_REFRESH
#define ENABLE_USE_COSTUME_ATTR

#define WJ_SHOW_MOB_INFO
#ifdef WJ_SHOW_MOB_INFO
#define ENABLE_SHOW_MOBAIFLAG
#define ENABLE_SHOW_MOBLEVEL
#endif

/* de programat
#define ENABLE_SERVER_SELECT_RENEWAL
#define ENABLE_STEAM
#define LOGIN_TYPE_STEAM
#define ENABLE_BATTLE_FIELD
#define ENABLE_DELETE_FAILURE_TYPE
#define ENABLE_MONSTER_CARD
#define ENABLE_GROWTH_PET_SYSTEM
#define ENABLE_PRIVATESHOP_SEARCH_SYSTEM
#define ENABLE_12ZI
#define ENABLE_PARTY_MATCH
#define ENABLE_USER_SITUATION_NOTICE
#define ENABLE_MINI_GAME_YUTNORI
#define ENABLE_WEB_LINKED_BANNER
#define ENABLE_AUTO_ATTACK
#define ENABLE_CHANGED_ATTR
#define ENABLE_PVP_BALANCE
#define ENABLE_PENDANT
#define ENABLE_ELEMENT_ADD
*/

/* de completat */
#define ENABLE_DETAILS_UI
#define ENABLE_CONQUEROR_LEVEL



/* noi */
#define SPECIAL_ACTION_START_INDEX 101
#define INGAME_WIKI
#if defined(INGAME_WIKI)
	/*
		Only define this if you have wolfman in you server
	*/
	#define INGAME_WIKI_WOLFMAN 

	/*
		Only put this line if you have any problems in dynamic wiki communication (G-C)
	*/
	// #define INGAME_WIKI_AUTOPACKET_SIZE
#endif
#define INGAME_REGISTER



/* bufixes*/
#define ENABLE_BUGFIXES
//fix1 - memerr
/* end bugfixes */



// ### New From LocaleInc ###
//////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////
// ### From GameLib ###
#define ENABLE_WOLFMAN_CHARACTER

// #define ENABLE_MAGIC_REDUCTION_SYSTEM
#define ENABLE_MOUNT_COSTUME_SYSTEM
#define ENABLE_WEAPON_COSTUME_SYSTEM
// ### From GameLib ###
//////////////////////////////////////////////////////////////////////////
