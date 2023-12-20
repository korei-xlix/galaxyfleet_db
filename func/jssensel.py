#!/usr/bin/python
# coding: UTF-8
#####################################################
# Star Region
#   Class   ：JSシナリオセレクター
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


from gval import gVal
#####################################################
class CLS_JSSenSel() :
#####################################################
	@classmethod
	def sSel( cls, inParam, outSrcFile ):
		pSrcFile = outSrcFile
		if len(inParam)!=3 :
			gVal.STR_ScriptResp['Reason'] = "CLS_JSSenSel: Missing parameter"
			return False
		
		#############################
		# シナリオ番号の取り出し
		wSenNumber = inParam[2].split(",")
		for wLine in wSenNumber :
			wSen = '<script src=\"' + gVal.DEF_SENARIO_PATH + wLine + '.js\"></script>'
			pSrcFile.append( wSen )
			
##			#############################
##			# 無いシナリオ
##			else :
##				gVal.STR_ScriptResp['Reason'] = "CLS_JSSenSel: There is no scenario included"
##				return False
		
		return True



