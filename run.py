#!/usr/bin/python
# coding: UTF-8
#####################################################
# Star Region
#   Class   ：実行メイン処理
#   Site URL：https://mynoghra.jp/
#   Update  ：2019/6/28
#####################################################
# systemctl restart uwsgi
#
#####################################################
# req：
# 
#####################################################
import sys
sys.path.append('admin')
sys.path.append('api')
sys.path.append('data')
sys.path.append('func')
sys.path.append('oslib')

from outhtml import CLS_OutHTML
from jssensel import CLS_JSSenSel
from login import CLS_Login
#from download import CLS_Download
from gval import gVal
#####################################################
# run.py実行
# ※ここが最初に起動してHTMLを返送する
#####################################################
def application( env, start_response ):
	start_response('200 OK', [('Content-Type','text/html')])
######## sample
#	return b'<html><body>Hello, world. 2.</body></html>'
#	return [ 'Hello, World'.encode('utf-8') ]
#	method = env.get('REQUEST_METHOD')
#	print( method )
########
	
	#############################
	# リクエストの取得
##	gVal.STR_ScriptResp['Request'] = CLS_OSIF.sGetArg()
##	gVal.STR_ScriptResp['Request'] = env.get('REQUEST_METHOD')
##	gVal.STR_ScriptResp['Request'] = env
##	gVal.STR_ScriptResp['Request'] = env['REQUEST_URI']
	if env['HTTPS']=='on' :
		wURI = "https://"
	else:
		wURI = "http://"
	
	wURI = wURI + env['SERVER_NAME'] + env['REQUEST_URI']
	gVal.STR_ScriptResp['Request'] = wURI
	
	wListSrc = []
	wSrcPath = []
	#############################
	# パラメータ部分の取得
	wParam = wURI.split("?")
	if len(wParam)!=2 :
		gVal.STR_ScriptResp['Reason'] = "Parameter is not found"
		wCHR_html = CLS_OutHTML.sOutHTML5( gVal.STR_ScriptResp, wListSrc, wSrcPath )
		return wCHR_html
	
	#############################
	# パラメータごとに分解
	wParam = wParam[1].split("&")
	if len(wParam)<2 :
		gVal.STR_ScriptResp['Reason'] = "Missing parameter"
		wCHR_html = CLS_OutHTML.sOutHTML5( gVal.STR_ScriptResp, wListSrc, wSrcPath )
		return wCHR_html
	
	#############################
	# パスの判定
	if wParam[0]!=gVal.DEF_REQ_PASS :
		gVal.STR_ScriptResp['Reason'] = "Invalid request"
		wCHR_html = CLS_OutHTML.sOutHTML5( gVal.STR_ScriptResp, wListSrc, wSrcPath )
		return wCHR_html
	
	#############################
	# リクエストの取り出し
	wReq = wParam[1].split("=")
	if len(wReq)!=2 :
		gVal.STR_ScriptResp['Reason'] = "Request header missing"
		wCHR_html = CLS_OutHTML.sOutHTML5( gVal.STR_ScriptResp, wListSrc, wSrcPath )
		return wCHR_html
	if wReq[0]!="req" :
		gVal.STR_ScriptResp['Reason'] = "Request header is not found"
		wCHR_html = CLS_OutHTML.sOutHTML5( gVal.STR_ScriptResp, wListSrc, wSrcPath )
		return wCHR_html
	
	#############################
	# 応答通知用スクリプト
	wSrcPath.append('<script src=\"' + gVal.DEF_LOADER_JSSCRIPT_PATH + '\"></script>')
	
	#############################
	# 要求された処理の呼び出し
	
	#############################
	# JavaScriptシナリオ要求
	if wReq[1]==gVal.DEF_STRG_REQ_JSSENARIO :
		if CLS_JSSenSel.sSel( wParam, wSrcPath )!=True :
			wCHR_html = CLS_OutHTML.sOutHTML5( gVal.STR_ScriptResp, wListSrc, wSrcPath )
			return wCHR_html
	
	#############################
	# ログイン要求
	elif wReq[1]==gVal.DEF_STRG_REQ_LOGIN :
		if CLS_Login.sRun( wParam, wSrcPath )!=True :
			wCHR_html = CLS_OutHTML.sOutHTML5( gVal.STR_ScriptResp, wListSrc, wSrcPath )
			return wCHR_html
	
	#############################
	# 基本データ要求
	elif wReq[1]==gVal.DEF_STRG_REQ_BASEDATA_DL :
		if CLS_Download.sBaseData( wParam, wListSrc )!=True :
			wCHR_html = CLS_OutHTML.sOutHTML5( gVal.STR_ScriptResp, wListSrc, wSrcPath )
			return wCHR_html
	
	#############################
	# 不明な要求
	else :
		gVal.STR_ScriptResp['Reason'] = "Unknown request"
		wCHR_html = CLS_OutHTML.sOutHTML5( gVal.STR_ScriptResp, wListSrc, wSrcPath )
		return wCHR_html
	
	#############################
	# 出力
	gVal.STR_ScriptResp['Result'] = True
	wCHR_html = CLS_OutHTML.sOutHTML5( gVal.STR_ScriptResp, wListSrc, wSrcPath )
	return wCHR_html



