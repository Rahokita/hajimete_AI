# -*- coding: utf-8 -*-
"""
readwavprop.pyプログラム
任意のWAVEファイルを読み込んで属性を出力します
使い方　c:\>python readwavprop.py 
"""
# モジュールのインポート
import wave
# メイン実行部
# ファイルオープン
filename = input("ファイル名を入力：")
w = wave.open(filename + ".wav", mode = 'rb')

# 属性の出力
print("オーディオチャンネル数：", w.getnchannels())
print("サンプルサイズ　　　　：", w.getsampwidth())
print("サンプリングレート　　：", w.getframerate()) 
print("オーディオフレーム数　：", w.getnframes())

# readwavprop.pyの終わり
