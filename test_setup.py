#!/usr/bin/python
# coding: UTF-8
#####################################################
# ::Project  : Galaxy Fleet
# ::Admin    : Korei (@korei-xlix)
# ::github   : https://github.com/korei-xlix/galaxyfleet/
# ::Class    : テストプログラム
#####################################################

#print("Script Text :: OK")


def Func_Test1(
		inX = 1111,
		inY = 2222,
		inZ = 3333
	):
	
	print("OK")
	return

def Func_Test(
		inX = 9999,
		inY = 7777
	):
	
	print(str( inX ))	# 5
	Func_Test1(
		inX=3,
		inY=6666,
		inZ=7777
	)
	print(str( inX ))	# 5
	return



Func_Test( inY=7, inX=5 );



