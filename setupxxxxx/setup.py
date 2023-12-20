#!/usr/bin/python
# coding: UTF-8
#####################################################
# Star Region
#   Class   ：setup
#   Site URL：https://mynoghra.jp/
#   Update  ：2019/7/4
#####################################################
# Private Function:
#   (none)
#
# Instance Function:
#   (none)
#
# Class Function(static):
#   sRun(cls):
#
#####################################################

from osif import CLS_OSIF
from filectrl import CLS_File
from postgresql_use import CLS_PostgreSQL_Use
from admin import CLS_Admin


from create_tbl_unit_kind import CLS_Create_TBL_UNIT_KIND
from create_tbl_unit_class import CLS_Create_TBL_UNIT_CLASS
from create_tbl_unit_type import CLS_Create_TBL_UNIT_TYPE
from create_tbl_nation import CLS_Create_TBL_NATION
from create_tbl_material import CLS_Create_TBL_MATERIAL
from gval import gVal
#####################################################
class CLS_Setup() :
#####################################################

	#使用クラス実体化
	OBJ_DB    = ""
	OBJ_Mylog = ""

#####################################################
# 実行
#####################################################
	@classmethod
	def sRun(cls):
		#############################
		# 応答形式の取得
		#   "Result" : False, "Reason" : None, "Responce" : None
##		wRes = CLS_OSIF.sGet_Resp()
		
		#############################
		# 引数取得
		wArg = CLS_OSIF.sGetArg()
		if len(wArg)==3 :	#テストモードか
			if wArg[2]==gVal.DEF_TEST_MODE :
				gVal.FLG_Test_Mode = True
		
		elif len(wArg)!=2 :	#引数が足りない
			wStr = "CLS_Setup: Argument deficiency: argument=" + str( wArg )
			CLS_OSIF.sPrn( wStr  )
			return
		
		if wArg[1]!="init" and \
		   wArg[1]!="setup" :
			wStr = "CLS_Setup: Argument command is failed: argument=" + str( wArg )
			CLS_OSIF.sPrn( wStr  )
			return
		
		#############################
		# データフォルダのチェック
		if CLS_File.sExist( gVal.DEF_USERDATA_PATH )!=True :
			wStr = "CLS_Setup: Data folder is not found"
			CLS_OSIF.sPrn( wStr  )
			return
		
		#############################
		# DB接続情報ファイルのチェック
		if CLS_File.sExist( gVal.STR_File['DBinfo_File'] )!=True :
			###DB接続情報ファイルの作成(空ファイル)
			if CLS_File.sCopy(
				gVal.STR_File['defDBinfo_File'], gVal.STR_File['DBinfo_File'] )!=True :
				##失敗
				wStr = "CLS_Setup: DataBase file copy failed: src=" + gVal.STR_File['defDBinfo_File']
				wStr = wStr + " dst=" + gVal.STR_File['DBinfo_File']
				CLS_OSIF.sPrn( wStr  )
				return
		
		#############################
		# Administrator接続情報ファイルのチェック
		if CLS_File.sExist( gVal.STR_File['AdminInfo_File'] )!=True :
			###DB接続情報ファイルの作成(空ファイル)
			if CLS_File.sCopy(
				gVal.STR_File['defAdminInfo_File'], gVal.STR_File['AdminInfo_File'] )!=True :
				##失敗
				wStr = "CLS_Setup: AdminInfo file copy failed: src=" + gVal.STR_File['defAdminInfo_File']
				wStr = wStr + " dst=" + gVal.STR_File['AdminInfo_File']
				CLS_OSIF.sPrn( wStr  )
				return
		
		#############################
		# セットアップモード
		
		#############################
		# モード: setup
		if wArg[1]=="setup" :
			cls.OBJ_DB = CLS_PostgreSQL_Use()
			wOBJ_Admin = CLS_Admin()
			
			#############################
			# DB接続情報、Admin接続情報の作成
			if cls.OBJ_DB.CreateDBdata( gVal.STR_File['DBinfo_File'] )!=True :
				return
			if wOBJ_Admin.InputPath( gVal.STR_File['AdminInfo_File'] )!=True :
				return
			cls.OBJ_DB = CLS_PostgreSQL_Use( gVal.STR_File['DBinfo_File'] )
		
		#############################
		# モード: init
		elif wArg[1]=="init" :
			cls.OBJ_DB = CLS_PostgreSQL_Use( gVal.STR_File['DBinfo_File'] )
		
		#############################
		# モード: 該当なし
		else :
			###ありえない
			wStr = "CLS_Setup: Argument command is failed: argument=" + str( wArg )
			CLS_OSIF.sPrn( wStr  )
			return
		
		#############################
		# DBの状態チェック
		wRes = cls.OBJ_DB.GetIniStatus()
		if wRes['Result']!=True :
			###失敗
			wStr = "CLS_Setup: DB Connect test is failed: " + wRes['Reason']
			CLS_OSIF.sPrn( wStr  )
			return
		
