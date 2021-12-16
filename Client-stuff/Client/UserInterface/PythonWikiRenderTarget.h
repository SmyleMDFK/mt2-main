#pragma once

#if defined(INGAME_WIKI)
#include "../gamelib/in_game_wiki.h"
#include "../EterPythonLib/PythonWindow.h"
#include "../eterLib/CWikiRenderTargetManager.h"
#include "../eterLib/GrpWikiRenderTargetTexture.h"

class CPythonWikiRenderTarget : public CSingleton<CPythonWikiRenderTarget>
{
	public:
		CPythonWikiRenderTarget();
		virtual ~CPythonWikiRenderTarget();
	
	public:
		const static	int32_t DELETE_PARM = -1;
		const static	int32_t START_MODULE = 1;
		
		typedef std::vector<std::tuple<int32_t, std::shared_ptr<UI::CUiWikiRenderTarget>>> TWikiRenderTargetModules;
		
		int32_t		GetFreeID();
		void		RegisterRenderModule(int32_t module_id, int32_t module_wnd);
		
		void		ManageModelViewVisibility(int32_t module_id, bool flag);
		
		void		ShowModelViewManager(bool flag) { _bCanRenderModules = flag; }
		bool		CanRenderWikiModules() const;
		
		void		SetModelViewModel(int32_t module_id, int32_t module_vnum);
		void		SetWeaponModel(int32_t module_id, int32_t weapon_vnum);
		void		SetModelForm(int32_t module_id, int32_t main_vnum);
		void		SetModelHair(int32_t module_id, int32_t hair_vnum);
		void		SetModelV3Eye(int32_t module_id, float x, float y, float z);
		void		SetModelV3Target(int32_t module_id, float x, float y, float z);
	
	protected:
		bool									_InitializeWindow(int32_t module_id, UI::CUiWikiRenderTarget* handle_window);
		std::shared_ptr<CWikiRenderTarget>		_GetRenderTargetHandle(int32_t module_id);
	
	private:
		TWikiRenderTargetModules				_RenderWikiModules;
		bool									_bCanRenderModules;
};
#endif
