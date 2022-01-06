# -*- coding: utf-8 -*-
"""
cutmorph.pyプログラム
正規表現を利用した簡易的な形態素分離プログラム
使い方　c:\>python cutmorph.py < (日本語テキストデータ） 
"""
# モジュールのインポート
import sys
import re

# 下請け関数の定義
# whatch()関数
def whatch(ch):
    """字種の判定"""
    if re.match('[ぁ-ん]' , ch):  #　ひらがな
        chartype = 0
    elif re.match('[ァ-ン]' , ch):#　カタカナ
        chartype = 1
    elif re.match('[一-龥]' , ch):#　漢字
        chartype = 2
    else :                        #　それ以外
        chartype = 3
    return chartype
# whatch()関数の終わり

# メイン実行部
# 解析対象文字列の読み込み
inputtext = sys.stdin.read()

# 分かち書き文の生成
for i in range(len(inputtext) - 1):
    if re.match('[。．、，]', inputtext[i]):
        continue
    print(inputtext[i], end = "")
    if whatch(inputtext[i]) != whatch(inputtext[i + 1]):
        print() 
# cutmorph.pyの終わり
