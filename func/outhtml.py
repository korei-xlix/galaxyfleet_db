#!/usr/bin/python
# coding: UTF-8
#####################################################
# Star Region
#   Class   ：HTML出力
#   Site URL：https://mynoghra.jp/
#   Update  ：2019/6/10
#####################################################
# Private Function:
#   (none)
#
# Instance Function:
#   (none)
#
# Class Function(static):
#   (none)
#
#####################################################


#####################################################
class CLS_OutHTML() :
#####################################################

#####################################################
# HTML作成
#####################################################
	@classmethod
	def sOutHTML5( cls, inParam, inListSrc=[], inSrcFile=[] ):
		wHTML = []
		#############################
		# HTMLヘッダ
		wHTML.append('<!DOCTYPE html>')
		wHTML.append('<html lang=\"ja\"><head>')
		wHTML.append('<meta charset=\"utf-8\">')
		wHTML.append('<meta name=\"author\" content=\"Lucida\">')
		wHTML.append('<meta name=\"robots\" content=\"noindex,nofollow\">')
		wHTML.append('<title>Star Region</title>')
##		wHTML.append('<script src=\"' + gVal.DEF_LOADER_JSSCRIPT_PATH + '\"></script>')
		
		#############################
		# JavaScriptソースファイルを挟む
		for wLine in inSrcFile :
			wHTML.append( wLine )
		
		#############################
		# JavaScriptソースを挟む
		wHTML.append('<script>')
		wHTML.append('<!--')

		wHTML.append('var cSTR_STRG_RUN_Result = {')
##		wHTML.append('    Request : \"' + str(inParam['Request']) + '\", ')
		
		if inParam['Result']==True :
			wHTML.append('    Result  : true, ')
		else :
			wHTML.append('    Result  : false, ')
		
		wHTML.append('    Reason  : \"' + inParam['Reason'] + '\" } ;')
##		wHTML.append('    Reason  : \"' + inParam['Reason'] + '\", ')
##		wHTML.append('    Loaded  : false };')
##		wHTML.append('function _hdl_Loaded() {')
##		wHTML.append('   cSTR_STRG_RUN_Result.Loaded = true ;')
##		wHTML.append('}')

		for wLine in inListSrc :
			wHTML.append( wLine )
		
		wHTML.append('//-->')
		wHTML.append('</script>')
		
		#############################
		# HTMLヘッダ閉じ + BODY
		wHTML.append('</head><body onload=\"_hdl_PageLoad()\">')
		
		#############################
		# パラメータ
##		wHTML.append('Request:<br>')
##		wHTML.append( str(inParam['Request']) + '<br>')
##		wHTML.append('<br>')
		
		wHTML.append('Result:<br>')
		wHTML.append( str(inParam['Result']) + '<br>')
		wHTML.append('<br>')
		
		wHTML.append('Reason:<br>')
		wHTML.append( inParam['Reason'] + '<br>')
		wHTML.append('<br>')
		
		#############################
		# HTMLフッタ
		wHTML.append('</body></html>')
		
		#############################
		# 改行の付加
		wOutHTML = []
		for wLine in wHTML :
			wOutHTML.append( wLine + '\n' )
		
		return wOutHTML



