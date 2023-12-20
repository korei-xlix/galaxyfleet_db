#!/usr/bin/python
# coding: UTF-8
#####################################################
# ::Project  : Galaxy Fleet
# ::Admin    : Korei (@korei-xlix)
# ::github   : https://github.com/korei-xlix/galaxyfleet/
# ::Class    : DBセットアップ
#####################################################
from mylog import CLS_Mylog

from osif import CLS_OSIF
from filectrl import CLS_File
from db_if import CLS_DB_IF
from twitter_if import CLS_Twitter_IF
from gval import gVal
#####################################################
class CLS_SetupDB():
#####################################################

#####################################################
# 初期化
#####################################################
	def __init__(self):
		return



#####################################################
# セットアップ
#####################################################
	def Setup( self, inData ):
		#############################
		# 応答形式の取得
		#   "Result" : False, "Class" : None, "Func" : None, "Reason" : None, "Responce" : None
		wRes = CLS_OSIF.sGet_Resp()
		wRes['Class'] = "CLS_Setup"
		wRes['Func']  = "Setup"
		
		CLS_OSIF.sPrn( "データベースのセットアップを開始します" + '\n' )
		






		#############################
		# DBに接続
		gVal.OBJ_DB_IF = CLS_DB_IF()
		wSubRes = gVal.OBJ_DB_IF.Connect( inData )
		if wSubRes['Result']!=True :
			return False
		if wSubRes['Responce']!=True :
			##テーブルがない= 初期化してない
			##DB初期化
			self.__initDB( gVal.OBJ_DB_IF.OBJ_DB )
			CLS_OSIF.sPrn( "データベースを初期化しました" + '\n' )
		







		#############################
		# ユーザチェック
		wSubRes = gVal.OBJ_DB_IF.CheckUserData()
		if wSubRes['Result']!=True :
			gVal.OBJ_DB_IF.Close()
			
			wSubRes['Reason'] = "ユーザチェックに失敗しました: " + wSubRes['Reason'] + '\n'
			CLS_OSIF.sErr( wSubRes )
			return False
		
		wTwitterAccount = wSubRes['Responce']['Account']
		#############################
		# ユーザありの場合
		if wSubRes['Responce']['detect']==True :
			wStr = "ユーザ " + wTwitterAccount + " は既に登録されています。キーの変更をおこないますか？" + '\n'
			CLS_OSIF.sPrn( wStr )
			wSelect = CLS_OSIF.sInp( "変更する？(y/N)=> " )
			if wSelect!="y" :
				###キャンセル
				wStr = "ユーザデータは正常でした。" + '\n'
				CLS_OSIF.sPrn( wStr )
				
				gVal.OBJ_DB_IF.Close()
				wRes['Result'] = True
				return wRes
		
		### ※ユーザ変更あり
		




		#############################
		# Twitterキーの入力と接続テスト
		gVal.OBJ_Tw_IF = CLS_Twitter_IF()
		wSubRes = gVal.OBJ_Tw_IF.SetTwitter( wTwitterAccount )
		if wSubRes['Result']!=True :
			gVal.OBJ_DB_IF.Close()
			
			wSubRes['Reason'] = "Twitterキーの入力と接続テストに失敗しました :" + wSubRes['Reason'] + '\n'
			CLS_OSIF.sErr( wSubRes )
			return False
		


		#############################
		# ユーザを登録、もしくは更新する
		wSubRes = gVal.OBJ_DB_IF.SetUserData( wSubRes['Responce'] )
		if wSubRes['Result']!=True :
			gVal.OBJ_DB_IF.Close()
			
			wSubRes['Reason'] = wSubRes['Reason'] + ": ユーザ登録に失敗しました。" + '\n'
			CLS_OSIF.sErr( wSubRes )
			return False
		





		
		#############################
		# 終わり
		gVal.OBJ_DB_IF.Close()
		return True



#####################################################
# 全初期化
#   作業ファイルとDBを全て初期化する
#####################################################
	def AllInit( self, inData ):
		#############################
		# 応答形式の取得
		#   "Result" : False, "Class" : None, "Func" : None, "Reason" : None, "Responce" : None
		wRes = CLS_OSIF.sGet_Resp()
		wRes['Class'] = "CLS_Setup"
		wRes['Func']  = "AllInit"
		
		#############################
		# 実行の確認
		wStr = "データベースと全ての作業ファイルをクリアします。" + '\n'
		CLS_OSIF.sPrn( wStr )
		wSelect = CLS_OSIF.sInp( "よろしいですか？(y/N)=> " )
		if wSelect!="y" :
			##キャンセル
			return True
		
		#############################
		# DBに接続 (接続情報の作成)
		gVal.OBJ_DB_IF = CLS_DB_IF()
		wSubRes = gVal.OBJ_DB_IF.Connect( inData )
		if wSubRes['Result']!=True :
			return False
		
		#############################
		# DB初期化
		self.__initDB( gVal.OBJ_DB_IF.OBJ_DB )
		CLS_OSIF.sPrn( "データベースを初期化しました" + '\n' )
		
		#############################
		# 終わり
		gVal.OBJ_DB_IF.Close()
		CLS_OSIF.sPrn( "全初期化が正常終了しました。" )
		
		#############################
		# セットアップの確認
		wStr = "続いてセットアップを続行しますか。" + '\n'
		CLS_OSIF.sPrn( wStr )
		wSelect = CLS_OSIF.sInp( "セットアップする？(y/N)=> " )
		if wSelect!="y" :
			##キャンセル
			return True
		
		###入力の手間を省くため、パスワードを引き継ぐ
		self.Setup( inData )
		return True