#############################
# **** データの挿入 ****
		#############################
		# 兵器種別
		wOBJ_Data = CLS_Create_TBL_UNIT_KIND( cls.OBJ_DB )
		#############################
		# 兵器分類
		wOBJ_Data = CLS_Create_TBL_UNIT_CLASS( cls.OBJ_DB )
		#############################
		# 兵器型
		wOBJ_Data = CLS_Create_TBL_UNIT_TYPE( cls.OBJ_DB )
		
		#############################
		# 国家
		wOBJ_Data = CLS_Create_TBL_NATION( cls.OBJ_DB )
		#############################
		# 資源
		wOBJ_Data = CLS_Create_TBL_MATERIAL( cls.OBJ_DB )
		
#############################

#############################
#		if wArg[2]=="create" :
#			wQuery = "create table TEST_TABLE(" + \
#						"test1 int," + \
#						"test2 int" + \
#						") ;"
#
#		elif wArg[2]=="insert" :
#			wQuery = "insert into TEST_TABLE values ( 1, 201 ) ;"
#
#		elif wArg[2]=="select" :
#			wQuery = "select * from TEST_TABLE;"
#
#		elif wArg[2]=="check" :
#			wQuery = "select relname FROM pg_class WHERE relkind = \'r\' AND relname = \'" + "TEST_TABLE" + "\' ;"
#
#		elif wArg[2]=="table" :
#			wQuery = "select tablename from pg_tables where tablename not like 'pg_%' and schemaname like 'public';"
#
#		elif wArg[2]=="drop" :
#			wQuery = "drop table if exists TEST_TABLE;"
#
#		cls.OBJ_DB.RunQuery( wQuery )
#
#		wRes = cls.OBJ_DB.GetQueryStat()
#		wMsg = str(wRes['Result']) + ": " + str(wRes['Reason']) + "::: " + str(wRes['Responce'])
#		CLS_OSIF.sPrn( wMsg )
#
#		if wArg[2]=="select" or  wArg[2]=="table" :
#			wNum = len(wRes['Responce']['Data'])
#			CLS_OSIF.sPrn( str(wNum) )
#
#			wTable = ""
#			for wLine in wRes['Responce']['Data'] :
#				wTable = wTable + str(wLine) + '\n'
#			CLS_OSIF.sPrn( wTable )
#############################

		cls.OBJ_DB.Close()
#############################

		#############################
		# 正常終了
		CLS_OSIF.sPrn( "セットアップ正常終了" )
		return



##		cls().__testRun()
##		cls.OBJ_Mylog.Log( 'a', "てすと。"+'\n'+"てすちょーw"+'\n'+"てすと３。", True )
##		cls.OBJ_Mylog.Log( 'a', str(cls.FlgTest), True )

##		wVal = 0
##		cls().__testRun2( wVal )
##		CLS_OSIF.sPrn( str(wVal) )

##	def __testRun(cls):
##		cls.OBJ_Mylog.Log( 'a', "Test Log", True )
##		return

##	def __testRun2( cls, outVal ):
##		wVal = outVal
##		
##		wVal = 2
##		return



