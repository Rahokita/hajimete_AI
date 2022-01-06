# -*- coding: utf-8 -*-
"""
playmem.pyプログラム
winsoundモジュールを利用して、wavファイルを再生します
使い方　c:\>python playmem.py
"""
# モジュールのインポート
import winsound

# メイン実行部
filename = input("ファイル名を入力：")
wavfile = open(filename + ".wav", mode = "rb")
wavdata = wavfile.read()
winsound.PlaySound(wavdata, winsound.SND_MEMORY)
 
# playmem.pyの終わり