#####################################################
# データベースの初期化
#####################################################
	def __initDB( self, inDBobj ):
		self.__create_TBL_USER_DATA( inDBobj )
		
		self.__create_TBL_UNIT_KIND( inDBobj )
		self.__create_TBL_UNIT_CLASS( inDBobj )
		self.__create_TBL_UNIT_TYPE( inDBobj )
		self.__create_TBL_UNIT_DATA( inDBobj )
		
		self.__create_TBL_COUNTRY_KIND( inDBobj )
		
		self.__create_TBL_ADMIN_DATA( inDBobj )
		return True



#####################################################
# テーブル作成: TBL_USER_DATA
#####################################################
	def __create_TBL_USER_DATA( self, inOBJ_DB, inTBLname="tbl_user_data" ):
		#############################
		# テーブルのドロップ
		wQy = "drop table if exists " + inTBLname + ";"
		inOBJ_DB.RunQuery( wQy )
		
		#############################
		# テーブル枠の作成
		wQy = "create table " + inTBLname + "("
		wQy = wQy + "id          TEXT  NOT NULL,"		# ID
		wQy = wQy + "regdate     TIMESTAMP,"			# 登録日時
		wQy = wQy + "update      TIMESTAMP,"			# 更新日時
		wQy = wQy + "block       BOOL  DEFAULT false,"	# ブロック true=有効
		wQy = wQy + " PRIMARY KEY ( id ) ) ;"
		
		inOBJ_DB.RunQuery( wQy )
		return



#####################################################
# テーブル作成: TBL_UNIT_KIND
#####################################################
	def __create_TBL_UNIT_KIND( self, inOBJ_DB, inTBLname="tbl_unit_kind" ):
		#############################
		# テーブルのドロップ
		wQy = "drop table if exists " + inTBLname + ";"
		inOBJ_DB.RunQuery( wQy )
		
		#############################
		# テーブル枠の作成
		wQy = "create table " + inTBLname + "("
		wQy = wQy + "valid       BOOL  DEFAULT false,"	# 有効無効  true=有効
		wQy = wQy + "index       INTEGER,"				# Index Number
		wQy = wQy + "id          TEXT  NOT NULL,"		# ID
		wQy = wQy + "regdate     TIMESTAMP,"			# 登録日時
		wQy = wQy + "update      TIMESTAMP,"			# 更新日時
		wQy = wQy + "namejp      TEXT  NOT NULL,"		# 種別名（日本語）
		wQy = wQy + "nameen      TEXT  NOT NULL,"		# 種別名（英語）
		wQy = wQy + " PRIMARY KEY ( index ) ) ;"
		
		inOBJ_DB.RunQuery( wQy )
		return



#####################################################
# テーブル作成: TBL_UNIT_CLASS
#####################################################
	def __create_TBL_UNIT_CLASS( self, inOBJ_DB, inTBLname="tbl_unit_class" ):
		#############################
		# テーブルのドロップ
		wQy = "drop table if exists " + inTBLname + ";"
		inOBJ_DB.RunQuery( wQy )
		
		#############################
		# テーブル枠の作成
		wQy = "create table " + inTBLname + "("
		wQy = wQy + "valid       BOOL  DEFAULT false,"	# 有効無効  true=有効
		wQy = wQy + "index       INTEGER,"				# Index Number
		wQy = wQy + "id          TEXT  NOT NULL,"		# ID
		wQy = wQy + "regdate     TIMESTAMP,"			# 登録日時
		wQy = wQy + "update      TIMESTAMP,"			# 更新日時
		wQy = wQy + "kindid      TEXT  NOT NULL,"		# 関連 種別ID
		wQy = wQy + "namejp      TEXT  NOT NULL,"		# 分類名（日本語）
		wQy = wQy + "nameen      TEXT  NOT NULL,"		# 分類名（英語）
		wQy = wQy + " PRIMARY KEY ( index ) ) ;"
		
		inOBJ_DB.RunQuery( wQy )
		return



