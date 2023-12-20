#!/usr/bin/python
# coding: UTF-8
#####################################################
# Star Region
#   Class   ：setup
#   Site URL：https://mynoghra.jp/
#   Update  ：2019/6/28
#####################################################
from osif import CLS_OSIF

#####################################################
class CLS_Create_TBL_NATION() :
#####################################################

	sOBJ_DB        = ""
	sCHR_TableName = ""

#####################################################
# 初期化
#####################################################
	def __init__( self, in_DB_Obj=None ):
		self.sOBJ_DB        = in_DB_Obj
		self.sCHR_TableName = "TBL_NATION"
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
					"flag     CHAR(2)    NOT NULL," + \
					"name     CHAR(20)   NOT NULL," + \
					"name_en  CHAR(40)   NOT NULL," + \
					" PRIMARY KEY ( flag ) ) ;"
		
		self.sOBJ_DB.RunQuery( wQuery )

#############################
# **** データの挿入 ****
		self.__insert( "UK", "ユグドキア連合王国",       "United Kingdom of Yugdokia" )
		self.__insert( "US", "アガルタ合衆国",           "United States of Agarta" )
		self.__insert( "VP", "フォルクパン公国",         "Principality of Volkpan" )
		self.__insert( "VL", "自由フォルクパン",         "Volkpan Libre" )
		self.__insert( "JC", "ミーミス共同連合",         "Memiss Joint Coalition" )
		self.__insert( "RE", "ウルザ共和国",             "Republic Urza" )
		self.__insert( "EP", "タナイス帝国",             "Tanais Empire" )
		self.__insert( "SF", "スヴァルト社会主義連邦",   "Swart Socialist Federation" )
		self.__insert( "PR", "ニザヴェッリル人民共和国", "Nizavell People''s Republic" )
		self.__insert( "IC", "ヨトンハイム皇国",         "Jotonheim Imperial Country" )
		self.__insert( "UN", "ミズガルズ連合",           "Mizugalz Union" )
		self.__insert( "LF", "ビフロスト解放戦線",       "Bifrost Liberation Front" )
		self.__insert( "FD", "ハバージガルム連盟",       "Huberge-Galum Federation" )
		self.__insert( "DR", "ニーブルグ民主共和国",     "Niburg Democratic Republic" )
		self.__insert( "KG", "ギヌンガープ王国",         "Guinung-Gap Kingdom" )
		self.__insert( "EI", "ムスパル首長国",           "Muspal Emirates" )
		self.__insert( "AL", "ウィグリド諸国同盟",       "Wigride Alliance" )
		self.__insert( "BC", "黒色連星団",               "Black Star Cluster" )
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
	def __insert( self, in_Flag, in_Name, in_NameEN ):
		wQuery = "insert into " + self.sCHR_TableName + " values (" + \
					"'" + in_Flag + "'," + \
					"'" + in_Name + "'," + \
					"'" + in_NameEN + "'" + \
					") ;"
		
		self.sOBJ_DB.RunQuery( wQuery )
		return


