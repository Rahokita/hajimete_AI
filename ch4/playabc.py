# -*- coding: utf-8 -*-
"""
playabc.pyプログラム
winsoundモジュールを利用して、a.wav,b.wav,およびc.wavという
３つのwavファイルに格納された音声を10回繰り返して読み上げます
使い方　c:\>python playabc.py
"""
# モジュールのインポート
import winsound

# メイン実行部
# ファイルからの音声データの読み込み
awavfile = open("a.wav", mode = "rb")
awavdata = awavfile.read()
bwavfile = open("b.wav", mode = "rb")
bwavdata = bwavfile.read()
cwavfile = open("c.wav", mode = "rb")
cwavdata = cwavfile.read()
# 音声の読み上げ
for i in range(10):
    winsound.PlaySound(awavdata, winsound.SND_MEMORY)
    winsound.PlaySound(bwavdata, winsound.SND_MEMORY)
    winsound.PlaySound(cwavdata, winsound.SND_MEMORY)
 
# playabc.pyの終わり