#####################################################
# テーブル作成: TBL_UNIT_TYPE
#####################################################
	def __create_TBL_UNIT_TYPE( self, inOBJ_DB, inTBLname="tbl_unit_type" ):
		#############################
		# テーブルのドロップ
		wQy = "drop table if exists " + inTBLname + ";"
		inOBJ_DB.RunQuery( wQy )
		
		#############################
		# テーブル枠の作成
		wQy = "create table " + inTBLname + "("
		wQy = wQy + "valid       BOOL  DEFAULT false,"	# 有効無効  true=有効
		wQy = wQy + "index       INTEGER,"				# Index Number
		wQy = wQy + "id          TEXT  NOT NULL,"		# ID
		wQy = wQy + "regdate     TIMESTAMP,"			# 登録日時
		wQy = wQy + "update      TIMESTAMP,"			# 更新日時
		wQy = wQy + "kindid      TEXT  NOT NULL,"		# 関連 種別ID
		wQy = wQy + "classid     TEXT  NOT NULL,"		# 関連 分類ID
		wQy = wQy + "namejp      TEXT  NOT NULL,"		# 形式名（日本語）
		wQy = wQy + "nameen      TEXT  NOT NULL,"		# 形式名（英語）
		wQy = wQy + " PRIMARY KEY ( index ) ) ;"
		
		inOBJ_DB.RunQuery( wQy )
		return



#####################################################
# テーブル作成: TBL_UNIT_DATA
#####################################################
	def __create_TBL_UNIT_DATA( self, inOBJ_DB, inTBLname="tbl_unit_data" ):
		#############################
		# テーブルのドロップ
		wQy = "drop table if exists " + inTBLname + ";"
		inOBJ_DB.RunQuery( wQy )
		
		#############################
		# テーブル枠の作成
		wQy = "create table " + inTBLname + "("
		wQy = wQy + "valid       BOOL  DEFAULT false,"	# 有効無効  true=有効
		wQy = wQy + "index       INTEGER,"				# Index Number
		wQy = wQy + "id          TEXT  NOT NULL,"		# ID
		wQy = wQy + "regdate     TIMESTAMP,"			# 登録日時
		wQy = wQy + "update      TIMESTAMP,"			# 更新日時
		wQy = wQy + "kindid      TEXT  NOT NULL,"		# 関連 種別ID
		wQy = wQy + "classid     TEXT  NOT NULL,"		# 関連 分類ID
		wQy = wQy + "typeid      TEXT  NOT NULL,"		# 関連 形式ID
		wQy = wQy + "countryid   TEXT  NOT NULL,"		# 製造国ID
		wQy = wQy + "namejp      TEXT  NOT NULL,"		# ユニット名（日本語）
		wQy = wQy + "nameen      TEXT  NOT NULL,"		# ユニット名（英語）
		wQy = wQy + "profjp      TEXT  NOT NULL,"		# プロフィール（日本語）
		wQy = wQy + "profen      TEXT  NOT NULL,"		# プロフィール（英語）




		wQy = wQy + " PRIMARY KEY ( index ) ) ;"
		
		inOBJ_DB.RunQuery( wQy )
		return






#####################################################
# テーブル作成: TBL_COUNTRY_KIND
#####################################################
	def __create_TBL_COUNTRY_KIND( self, inOBJ_DB, inTBLname="tbl_country_kind" ):
		#############################
		# テーブルのドロップ
		wQy = "drop table if exists " + inTBLname + ";"
		inOBJ_DB.RunQuery( wQy )
		
		#############################
		# テーブル枠の作成
		wQy = "create table " + inTBLname + "("
		wQy = wQy + "valid       BOOL  DEFAULT false,"	# 有効無効  true=有効
		wQy = wQy + "index       INTEGER,"				# Index Number
		wQy = wQy + "id          TEXT  NOT NULL,"		# ID
		wQy = wQy + "regdate     TIMESTAMP,"			# 登録日時
		wQy = wQy + "update      TIMESTAMP,"			# 更新日時
		wQy = wQy + "namejp      TEXT  NOT NULL,"		# 国名（日本語）
		wQy = wQy + "nameen      TEXT  NOT NULL,"		# 国名（英語）
		wQy = wQy + " PRIMARY KEY ( index ) ) ;"
		
		inOBJ_DB.RunQuery( wQy )
		return



#####################################################
# テーブル作成: TBL_ADMIN_DATA
#####################################################
	def __create_TBL_ADMIN_DATA( self, inOBJ_DB, inTBLname="tbl_admin_data" ):
		#############################
		# テーブルのドロップ
		wQy = "drop table if exists " + inTBLname + ";"
		inOBJ_DB.RunQuery( wQy )
		
		#############################
		# テーブル枠の作成
		wQy = "create table " + inTBLname + "("
		wQy = wQy + "id          TEXT  NOT NULL,"		# ID
		wQy = wQy + "regdate     TIMESTAMP,"			# 登録日時
		wQy = wQy + "update      TIMESTAMP,"			# 更新日時
		wQy = wQy + "pw          TEXT  NOT NULL,"		# パスワード
		wQy = wQy + " PRIMARY KEY ( id ) ) ;"
		
		inOBJ_DB.RunQuery( wQy )
		return



