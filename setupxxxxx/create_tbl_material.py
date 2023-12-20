#!/usr/bin/python
# coding: UTF-8
#####################################################
# Star Region
#   Class   ：setup
#   Site URL：https://mynoghra.jp/
#   Update  ：2019/7/4
#####################################################
from osif import CLS_OSIF

#####################################################
class CLS_Create_TBL_MATERIAL() :
#####################################################

	sOBJ_DB        = ""
	sCHR_TableName = ""

#####################################################
# 初期化
#####################################################
	def __init__( self, in_DB_Obj=None ):
		self.sOBJ_DB        = in_DB_Obj
		self.sCHR_TableName = "TBL_MATERIAL"
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
					"mate     CHAR(8)    NOT NULL," + \
					"name     CHAR(20)   NOT NULL," + \
					"name_en  CHAR(40)   NOT NULL," + \
					" PRIMARY KEY ( mate ) ) ;"
		
		self.sOBJ_DB.RunQuery( wQuery )

#############################
# **** データの挿入 ****
		self.__insert( "Fuel", "燃料",                 "Fuel" )
		self.__insert( "Stel", "鋼材",                 "Steel" )
		self.__insert( "HyPl", "ハイパープラスチック", "Hyper Plastic" )
		self.__insert( "RerM", "レアメタル",           "Rare Metals" )
		self.__insert( "Ammo", "弾薬",               "Ammunition" )
		self.__insert( "CorS", "コアストーン",       "Core Stone" )
		self.__insert( "GliS", "グリッターストーン", "Glitter Stone" )
		self.__insert( "Scrp", "スクラップストーン", "Scrap Stone" )
		self.__insert( "Capt", "資金",               "Capital" )
		self.__insert( "HSConst", "高速建造剤",      "H-Speed Construction" )
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
	def __insert( self, in_Mate, in_Name, in_NameEN ):
		wQuery = "insert into " + self.sCHR_TableName + " values (" + \
					"'" + in_Mate + "'," + \
					"'" + in_Name + "'," + \
					"'" + in_NameEN + "'" + \
					") ;"
		
		self.sOBJ_DB.RunQuery( wQuery )
		return


