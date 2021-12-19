import app
import uiScriptLocale

LOCALE_PATH = uiScriptLocale.LOGIN_PATH
#Big-List
#SERVER_BOARD_HEIGHT = 180 + 390
#SERVER_LIST_HEIGHT = 171 + 350
#Small list like german
SERVER_BOARD_HEIGHT = 220 + 180
SERVER_LIST_HEIGHT = 171 + 180
SERVER_BOARD_WEIGHT = 375 

ID_LIMIT_COUNT = 19
PW_LIMIT_COUNT = 16

window = {
	"name" : "LoginWindow",
	"sytle" : ("movable",),

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	[

		## Board
		{
			"name" : "bg1", "type" : "expanded_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1024.0, "y_scale" : float(SCREEN_HEIGHT) / 768.0,
			"image" : "locale/ro/ui/serverlist.sub",
		},
		{
			"name" : "bg2", "type" : "expanded_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1024.0, "y_scale" : float(SCREEN_HEIGHT) / 768.0,
			"image" : "locale/ro/ui/login.sub",
		},

		## VirtualKeyboard
		{
			'name' : 'VirtualKeyboard',
			'type' : 'thinboard',
			'x' : (SCREEN_WIDTH - 564) / 2,
			'y' : SCREEN_HEIGHT - 320,
			'width' : 564,
			'height' : 254,
			'children' : 
			(
				{
					'name' : 'key_at',
					'type' : 'toggle_button',
					'x' : 40,
					'y' : 186,
					'default_image' : 'locale/ro/ui/vkey/key_at.tga',
					'down_image' : 'locale/ro/ui/vkey/key_at_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_at_over.tga',
				},
				{
					'name' : 'key_backspace',
					'type' : 'button',
					'x' : 498,
					'y' : 186,
					'default_image' : 'locale/ro/ui/vkey/key_backspace.tga',
					'down_image' : 'locale/ro/ui/vkey/key_backspace_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_backspace_over.tga',
				},
				{
					'name' : 'key_enter',
					'type' : 'button',
					'x' : 439,
					'y' : 186,
					'default_image' : 'locale/ro/ui/vkey/key_enter.tga',
					'down_image' : 'locale/ro/ui/vkey/key_enter_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_enter_over.tga',
				},
				{
					'name' : 'key_shift',
					'type' : 'toggle_button',
					'x' : 86,
					'y' : 186,
					'default_image' : 'locale/ro/ui/vkey/key_shift.tga',
					'down_image' : 'locale/ro/ui/vkey/key_shift_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_shift_over.tga',
				},
				{
					'name' : 'key_space',
					'type' : 'button',
					'x' : 145,
					'y' : 186,
					'default_image' : 'locale/ro/ui/vkey/key_space.tga',
					'down_image' : 'locale/ro/ui/vkey/key_space_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_space_over.tga',
				},
				{
					'name' : 'key_1',
					'type' : 'button',
					'x' : 40,
					'y' : 24,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_2',
					'type' : 'button',
					'x' : 80,
					'y' : 24,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_3',
					'type' : 'button',
					'x' : 120,
					'y' : 24,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_4',
					'type' : 'button',
					'x' : 160,
					'y' : 24,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_5',
					'type' : 'button',
					'x' : 200,
					'y' : 24,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_6',
					'type' : 'button',
					'x' : 240,
					'y' : 24,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_7',
					'type' : 'button',
					'x' : 280,
					'y' : 24,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_8',
					'type' : 'button',
					'x' : 320,
					'y' : 24,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_9',
					'type' : 'button',
					'x' : 360,
					'y' : 24,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_10',
					'type' : 'button',
					'x' : 400,
					'y' : 24,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_11',
					'type' : 'button',
					'x' : 440,
					'y' : 24,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_12',
					'type' : 'button',
					'x' : 480,
					'y' : 24,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_13',
					'type' : 'button',
					'x' : 40,
					'y' : 63,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_14',
					'type' : 'button',
					'x' : 80,
					'y' : 63,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_15',
					'type' : 'button',
					'x' : 120,
					'y' : 63,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_16',
					'type' : 'button',
					'x' : 160,
					'y' : 63,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_17',
					'type' : 'button',
					'x' : 200,
					'y' : 63,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_18',
					'type' : 'button',
					'x' : 240,
					'y' : 63,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_19',
					'type' : 'button',
					'x' : 280,
					'y' : 63,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_20',
					'type' : 'button',
					'x' : 320,
					'y' : 63,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_21',
					'type' : 'button',
					'x' : 360,
					'y' : 63,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_22',
					'type' : 'button',
					'x' : 400,
					'y' : 63,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_23',
					'type' : 'button',
					'x' : 440,
					'y' : 63,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_24',
					'type' : 'button',
					'x' : 480,
					'y' : 63,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_25',
					'type' : 'button',
					'x' : 60,
					'y' : 104,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_26',
					'type' : 'button',
					'x' : 100,
					'y' : 104,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_27',
					'type' : 'button',
					'x' : 140,
					'y' : 104,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_28',
					'type' : 'button',
					'x' : 180,
					'y' : 104,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_29',
					'type' : 'button',
					'x' : 220,
					'y' : 104,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_30',
					'type' : 'button',
					'x' : 260,
					'y' : 104,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_31',
					'type' : 'button',
					'x' : 300,
					'y' : 104,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_32',
					'type' : 'button',
					'x' : 340,
					'y' : 104,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_33',
					'type' : 'button',
					'x' : 380,
					'y' : 104,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_34',
					'type' : 'button',
					'x' : 420,
					'y' : 104,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_35',
					'type' : 'button',
					'x' : 460,
					'y' : 104,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_36',
					'type' : 'button',
					'x' : 60,
					'y' : 144,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_37',
					'type' : 'button',
					'x' : 100,
					'y' : 144,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_38',
					'type' : 'button',
					'x' : 140,
					'y' : 144,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_39',
					'type' : 'button',
					'x' : 180,
					'y' : 144,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_40',
					'type' : 'button',
					'x' : 220,
					'y' : 144,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_41',
					'type' : 'button',
					'x' : 260,
					'y' : 144,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_42',
					'type' : 'button',
					'x' : 300,
					'y' : 144,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_43',
					'type' : 'button',
					'x' : 340,
					'y' : 144,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_44',
					'type' : 'button',
					'x' : 380,
					'y' : 144,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_45',
					'type' : 'button',
					'x' : 420,
					'y' : 144,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_46',
					'type' : 'button',
					'x' : 460,
					'y' : 144,
					'default_image' : 'locale/ro/ui/vkey/key_normal.tga',
					'down_image' : 'locale/ro/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/ro/ui/vkey/key_normal_over.tga',
				},
			)
		},

		## ConnectBoard
		{
			"name" : "ConnectBoard",
			"type" : "thinboard",

			"x" : (SCREEN_WIDTH - 312) / 2,
			"y" : (SCREEN_HEIGHT - 430 - 35),
			"width" : 312,
			"height" : 30,

			"children" :
			(
				{
					"name" : "ConnectName",
					"type" : "text",

					"x" : 15,
					"y" : 0,
					"vertical_align" : "center",
					"text_vertical_align" : "center",

					"text" : uiScriptLocale.LOGIN_DEFAULT_SERVERADDR,
				},
				{
					"name" : "SelectConnectButton",
					"type" : "button",

					"x" : 150 + 104,
					"y" : 0,
					"vertical_align" : "center",

					"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/small_button_03.sub",

					"text" : uiScriptLocale.LOGIN_SELECT_BUTTON,
				},
			),
		},

		## LoginBoard
		{
			"name" : "LoginBoard",
			"type" : "image",

			"x" : (SCREEN_WIDTH - 312) / 2,
			"y" : (SCREEN_HEIGHT - 430),

			"image" : LOCALE_PATH + "loginwindow_new.sub",

			"children" :
			(
				{ 
					"name" : "ID_Text_window", "type" : "window", "x" : 45 + 52, "y" : 4, "width" : 120, "height" : 18,
					"children" :
					(
						{"name":"ID_Text", "type":"text", "x":0, "y":0, "text":uiScriptLocale.LOGIN_ID, "all_align" : "center"},
					),	
				},
				
				{ 
					"name" : "Password_Text_window", "type" : "window", "x" : 45 + 52, "y" : 41, "width" : 120, "height" : 18,
					"children" :
					(
						{"name":"Password_Text", "type":"text", "x":0, "y":0, "text":uiScriptLocale.LOGIN_PASSWORD, "all_align" : "center"},
					),	
				},
				
				{
					"name" : "ID_EditLine",
					"type" : "editline",

					"x" : 48 + 52,
					"y" : 23,

					"width" : 120,
					"height" : 18,

					"input_limit" : ID_LIMIT_COUNT,
					"enable_codepage" : 0,

					"r" : 1.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
				},
				{
					"name" : "Password_EditLine",
					"type" : "editline",

					"x" : 48 + 52,
					"y" : 60,

					"width" : 120,
					"height" : 18,

					"input_limit" : PW_LIMIT_COUNT,
					"secret_flag" : 1,
					"enable_codepage" : 0,

					"r" : 1.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
				},
				{
					"name" : "RegisterButton",
					"type" : "button",

					"x" : 15,
					"y" : 79,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : uiScriptLocale.LOGIN_REGISTER,
				},
				{
					"name" : "LoginButton",
					"type" : "button",

					"x" : 105,
					"y" : 79,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : uiScriptLocale.LOGIN_CONNECT,
				},
				{
					"name" : "LoginExitButton",
					"type" : "button",

					"x" : 195,
					"y" : 79,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : uiScriptLocale.LOGIN_EXIT,
				},
			),
		},

		## ServerBoard
		{
			"name" : "ServerBoard",
			"type" : "thinboard",

			"x" : 0,
			"y" : SCREEN_HEIGHT - SERVER_BOARD_HEIGHT - 72,
			"width" : 375,
			"height" : SERVER_BOARD_HEIGHT,
			"horizontal_align" : "center",

			"children" :
			[

				## Title
				{
					"name" : "Title",
					"type" : "text",

					"x" : 0,
					"y" : 12,
					"horizontal_align" : "center",
					"text_horizontal_align" : "center",
					"text" : uiScriptLocale.LOGIN_SELECT_TITLE,
				},

				## Horizontal
				{
					"name" : "HorizontalLine1",
					"type" : "line",

					"x" : 10,
					"y" : 34,
					"width" : 354,
					"height" : 0,
					"color" : 0xff777777,
				},
				{
					"name" : "HorizontalLine2",
					"type" : "line",

					"x" : 10,
					"y" : 35,
					"width" : 355,
					"height" : 0,
					"color" : 0xff111111,
				},

				## Vertical
				{
					"name" : "VerticalLine1",
					"type" : "line",

					"x" : 246,
					"y" : 38,
					"width" : 0,
					"height" : SERVER_LIST_HEIGHT + 4,
					"color" : 0xff777777,
				},
				{
					"name" : "VerticalLine2",
					"type" : "line",

					"x" : 247,
					"y" : 38,
					"width" : 0,
					"height" : SERVER_LIST_HEIGHT + 4,
					"color" : 0xff111111,
				},

				## Buttons
				{
					"name" : "ServerSelectButton",
					"type" : "button",

					"x" : 267,
					"y" : SERVER_LIST_HEIGHT,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : uiScriptLocale.OK,
				},
				{
					"name" : "ServerExitButton",
					"type" : "button",

					"x" : 267,
					"y" : SERVER_LIST_HEIGHT + 22,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : uiScriptLocale.LOGIN_SELECT_EXIT,
				},

			],

		},

	],
}

