#!/usr/bin/python
# coding: UTF-8
#####################################################
# public
#   Class   ：謎みん
#   Site URL：https://mynoghra.jp/
#   Update  ：2019/6/28
#####################################################
import os
import codecs
from getpass import getpass

#####################################################
class CLS_Admin():
#####################################################
	STR_Login = {
		"confirm"		: False,
		"username"		: "",
		"password"		: "",
		"loadpass"		: "",
		"Reason"		: None
	}

	DEF_MOJI_ENCODE = 'utf-8'				#ファイル文字エンコード


#####################################################
# 認証結果取得
#####################################################
	def GetStatus(self):
		return self.STR_Login['confirm']	#返すだけ



#####################################################
# 初期化
#####################################################
	def __init__(self):
		return



#####################################################
# 認証ユーザ、パスワードの設定 ※対話型
#####################################################
	def InputPath( self, inPath ):
		#############################
		# 開始
		wStr = "リモートからのAdministrator接続情報の作成をおこないます。"
		print( wStr )
		
		#############################
		# username名
		wStr = '\n' + "Administratorのusername名を入力してください"
		print( wStr )
		wInput = input( "=> " ).strip()
		if wInput=="" :
			print( "Administratorの接続情報の作成がキャンセルされました" )
			return False	#キャンセル
		self.STR_Login['username'] = wInput
		
		#############################
		# password
		wStr = '\n' + "Administratorのpasswordを入力してください"
		print( wStr )
		wInput = getpass( "=> " ).strip()
		if wInput=="" :
			print( "Administratorの接続情報の作成がキャンセルされました" )
			return False	#キャンセル
		self.STR_Login['password'] = wInput
		
		print( "Administratorの接続情報の作成中......" + '\n' )
		#############################
		# 書き込みデータを作成
		wSetLine = []
		wLine = self.STR_Login['username'] + self.STR_Login['password']
		wSetLine.append(wLine)
		
		#############################
		# ファイル上書き書き込み
		
		#############################
		# 存在チェック
		if os.path.exists( inPath )!=True :
			wStr = "作成失敗: ファイルがありません: " + inPath
			print( wStr )
			return False	#失敗
		
		#############################
		# 書き込み
		try:
			wFile = codecs.open( inPath, 'w', self.DEF_MOJI_ENCODE )
			wFile.writelines( wSetLine )
			wFile.close()
		except ValueError as err :
			return False
		
		print( "Administratorの接続情報の作成 成功!!" + '\n' )
		return True



#####################################################
# dbdataのロード
#####################################################
	def __loadPass( self, inPath ):
		#############################
		# Login 初期化
		self.STR_Login['confirm']  = False
		self.STR_Login['loadpass'] = ""
		
		#############################
		# 存在チェック
		wRes = os.path.exists( inPath )
		if wRes==False :
			self.STR_Login['Reason'] = "CLS_Admin: __loadPass: AdminInfo file is not found: " + inPath
			return False
		
		#############################
		# Login情報に読み出す
		try:
			for wLine in open( inPath, 'r'):	#ファイルを開く
				wLine = wLine.strip()
				self.STR_Login['loadpass'] = wLine
			
		except ValueError as err :
			self.STR_Login['Reason'] = "CLS_Admin: __loadPass: Load AdminInfo file Failed: " + err
			return False
		
		#############################
		# 正常
		return True



#####################################################
# 認証
#####################################################
	def Confirm( self, inPath, inUsername, inPassword ):
		
		#############################
		# 設定したAdmin情報のロード
		if self.__loadPass( inPath )!=True :
			self.STR_Login['confirm'] = False
			return False
		
		#############################
		# Passの作成
		wPass = inUsername + inPassword
		
		#############################
		# 認証
		if self.STR_Login['loadpass']!=wPass :
			self.STR_Login['Reason'] = "CLS_Admin: Confirm: Login confirm is failed"
###			self.STR_Login['Reason'] = "CLS_Admin: Confirm: Login confirm is failed: " + self.STR_Login['loadpass'] + " : " + wPass
			self.STR_Login['confirm'] = False
			return False
		
		#############################
		# 正常
		self.STR_Login['confirm'] = True
		return True


