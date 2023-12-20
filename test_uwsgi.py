#!/usr/bin/python
# coding: UTF-8
#####################################################
# ::Project  : Galaxy Fleet
# ::Admin    : Korei (@korei-xlix)
# ::github   : https://github.com/korei-xlix/galaxyfleet/
# ::Class    : テストプログラム
#####################################################

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]



