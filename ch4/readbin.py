# -*- coding: utf-8 -*-
"""
readbin.pyプログラム
バイナリファイルを読み込んで画面に値を出力します
使い方　c:\>python readbin.py 
"""
# モジュールのインポート

# メイン実行部
# ファイルの読み込み
filename = input("ファイル名を入力：")
bfile = open(filename + ".wav", mode = 'rb')
binarydata = bfile.read()

# 画面出力
for ch in binarydata:
    print(ch, end = '')
    if(ch >= 32) & (ch <= 127):# 英数記号の範囲
        print('\t', chr(ch), end = '')
    print()

# readbin.pyの終わり
