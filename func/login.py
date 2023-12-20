#!/usr/bin/python
# coding: UTF-8
#####################################################
# Star Region
#   Class   ：
#   Site URL：https://mynoghra.jp/
#   Update  ：2019/6/28
#####################################################

##from postgresql_use import CLS_PostgreSQL_Use
from admin import CLS_Admin
from gval import gVal
#####################################################
class CLS_Login() :
#####################################################
	@classmethod
	def sRun( cls, inParam, outSrcFile ):
		pSrcFile = outSrcFile
		if len(inParam)!=4 :
			gVal.STR_ScriptResp['Reason'] = "CLS_Login: Missing parameter"
			return False
		
		#############################
		# 
		wOBJ_Admin = CLS_Admin()
		if wOBJ_Admin.Confirm( gVal.STR_File['AdminInfo_File'], inParam[2], inParam[3] )!=True :
			gVal.STR_ScriptResp['Reason'] = "CLS_Login: " + wOBJ_Admin.STR_Login['Reason']
			
			wSen = '<script src=\"' + gVal.DEF_SENARIO_PATH + 'login_ng' + '.js\"></script>'
			pSrcFile.append( wSen )
			return False
		
		wSen = '<script src=\"' + gVal.DEF_SENARIO_PATH + 'login_ok' + '.js\"></script>'
		pSrcFile.append( wSen )
		
		return True