if not app.ENABLE_SERVER_SELECT_RENEWAL:
	window["children"][5]["children"] = window["children"][5]["children"] + [
				## ListBox
				{
					"name" : "ServerList",
					"type" : "listbox2",
	
					"x" : 10,
					"y" : 40,
					"width" : 232,
					"height" : SERVER_LIST_HEIGHT,
					"row_count" : 15,
					"item_align" : 0,
				},
				{
					"name" : "ChannelList",
					"type" : "listbox",
					"x" : 255,
					"y" : 40,
					"width" : 109,
					"height" : SERVER_LIST_HEIGHT-40,
	
					"item_align" : 0,
				},]

if app.INGAME_REGISTER:
	window["children"] = window["children"] + [
		{
			"name" : "bg3",
			"type" : "expanded_image",
			"x" : 0,
			"y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1909.0,
			"y_scale" : float(SCREEN_HEIGHT) / 876.0,
			"image" : "d:/ymir work/ui/register/background.jpg",
		},
		{
			"name" : "register_board",
			"type" : "window",
			"x" : 0,
			"y" : 0,
			"width" : SCREEN_WIDTH,
			"height" : SCREEN_HEIGHT,
			"children" : 
			[
				{
					"name" : "register_bar_top",
					"type" : "bar",
					"x" : (SCREEN_WIDTH / 2) - (380 / 2),
					"y" : (SCREEN_HEIGHT / 2) - (550 / 2) - 24,
					"width" : 380,
					"height" : 550,
					"color" : 0xFF121212,
					"children" : 
					[
						{
							"name" : "RegisterTitle",
							"type" : "text",
							"x" : 40,
							"y" : 20,
							"fontname" : "Arial:18b",
							"text" : uiScriptLocale.REGISTER_TITLE,
						},
						{
							"name" : "register_bar_line1",
							"type" : "bar",
							"x" : 40,
							"y" : 54,
							"width" : 300,
							"height" : 1,
							"color" : 0xFF303030,
						},
						#login
						{
							"name" : "RegisterLogin",
							"type" : "text",
							"x" : 40,
							"y" : 74,
							"color" : 0xC43F6A94,
							"fontname" : "Arial:17b",
							"text" : uiScriptLocale.LOGIN_ID,
						},
						{
							"name" : "register_bar_input1",
							"type" : "bar",
							"x" : 40,
							"y" : 104,
							"width" : 300,
							"height" : 38,
							"color" : 0xFF303030,
							"children" :
							[
								{
									"name" : "login_editline",
									"type" : "editline",
									"x" : 10,
									"y" : 12,
									"width" : 280,
									"height" : 26,
									"limit_width" : 280,
									"multi_line" : 1,
									"input_limit" : 1,
									"enable_codepage" : 0,
									"r" : 1.0,
									"g" : 1.0,
									"b" : 1.0,
									"a" : 1.0,
								},
							]
						},
						{
							"name" : "register_line1_input1",
							"type" : "bar",
							"x" : 40,
							"y" : 142,
							"width" : 300,
							"height" : 2,
							"color" : 0xC43F6A94,
						},
						{
							"name" : "register_line2_input1",
							"type" : "bar",
							"x" : 40,
							"y" : 142,
							"width" : 300,
							"height" : 2,
							"color" : 0xFFFF0000,
						},
						{
							"name" : "register_status_input1",
							"type" : "text",
							"x" : 40,
							"y" : 148,
							"color" : 0xFFFF0000,
							"text" : "",
						},
						#parola
						{
							"name" : "RegisterPassword",
							"type" : "text",
							"x" : 40,
							"y" : 74 + 100,
							"color" : 0xC43F6A94,
							"fontname" : "Arial:17b",
							"text" : uiScriptLocale.LOGIN_PASSWORD,
						},
						{
							"name" : "register_bar_input2",
							"type" : "bar",
							"x" : 40,
							"y" : 104 + 100,
							"width" : 300,
							"height" : 38,
							"color" : 0xFF303030,
							"children" :
							[
								{
									"name" : "password_editline",
									"type" : "editline",
									"x" : 10,
									"y" : 12,
									"width" : 280,
									"height" : 26,
									"limit_width" : 280,
									"multi_line" : 1,
									"input_limit" : 1,
									"enable_codepage" : 0,
									"r" : 1.0,
									"g" : 1.0,
									"b" : 1.0,
									"a" : 1.0,
								},
							]
						},
						{
							"name" : "register_line1_input2",
							"type" : "bar",
							"x" : 40,
							"y" : 142 + 100,
							"width" : 300,
							"height" : 2,
							"color" : 0xC43F6A94,
						},
						{
							"name" : "register_line2_input2",
							"type" : "bar",
							"x" : 40,
							"y" : 142 + 100,
							"width" : 300,
							"height" : 2,
							"color" : 0xFFFF0000,
						},
						{
							"name" : "register_status_input2",
							"type" : "text",
							"x" : 40,
							"y" : 148 + 100,
							"color" : 0xFFFF0000,
							"text" : "",
						},
						#email
						{
							"name" : "RegisterEmail",
							"type" : "text",
							"x" : 40,
							"y" : 74 + 200,
							"color" : 0xC43F6A94,
							"fontname" : "Arial:17b",
							"text" : uiScriptLocale.REGISTER_EMAIL,
						},
						{
							"name" : "register_bar_input3",
							"type" : "bar",
							"x" : 40,
							"y" : 104 + 200,
							"width" : 300,
							"height" : 38,
							"color" : 0xFF303030,
							"children" :
							[
								{
									"name" : "email_editline",
									"type" : "editline",
									"x" : 10,
									"y" : 12,
									"width" : 280,
									"height" : 26,
									"limit_width" : 280,
									"multi_line" : 1,
									"input_limit" : 1,
									"enable_codepage" : 1,
									"r" : 1.0,
									"g" : 1.0,
									"b" : 1.0,
									"a" : 1.0,
								},
							]
						},
						{
							"name" : "register_line1_input3",
							"type" : "bar",
							"x" : 40,
							"y" : 142 + 200,
							"width" : 300,
							"height" : 2,
							"color" : 0xC43F6A94,
						},
						{
							"name" : "register_line2_input3",
							"type" : "bar",
							"x" : 40,
							"y" : 142 + 200,
							"width" : 300,
							"height" : 2,
							"color" : 0xFFFF0000,
						},
						{
							"name" : "register_status_input3",
							"type" : "text",
							"x" : 40,
							"y" : 148 + 200,
							"color" : 0xFFFF0000,
							"text" : "",
						},
						#social
						{
							"name" : "RegisterSocial",
							"type" : "text",
							"x" : 40,
							"y" : 74 + 300,
							"color" : 0xC43F6A94,
							"fontname" : "Arial:17b",
							"text" : uiScriptLocale.REGISTER_SOCIALID,
						},
						{
							"name" : "register_bar_input4",
							"type" : "bar",
							"x" : 40,
							"y" : 104 + 300,
							"width" : 300,
							"height" : 38,
							"color" : 0xFF303030,
							"children" :
							[
								{
									"name" : "social_editline",
									"type" : "editline",
									"x" : 10,
									"y" : 12,
									"width" : 280,
									"height" : 26,
									"limit_width" : 280,
									"multi_line" : 1,
									"input_limit" : 1,
									"enable_codepage" : 0,
									"r" : 1.0,
									"g" : 1.0,
									"b" : 1.0,
									"a" : 1.0,
								},
							]
						},
						{
							"name" : "register_line1_input4",
							"type" : "bar",
							"x" : 40,
							"y" : 142 + 300,
							"width" : 300,
							"height" : 2,
							"color" : 0xC43F6A94,
						},
						{
							"name" : "register_line2_input4",
							"type" : "bar",
							"x" : 40,
							"y" : 142 + 300,
							"width" : 300,
							"height" : 2,
							"color" : 0xFFFF0000,
						},
						{
							"name" : "register_status_input4",
							"type" : "text",
							"x" : 40,
							"y" : 148 + 300,
							"color" : 0xFFFF0000,
							"text" : "",
						},
						{
							"name" : "register_create_btn",
							"type" : "button",
							"x" : 40,
							"y" : 80 + 400,
							"default_image" : "d:/ymir work/ui/register/register_btn_01.jpg",
							"over_image" : "d:/ymir work/ui/register/register_btn_02.jpg",
							"down_image" : "d:/ymir work/ui/register/register_btn_03.jpg",
							"disable_image" : "d:/ymir work/ui/register/register_btn_04.jpg",
							"children" : 
							[
								{
									"name" : "RegisterCreate",
									"type" : "text",
									"x" : 0,
									"y" : 0,
									"all_align" : 1,
									"color" : 0xFFFFFFFF,
									"fontname" : "Arial:17b",
									"text" : uiScriptLocale.REGISTER_CREATE,
								},
							],
						},
						{
							"name" : "register_create_status",
							"type" : "text",
							"x" : 40,
							"y" : 126 + 400,
							"text" : "",
						},
					],
				},
				{
					"name" : "register_bar_bottom",
					"type" : "bar",
					"x" : (SCREEN_WIDTH / 2) - (380 / 2),
					"y" : (SCREEN_HEIGHT / 2) + (550 / 2) - 24,
					"width" : 380,
					"height" : 48,
					"color" : 0xF51D2327,
					"children" : 
					[
						{
							"name" : "register_login_btn",
							"type" : "button",
							"x" : 0,
							"y" : 0,
							"width" : 380,
							"height" : 48,
							"children" : 
							[
								{
									"name" : "RegisterCreate",
									"type" : "text",
									"x" : 0,
									"y" : 0,
									"all_align" : 1,
									"color" : 0xFFFFFFFF,
									"fontname" : "Arial:17b",
									"text" : uiScriptLocale.REGISTER_LOGIN,
								},
							],
						},
					],
				},
			],
		},
	]
