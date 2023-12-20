#!/usr/bin/python
# coding: UTF-8
#####################################################
# ::Project  : Galaxy Fleet
# ::Admin    : Korei (@korei-xlix)
# ::github   : https://github.com/korei-xlix/galaxyfleet/
# ::Class    : セットアップ
#####################################################
import sys
###sys.path.append('admin')
###sys.path.append('api')
###sys.path.append('data')
###sys.path.append('func')
sys.path.append('galaxyfleet_uwsgi/oslib')
sys.path.append('galaxyfleet_uwsgi/setup')

from setup_main import CLS_SetupMain
from setup_db import CLS_SetupDB

#####################################################
# main
#####################################################
def MainRun():
	
	#############################
	# 引数取得
	wArg = CLS_OSIF.sGetArg()
	
	#############################
	# メインセットアップ
	if wArg[1]!="main" :
		CLS_SetupMain.sSetup()
	
	#############################
	# DBセットアップ
	elif wArg[1]!="db" :
		CLS_SetupDB.sSetup()



#####################################################
# Main
#####################################################
###
###CLS_SetupMain.sSetup()
###
#
