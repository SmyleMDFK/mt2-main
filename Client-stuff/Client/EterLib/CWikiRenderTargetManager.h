#pragma once

#if defined(INGAME_WIKI)
#include <unordered_map>
#include <cstdint>
#include <memory>

#include "../EterBase/Singleton.h"
#include "../GameLib/in_game_wiki.h"

#include "CWikiRenderTarget.h"

class CWikiRenderTargetManager : public CSingleton<CWikiRenderTargetManager>
{
	public:
		CWikiRenderTargetManager();
		virtual ~CWikiRenderTargetManager();
		void InitializeData() { m_renderTargets.clear(); }
	
	public:
		std::shared_ptr<CWikiRenderTarget>	GetRenderTarget(int32_t module_id);
		bool								CreateRenderTarget(int32_t module_id, int32_t width, int32_t height);
		void								DeleteRenderTarget(int32_t module_id);
		
		void								CreateRenderTargetTextures();
		void								ReleaseRenderTargetTextures();
		
		void								DeformModels();
		void								UpdateModels();
		void								RenderModels();
	
	protected:
		std::unordered_map<int32_t, std::shared_ptr<CWikiRenderTarget>>	m_renderTargets;
};
#endif
