#!/usr/bin/python
# coding: UTF-8
#####################################################
# ::Project  : Korei Bot Win
# ::Admin    : Korei (@korei-xlix)
# ::github   : https://github.com/korei-xlix/koreibot_win/
# ::Class    : bot制御(共通)
#####################################################
from mylog import CLS_Mylog
from db_if import CLS_DB_IF
from twitter_if import CLS_Twitter_IF

from traffic import CLS_Traffic
from ktime import CLS_TIME
from osif import CLS_OSIF
from filectrl import CLS_File
from gval import gVal
#####################################################
class CLS_BotCtrl():
#####################################################

#####################################################
# Botテスト
#####################################################
	@classmethod
	def sBotTest(cls):
		#############################
		# 応答形式の取得
		#   "Result" : False, "Class" : None, "Func" : None, "Reason" : None, "Responce" : None
		wRes = CLS_OSIF.sGet_Resp()
		wRes['Class'] = "CLS_BotCtrl"
		wRes['Func']  = "sBotTest"
		
		wRes['Responce'] = {
			"hostname"		: None,
			"database"		: None,
			"username"		: None,
			"password"		: None
		}
		#############################
		# 引数取得
		wArg = CLS_OSIF.sGetArg()
		
###		if len(wArg)<6 :	#引数が足りない
		if wArg[1]!="ping" and len(wArg)<6 :	#引数が足りない
			wRes['Reason'] = "CLS_BotCtrl: sBotTest: 引数が足りません(1)= " + str( wArg )
			CLS_OSIF.sErr( wRes )
			return wRes
		
		#############################
		# モード、DB情報の取得
###		wRes['Responce']['hostname'] = wArg[2]
###		wRes['Responce']['database'] = wArg[3]
###		wRes['Responce']['username'] = wArg[4]
###		wRes['Responce']['password'] = wArg[5]
		if wArg[1]!="ping" :
			wRes['Responce']['hostname'] = wArg[2]
			wRes['Responce']['database'] = wArg[3]
			wRes['Responce']['username'] = wArg[4]
			wRes['Responce']['password'] = wArg[5]
		
		#############################
		# setup : セットアップモード
		elif wArg[1]=="setup" :
			if len(wArg)!=6 and len(wArg)!=7 :
				wRes['Reason'] = "CLS_BotCtrl: sBotTest: 引数が足りません(3)= " + str( wArg )
				CLS_OSIF.sErr( wRes )
				return wRes
			
			gVal.STR_SystemInfo['RunMode'] = wArg[1]
			
			if len(wArg)==7 :
				gVal.STR_SystemInfo['EXT_FilePath'] = wArg[6]
			
			wRes['Result'] = True	#正常
			return wRes
		
		#############################
		# init  : 初期化モード
		elif wArg[1]=="init" :
			if len(wArg)!=6 and len(wArg)!=7 :
				wRes['Reason'] = "CLS_BotCtrl: sBotTest: 引数が足りません(4)= " + str( wArg )
				CLS_OSIF.sErr( wRes )
				return wRes
			
			gVal.STR_SystemInfo['RunMode'] = wArg[1]
			
			if len(wArg)==7 :
				gVal.STR_SystemInfo['EXT_FilePath'] = wArg[6]
			
			wRes['Result'] = True	#正常
			return wRes
		
		#############################
		# test : テストモード
		elif wArg[1]==gVal.DEF_TEST_MODE :
			if len(wArg)!=7 :
				wRes['Reason'] = "CLS_BotCtrl: sBotTest: 引数が足りません(7)= " + str( wArg )
				CLS_OSIF.sErr( wRes )
				return wRes
			
			gVal.FLG_Test_Mode = True
		
		else:
			wRes['Reason'] = "CLS_BotCtrl: sBotTest: コマンドがありません= " + str( wArg )
			CLS_OSIF.sErr( wRes )
			return wRes
		
		gVal.STR_SystemInfo['RunMode'] = "Normal"
		gVal.STR_UserInfo['Account']   = wArg[6]
		
		#############################
		# DBに接続
		gVal.OBJ_DB_IF = CLS_DB_IF()
		wSubRes = gVal.OBJ_DB_IF.Connect( wRes['Responce'] )
		if wSubRes['Result']!=True :
			wRes['Reason'] = "CLS_BotCtrl: sBotTest: DB接続失敗: reason=" + wResDB['Reason']
			CLS_OSIF.sErr( wRes )
			return wRes
		if wSubRes['Responce']!=True :
			##テーブルがない= 初期化してない
			wRes['Reason'] = "CLS_BotCtrl: sBotTest: DB未構築"
			CLS_OSIF.sErr( wRes )
			gVal.OBJ_DB_IF.Close()
			return wRes
		
		#############################
		# ログオブジェクトの生成
		gVal.OBJ_L = CLS_Mylog()
		
		#############################
		# 時間を取得
		wTD = CLS_TIME.sGet( wRes, "(1)" )
		if wTD['Result']!=True :
			cls.sBotEnd()	#bot終了
			return wRes
		### wTD['TimeDate']
		#############################
		# コマンド実行時間を設定
		wTimeRes = gVal.OBJ_DB_IF.SetTimeInfo( gVal.STR_UserInfo['Account'], "run", wTD['TimeDate'] )
		if wTimeRes['Result']!=True :
			wRes['Reason'] = "SetTimeInfo is failed"
			gVal.OBJ_L.Log( "B", wRes )
			return wRes
		
		#############################
		# Version情報
		wReadme = []
		if CLS_File.sReadFile( gVal.DEF_STR_FILE['Readme'], outLine=wReadme )!=True :
			wRes['Reason'] = "Readme.mdファイルが見つかりません: path=" + gVal.DEF_STR_FILE['Readme']
			gVal.OBJ_L.Log( "D", wRes )
			cls.sBotEnd()	#bot終了
			return wRes
		
		if len(wReadme)<=1 :
			wRes['Reason'] = "Readme.mdファイルが空です: path=" + gVal.DEF_STR_FILE['Readme']
			gVal.OBJ_L.Log( "D", wRes )
			cls.sBotEnd()	#bot終了
			return wRes
		
		for wLine in wReadme :
			#############################
			# 分解+要素数の確認
			wLine = wLine.strip()
			wGetLine = wLine.split("= ")
			if len(wGetLine) != 2 :
				continue
			
			wGetLine[0] = wGetLine[0].replace("::", "")
			#############################
			# キーがあるか確認
			if wGetLine[0] not in gVal.STR_SystemInfo :
				continue
			
			#############################
			# キーを設定
			gVal.STR_SystemInfo[wGetLine[0]] = wGetLine[1]
		
		#############################
		# 時間情報の取得
		wListRes = gVal.OBJ_DB_IF.GetTimeInfo( gVal.STR_UserInfo['Account'] )
		if wListRes['Result']!=True :
			wRes['Reason'] = "GetTimeInfo is failed"
			gVal.OBJ_L.Log( "B", wRes )
			return wRes
		
		#############################
		# システム情報の取得
		wCLS_work = CLS_OSIF()
		gVal.STR_SystemInfo['PythonVer'] = wCLS_work.Get_PythonVer()
		gVal.STR_SystemInfo['HostName']  = wCLS_work.Get_HostName()
		
		#############################
		# ログに記録する
		if gVal.FLG_Test_Mode==False :
			gVal.OBJ_L.Log( "S", wRes, "bot実行" )
		else:
			# テストモード
			gVal.OBJ_L.Log( "S", wRes, "bot実行(テストモード)" )
		
		#############################
		# テスト終了
		wRes['Result'] = True	#正常
		return wRes



