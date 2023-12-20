#!/usr/bin/python
# coding: UTF-8
#####################################################
# ::Project  : Korei Bot Win
# ::Admin    : Korei (@korei-xlix)
# ::github   : https://github.com/korei-xlix/koreibot_win/
# ::Class    : メイン処理(コンソール)
#####################################################

from ktime import CLS_TIME
from osif import CLS_OSIF
from traffic import CLS_Traffic
from filectrl import CLS_File
from setup import CLS_Setup
from botctrl import CLS_BotCtrl
from mydisp import CLS_MyDisp

from twitter_main import CLS_TwitterMain
from gval import gVal
#####################################################
class CLS_Main_Console() :
#####################################################
	#使用クラス実体化
	OBJ_TwitterMain = ""
	
	FLG_MainDispClear = True

#####################################################
# 実行
#####################################################
	@classmethod
	def sRun(cls):
		#############################
		# 応答形式の取得
		#   "Result" : False, "Class" : None, "Func" : None, "Reason" : None, "Responce" : None
		wRes = CLS_OSIF.sGet_Resp()
		wRes['Class'] = "CLS_Main_Console"
		wRes['Func']  = "sRun"
		
		#############################
		# 時間を取得
		wSubRes = CLS_TIME.sTimeUpdate()
		if wSubRes['Result']!=True :
			###時間取得失敗  時計壊れた？
			wRes['Reason'] = "TimeUpdate is failed"
			CLS_OSIF.sErr( wRes )
			return wRes
		
		#############################
		# 実行チェック
		wTestRes = cls.sCheckTest()
		if wTestRes!=True :
			###処理終了
			CLS_OSIF.sInp( '\n' + "リターンキーを押して再度コンソールアプリを起動してください。[RT]" )
			return wRes
		






		### ※通常処理継続
		


			
		return








#####################################################
# 実行チェック処理
#####################################################
	@classmethod
	def sCheckTest(cls):
		#############################
		# botテスト、引数ロード
		#   テスト項目
		#     1.引数ロード
		#     2.データベースの取得
		#     3.ログの取得
		#     4.排他
		#     5.Twitterの取得
		#     6.Readme情報の取得
		#     7.Python情報の取得
		#     8.TESTログ記録
		wResTest = CLS_BotCtrl.sBotTest()
		if wResTest['Result']!=True :
			return False	###問題あり
		
		wCLS_Setup = CLS_Setup()
		#############################
		# セットアップモードで実行
		if gVal.STR_SystemInfo['RunMode']=="setup" :
			wCLS_Setup.Setup( wResTest['Responce'] )
			return False	###問題あり
		
		#############################
		# 初期化モードで実行
		elif gVal.STR_SystemInfo['RunMode']=="init" :
			wCLS_Setup.AllInit( wResTest['Responce'] )
			return False	###問題あり
		
		#############################
		# データ追加モードで実行
		elif gVal.STR_SystemInfo['RunMode']=="add" :
			wCLS_Setup.Add( wResTest['Responce'] )
			return False	###問題あり
		
		#############################
		# 禁止ワード追加モードで実行
		elif gVal.STR_SystemInfo['RunMode']=="word" :
			wCLS_Setup.Add( wResTest['Responce'], inWordOnly=True )
			return False	###問題あり
		
		#############################
		# データクリアモードで実行
		elif gVal.STR_SystemInfo['RunMode']=="testclear" :
			wCLS_Setup.testClear( wResTest['Responce'] )
			return False	###問題あり
		
		#############################
		# PINGテストで実行
		elif gVal.STR_SystemInfo['RunMode']=="ping" :
			wCLS_Setup.Ping( wResTest['Responce']['hostname'] )
			return False	###問題あり
		
		#############################
		# =正常
		return True






