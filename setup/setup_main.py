#!/usr/bin/python
# coding: UTF-8
#####################################################
# ::Project  : Galaxy Fleet
# ::Admin    : Korei (@korei-xlix)
# ::github   : https://github.com/korei-xlix/galaxyfleet/
# ::Class    : セットアップ
#####################################################

from filectrl import CLS_File
from osif import CLS_OSIF

#####################################################
class CLS_SetupMain() :

#####################################################
# セットアップ
#####################################################
	@classmethod
	def sSetup(cls):
		#############################
		# 応答形式の取得
		#   "Result" : False, "Class" : None, "Func" : None, "Reason" : None, "Responce" : None
		wRes = CLS_OSIF.sGet_Resp()
		wRes['Class'] = "CLS_Setup"
		wRes['Func']  = "Init"
		
		#############################
		# webサイトソースのカレントパス取得
		wCHR_Path = CLS_File.sGetCurrentPath()
		wCHR_Path = wCHR_Path + "/"
		wStr = "current folder: " + wCHR_Path
		CLS_OSIF.sPrn(wStr)
		
		wCHR_SrcPath = wCHR_Path + "galaxyfleet_data/nginx/https_gyft.conf"
		wCHR_DstPath = "/var/galaxyfleet/" + "galaxyfleet_data/nginx/https_gyft.conf"
		wCHR_WebPath   = wCHR_Path + "galaxyfleet_web/"
		wCHR_uwsgiPath = wCHR_Path + "galaxyfleet_uwsgi/"
		
		wSTR_Strings = {
			"[@ROOT-WEB-PATH@]"		:	wCHR_WebPath,
			"[@ROOT-UWSGI-PATH@]"	:	wCHR_uwsgiPath
		}
		#############################
		# nginx configのパス書き換え
		if CLS_File.sChangeWriteFile( inSrcPath=wCHR_SrcPath, inDstPath=wCHR_DstPath, inSTR_Strings=wSTR_Strings )!=True :
			wRes['Reason'] = "failer write config: dstpath=" + wCHR_DstPath
			CLS_OSIF.sErr( wRes )
			return wRes
		
		#############################
		# 状況表示
		wStr = "complete write config" + '\n'
		wStr = wStr + "  src path  = " + wCHR_SrcPath + '\n'
		wStr = wStr + "  dst path  = " + wCHR_DstPath + '\n'
		wStr = wStr + "  root path = " + wCHR_Path
		CLS_OSIF.sPrn(wStr)
		
		#############################
		# 正常
		wRes['Result']  = True
		return wRes



