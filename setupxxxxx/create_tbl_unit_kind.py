#!/usr/bin/python
# coding: UTF-8
#####################################################
# Star Region
#   Class   ：setup
#   Site URL：https://mynoghra.jp/
#   Update  ：2019/6/13
#####################################################
from osif import CLS_OSIF

#####################################################
class CLS_Create_TBL_UNIT_KIND() :
#####################################################

	sOBJ_DB        = ""
	sCHR_TableName = ""

#####################################################
# 初期化
#####################################################
	def __init__( self, in_DB_Obj=None ):
		self.sOBJ_DB        = in_DB_Obj
		self.sCHR_TableName = "TBL_UNIT_KIND"
		self.__run()
		return



#####################################################
# 実行
#####################################################
	def __run(self):
		#############################
		# テーブルのドロップ
		wQuery = "drop table if exists " + self.sCHR_TableName + ";"
		self.sOBJ_DB.RunQuery( wQuery )
		
		#############################
		# テーブル枠の作成
		wQuery = "create table " + self.sCHR_TableName + "(" + \
					"kind     CHAR(2)    NOT NULL," + \
					"name     CHAR(10)   NOT NULL," + \
					"name_en  CHAR(40)   NOT NULL," + \
					" PRIMARY KEY ( kind ) ) ;"
		
		self.sOBJ_DB.RunQuery( wQuery )

#############################
# **** データの挿入 ****
		self.__insert( "BS", "戦列艦",   "Battle Ships" )
		self.__insert( "ES", "護衛艦",   "Escort Ships" )
		self.__insert( "SS", "支援艦",   "Support Ships" )
		self.__insert( "MU", "機動兵器", "Movable Unit" )
		self.__insert( "LU", "陸戦兵器", "Land Unit" )
		self.__insert( "DU", "防衛兵器", "Defense Unit" )
#############################
		
		#############################
		# データの確認
		wQuery = "select * from " + self.sCHR_TableName + ";"
		self.sOBJ_DB.RunQuery( wQuery )
		
		wRes = self.sOBJ_DB.GetQueryStat()
		wNum = len(wRes['Responce']['Data'])
		wTable = ""
		for wLine in wRes['Responce']['Data'] :
			wTable = wTable + str(wLine) + '\n'
		CLS_OSIF.sPrn( wTable )
		return


#####################################################
	def __insert( self, in_Kind, in_Name, in_NameEN ):
		wQuery = "insert into " + self.sCHR_TableName + " values (" + \
					"'" + in_Kind + "'," + \
					"'" + in_Name + "'," + \
					"'" + in_NameEN + "'" + \
					") ;"
		
		self.sOBJ_DB.RunQuery( wQuery )
		return


