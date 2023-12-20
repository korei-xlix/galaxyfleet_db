#!/usr/bin/python
# coding: UTF-8
#####################################################
# Star Region
#   Class   ：
#   Site URL：https://mynoghra.jp/
#   Update  ：2019/7/4
#####################################################

from postgresql_use import CLS_PostgreSQL_Use
from gval import gVal
#####################################################
class CLS_Download() :
#####################################################
	@classmethod
	def sBaseData( cls, inParam, outListSrc ):
		pListSrc = outListSrc
		if len(inParam)!=3 :
			gVal.STR_ScriptResp['Reason'] = "CLS_Download: Missing parameter"
			return False
		
		#############################
		# DB Open
		wOBJ_DB = CLS_PostgreSQL_Use( gVal.STR_File['DBinfo_File'] )
		
		#############################
		# DB check
		wRes = wOBJ_DB.GetIniStatus()
		if wRes['Result']!=True :
			gVal.STR_ScriptResp['Reason'] = "CLS_Download: DB Connect test is failed: " + wRes['Reason']
			return False
		
		#############################
		# Run Query
		wQuery = "select * from TBL_UNIT_KIND;"
		wOBJ_DB.RunQuery( wQuery )
		
		#############################
		# cSTRG_DOUNLOADDATA_Unit_Kind
		#   ※超ヒント: wLine はタプル形式
		wRes = wOBJ_DB.GetQueryStat()
