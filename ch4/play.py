# -*- coding: utf-8 -*-
"""
play.pyプログラム
winsoundモジュールを利用して、wavファイルを再生します
使い方　c:\>python play.py
"""
# モジュールのインポート
import winsound
# メイン実行部
filename = input("ファイル名を入力：")
winsound.PlaySound(filename + ".wav",winsound.SND_FILENAME)
 
# play.pyの終わり
