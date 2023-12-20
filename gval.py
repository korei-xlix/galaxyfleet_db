#!/usr/bin/python
# coding: UTF-8
#####################################################
# ::Project  : Galaxy Fleet
# ::Admin    : Korei (@korei-xlix)
# ::github   : https://github.com/korei-xlix/koreibot_win/
# ::Class    : グローバル値
#####################################################

#####################################################
class gVal() :

#############################
# ※ユーザ自由変更※
	DEF_TIMEZONE = 9										# 9=日本時間 最終更新日補正用
	DEF_MOJI_ENCODE = 'utf-8'								#文字エンコード
	DEF_ADMIN    = 'admin'									#管理者ID

#############################
# システム情報
	#データversion(文字)
	DEF_CONFIG_VER = "1"

	STR_SystemInfo = {
		"Client_Name"	: "これーぼっと",
		"github"		: "",
		"Admin"			: "",
		"PythonVer"		: 0,
		"HostName"		: "",
		
		"EXT_FilePath"	: None,
		
		"RunMode"		: "normal"
			# normal= 通常モード
			# setup = セットアップモード
			# init  = 全初期化モード
			# clear = データクリア
	}

#############################
# ユーザ情報
	STR_UserInfo = {
		"Account"		: "",			#Twitterアカウント名
		"id"			: "",			#Twitter ID(番号)
		
		"TrendTag"		: "",			#トレンドタグ設定
		"QuestionTag"	: "",			#質問タグ設定
		
		"ListID"		: None,			#リスト通知 リストID
		"ListName"		: None,			#リスト通知 リスト名
		
		"AutoRemove"	: False,		#自動リムーブ True=有効
		"mListID"		: None,			#相互フォローリスト リストID
		"mListName"		: None,			#相互フォローリスト リスト名
		"fListID"		: None,			#片フォロワーリスト リストID
		"fListName"		: None,			#片フォロワーリスト リスト名
		
		"Traffic"		: False,		#Twitterにトラヒックを報告するか
		
		"VipTag"		: None,			#VIPリツイート 対象タグ
		
		"AutoSeq"		: 0,			#自動監視シーケンス
		
		"mfvstop"		: False,		#相互いいね停止 true=有効
		"mfvstop_date"	: None			#相互いいね停止 開始日
	}

#############################
# 時間情報
	STR_Time = {
										# 各実行時間
		"run"			: None,			# コマンド実行
		"autorun"		: None,			# 自動監視
		"autoseq"		: None,			# 自動監視シーケンス
		"reaction"		: None,			# リアクション受信
		"mffavo"		: None,			# 相互フォローリストいいね
		"flfavo"		: None,			# フォロワー支援いいね
		"list_clear"	: None,			# リスト通知クリア
		"auto_remove"	: None,			# 自動リムーブ
		"send_favo"		: None,			# いいね情報送信
		"auto_delete"	: None,			# 自動削除
		"vip_ope"		: None,			# VIP監視
		"tl_follow"		: None,			# タイムラインフォロー
		
		"TimeDate"		: None			# システム時間
	}







#############################
# ファイルパス
#   ファイルは語尾なし、フォルダは_path
	DEF_STR_FILE = {
									# readme.md ファイルパス
		"Readme"				: "readme.md",
		
									# 除外データアーカイブ ファイル名
		"ExcWordArc"			: "/DEF_ExcWordArc.zip",
									# 除外データアーカイブ 解凍先フォルダパス
		"Melt_ExcWordArc_path"	: "/DEF_ExcWordArc",
									# 除外データ 文字列ファイルパス(フォルダ付き)
		"Melt_ExcWord"			: "/DEF_ExcWordArc/DEF_ExcWord.txt",
									# 禁止ユーザファイルパス(フォルダ付き)
		"Melt_ExcUser"			: "/DEF_ExcWordArc/DEF_ExcUser.txt",
									# リストいいね指定ファイル
		"Melt_ListFavo"			: "/DEF_ExcWordArc/DEF_ListFavo.txt",
		
									# ログの退避フォルダ
		"LogBackup_path"		: "../koreibot_win_log",
		"(dummy)"				: 0
	}

	DEF_DISPPATH = "script/disp/"

	DEF_STR_DISPFILE = {
		"MainConsole"			: DEF_DISPPATH + "main_console.disp",
		"UserAdminConsole"		: DEF_DISPPATH + "useradmin_console.disp",
		"KeywordConsole"		: DEF_DISPPATH + "keyword_console.disp",
		"ListFavoConsole"		: DEF_DISPPATH + "listfavo_console.disp",
		"ExcUserConsole"		: DEF_DISPPATH + "excuser_console.disp",
		"CautionConsole"		: DEF_DISPPATH + "caution_console.disp",
		"UserBConsole"			: DEF_DISPPATH + "userb_console.disp",
		
		"TrafficReport"			: DEF_DISPPATH + "traffic_report.disp",
		
		"SystemConfigConsole"	: DEF_DISPPATH + "system_config_console.disp",
		"SystemViewConsole"		: DEF_DISPPATH + "system_view_console.disp",
		"(dummy)"				: 0
	}

#############################
# 定数
	DEF_LOCK_LOOPTIME = 2									#ロック解除待ち
	DEF_LOCK_WAITCNT  = 30									#  待ち時間: DEF_LOCK_LOOPTIME * DEF_LOCK_WAITCNT
	DEF_TEST_MODE     = "bottest"							#テストモード(引数文字)
	DEF_DATA_BOUNDARY = "|,|"
	
	DEF_SCREEN_NAME_SIZE = 24

	DEF_VAL_DAY  = 86400									# 時間経過: 1日  60x60x24
	DEF_VAL_WEEK = 604800									# 時間経過: 7日  (60x60x24)x7
	
	DEF_TIMEDATE = "1901-01-01 00:00:00"
	DEF_NOTEXT   = "(none)"

	DEF_ADMINLOG_POINT = 12

#############################
# 変数
	FLG_Test_Mode    = False								#テストモード有無
	
	OBJ_Tw_IF = ""											#Twitter I/F
	OBJ_DB_IF = ""											#DB I/F
	OBJ_L     = ""											#ログ用
	
	ARR_ExeWord = {}										# 除外文字データ
	ARR_ExeWordKeys = []
	ARR_ListFavo = {}										# リストいいね指定
	ARR_NotReactionUser = {}								# リアクション禁止ユーザ
	ARR_SearchData = {}										# 検索データ
	ARR_CautionTweet = {}									# 警告ツイート



