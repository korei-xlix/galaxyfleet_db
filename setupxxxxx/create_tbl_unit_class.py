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
class CLS_Create_TBL_UNIT_CLASS() :
#####################################################

	sOBJ_DB        = ""
	sCHR_TableName = ""

#####################################################
# 初期化
#####################################################
	def __init__( self, in_DB_Obj=None ):
		self.sOBJ_DB        = in_DB_Obj
		self.sCHR_TableName = "TBL_UNIT_CLASS"
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
					"class    CHAR(4)    NOT NULL," + \
					"kind     CHAR(2)    NOT NULL," + \
					"name     CHAR(10)   NOT NULL," + \
					"name_en  CHAR(40)   NOT NULL," + \
					" PRIMARY KEY ( class ) ) ;"

#CREATE TABLE Staff
#(id    CHAR(4)    NOT NULL,
#name   TEXT       NOT NULL,
#age    INTEGER    ,
#PRIMARY KEY (id));


		self.sOBJ_DB.RunQuery( wQuery )

#############################
# **** データの挿入 ****
		###戦列艦
		self.__insert( "BSDS", "BS", "駆逐艦",   "Destroyer" )
		self.__insert( "BSCR", "BS", "巡航艦",   "Cruiser" )
		self.__insert( "BSBB", "BS", "戦艦",     "Battle Ships" )
		self.__insert( "BSAC", "BS", "航空母艦", "Air Carrier" )
		self.__insert( "BSGC", "BS", "汎用母艦", "General Purpose Mother Ship" )
		self.__insert( "BSLC", "BS", "揚陸艦",   "Land Carrier" )
		self.__insert( "BSSB", "BS", "潜航艦",   "Submarine" )
		
		###護衛艦
		self.__insert( "ESCV", "ES", "防護艦",   "Escort Corvet" )
		self.__insert( "ESFG", "ES", "護衛艦",   "Escort Frigate" )
		self.__insert( "ESEC", "ES", "護衛母艦", "Escort Carrier" )
		
		###支援艦
		self.__insert( "SSRE", "SS", "偵察艦",   "Recommend Ship" )
		self.__insert( "SSTR", "SS", "輸送艦",   "Transport Ship" )
		self.__insert( "SSSS", "SS", "補給艦",   "Supply Ship" )
		self.__insert( "SSMS", "SS", "多用途支援艦", "Multipurpose Support Ship" )
		self.__insert( "SSBS", "SS", "戦闘支援艦",   "Battle Support Ship" )
		
		###機動兵器
		self.__insert( "MUSA", "MU", "艦載機",   "Shipboard Airplanes" )
		self.__insert( "MUMA", "MU", "航空機",   "Movable Airplanes" )
		self.__insert( "MUMS", "MU", "機動歩兵", "Movable Soldier" )
		self.__insert( "MUMB", "MU", "戦闘艇",   "Movable Boats" )
		
		###陸戦兵器
		self.__insert( "LULA", "LU", "陸戦攻撃機", "Land Airplane" )
		self.__insert( "LULS", "LU", "陸戦歩兵",   "Land Soldier" )
		self.__insert( "LULC", "LU", "戦闘車両",   "Land Car" )
		
		###防衛兵器
		self.__insert( "DUDU", "DU", "防衛兵器",   "Defense Unit" )
		self.__insert( "DULC", "DU", "拠点",       "Location" )
		self.__insert( "DUBT", "DU", "砲台",       "Battery" )
		self.__insert( "DUFU", "DU", "浮遊兵器",   "Floating Unit" )
		self.__insert( "DUIU", "DU", "設置兵器",   "Installed Unit" )
		
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
	def __insert( self, in_Class, in_Kind, in_Name, in_NameEN ):
		wQuery = "insert into " + self.sCHR_TableName + " values (" + \
					"'" + in_Class + "'," + \
					"'" + in_Kind + "'," + \
					"'" + in_Name + "'," + \
					"'" + in_NameEN + "'" + \
					") ;"
		
		self.sOBJ_DB.RunQuery( wQuery )
		return


