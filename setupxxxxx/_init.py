#!/usr/bin/python
# coding: UTF-8
#####################################################
# Star Region
#   Class   ：init実行
#   Site URL：https://mynoghra.jp/
#   Update  ：2019/6/27
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
# コマンド：
#  python3 _init.py setup  ...DB情報セットアップ＆テーブル初期化
#  python3 _init.py init   ...テーブル初期化のみ
#####################################################
import sys
sys.path.append('admin')
sys.path.append('api')
sys.path.append('data')
sys.path.append('setup')
sys.path.append('oslib')

from setup import CLS_Setup
from gval import gVal
#####################################################
CLS_Setup.sRun()	#起動