###		wMsg = str(wRes['Result']) + ": " + str(wRes['Reason']) + "::: " + str(wRes['Responce'])
###		wNum = len(wRes['Responce']['Data'])

		wGetLine = "function cSTRG_DOUNLOADDATA_Unit_Kind() {"
		pListSrc.append( wGetLine )
		wGetLine = "  wData = new Array() ;"
		pListSrc.append( wGetLine )
		
		for wLineTap in wRes['Responce']['Data'] :
			wGetTap = []
			for wCel in wLineTap :
				wCel = wCel.strip()
				wGetTap.append( wCel )
			
			wGetLine = "  wData.push( new Array("
			wGetLine = wGetLine + "'" + wGetTap[0] + "', "
			wGetLine = wGetLine + "'" + wGetTap[1] + "', "
			wGetLine = wGetLine + "'" + wGetTap[2] + "'"
			wGetLine = wGetLine + ") ) ;"
			pListSrc.append( wGetLine )
		
		wGetLine = "  return wData ;"
		pListSrc.append( wGetLine )
		wGetLine = "}" + '\n'
		pListSrc.append( wGetLine )
		
		#############################
		# cSTRG_DOUNLOADDATA_Unit_Class
		wQuery = "select * from TBL_UNIT_CLASS;"
		wOBJ_DB.RunQuery( wQuery )
		wRes = wOBJ_DB.GetQueryStat()
		
		wGetLine = "function cSTRG_DOUNLOADDATA_Unit_Class() {"
		pListSrc.append( wGetLine )
		wGetLine = "  wData = new Array() ;"
		pListSrc.append( wGetLine )
		
		for wLineTap in wRes['Responce']['Data'] :
			wGetTap = []
			for wCel in wLineTap :
				wCel = wCel.strip()
				wGetTap.append( wCel )
			
			wGetLine = "  wData.push( new Array("
			wGetLine = wGetLine + "'" + wGetTap[0] + "', "
			wGetLine = wGetLine + "'" + wGetTap[1] + "', "
			wGetLine = wGetLine + "'" + wGetTap[2] + "', "
			wGetLine = wGetLine + "'" + wGetTap[3] + "'"
			wGetLine = wGetLine + ") ) ;"
			pListSrc.append( wGetLine )
		
		wGetLine = "  return wData ;"
		pListSrc.append( wGetLine )
		wGetLine = "}" + '\n'
		pListSrc.append( wGetLine )
		
		#############################
		# cSTRG_DOUNLOADDATA_Unit_Type
		wQuery = "select * from TBL_UNIT_TYPE;"
		wOBJ_DB.RunQuery( wQuery )
		wRes = wOBJ_DB.GetQueryStat()
		
		wGetLine = "function cSTRG_DOUNLOADDATA_Unit_Type() {"
		pListSrc.append( wGetLine )
		wGetLine = "  wData = new Array() ;"
		pListSrc.append( wGetLine )
		
		for wLineTap in wRes['Responce']['Data'] :
			wGetTap = []
			for wCel in wLineTap :
				wCel = wCel.strip()
				wGetTap.append( wCel )
			
			wGetLine = "  wData.push( new Array("
			wGetLine = wGetLine + "'" + wGetTap[0] + "', "
			wGetLine = wGetLine + "'" + wGetTap[1] + "', "
			wGetLine = wGetLine + "'" + wGetTap[2] + "', "
			wGetLine = wGetLine + "'" + wGetTap[3] + "', "
			wGetLine = wGetLine + "'" + wGetTap[4] + "', "
			wGetTap[5] = wGetTap[5].replace( "'", "\\'" )
			wGetLine = wGetLine + "'" + wGetTap[5] + "'"
			wGetLine = wGetLine + ") ) ;"
			pListSrc.append( wGetLine )
		
		wGetLine = "  return wData ;"
		pListSrc.append( wGetLine )
		wGetLine = "}" + '\n'
		pListSrc.append( wGetLine )
		



		#############################
		# cSTRG_DOUNLOADDATA_Nation
		wQuery = "select * from TBL_NATION;"
		wOBJ_DB.RunQuery( wQuery )
		wRes = wOBJ_DB.GetQueryStat()
		
		wGetLine = "function cSTRG_DOUNLOADDATA_Nation() {"
		pListSrc.append( wGetLine )
		wGetLine = "  wData = new Array() ;"
		pListSrc.append( wGetLine )
		
		for wLineTap in wRes['Responce']['Data'] :
			wGetTap = []
			for wCel in wLineTap :
				wCel = wCel.strip()
				wGetTap.append( wCel )
			
			wGetLine = "  wData.push( new Array("
			wGetLine = wGetLine + "'" + wGetTap[0] + "', "
			wGetLine = wGetLine + "'" + wGetTap[1] + "', "
			wGetTap[2] = wGetTap[2].replace( "'", "\\'" )
			wGetLine = wGetLine + "'" + wGetTap[2] + "'"
			wGetLine = wGetLine + ") ) ;"
			pListSrc.append( wGetLine )
		
		wGetLine = "  return wData ;"
		pListSrc.append( wGetLine )
		wGetLine = "}" + '\n'
		pListSrc.append( wGetLine )
		
		#############################
		# cSTRG_DOUNLOADDATA_Material
		wQuery = "select * from TBL_MATERIAL;"
		wOBJ_DB.RunQuery( wQuery )
		wRes = wOBJ_DB.GetQueryStat()
		
		wGetLine = "function cSTRG_DOUNLOADDATA_Material() {"
		pListSrc.append( wGetLine )
		wGetLine = "  wData = new Array() ;"
		pListSrc.append( wGetLine )
		
		for wLineTap in wRes['Responce']['Data'] :
			wGetTap = []
			for wCel in wLineTap :
				wCel = wCel.strip()
				wGetTap.append( wCel )
			
			wGetLine = "  wData.push( new Array("
			wGetLine = wGetLine + "'" + wGetTap[0] + "', "
			wGetLine = wGetLine + "'" + wGetTap[1] + "', "
			wGetLine = wGetLine + "'" + wGetTap[2] + "'"
			wGetLine = wGetLine + ") ) ;"
			pListSrc.append( wGetLine )
		
		wGetLine = "  return wData ;"
		pListSrc.append( wGetLine )
		wGetLine = "}" + '\n'
		pListSrc.append( wGetLine )
		
		#############################
		# DB Close
		wOBJ_DB.Close()
		return True


