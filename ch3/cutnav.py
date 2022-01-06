# -*- coding: utf-8 -*-
"""
cutnav.pyプログラム
字種に基づく名詞・形容詞・動詞・形容動詞の切り出し
使い方　c:\>python cutnav.py < (日本語テキストデータ） 
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

# 品詞の切り出し
chartype = 3 # 字種の初期設定
i = 0
while i < len(inputtext) :
    if re.match('[。．、，]', inputtext[i]):
        pass
    elif whatch(inputtext[i]) != 2: # 漢字以外
        pass
    else: # 漢字
        while(whatch(inputtext[i]) == 2):
            print(inputtext[i],end = '')
            i += 1
        if inputtext[i] == 'い':   # 形容詞
            print(inputtext[i],end = '')
            print(" : 形容詞")
        elif inputtext[i] == 'う': # 動詞
            print(inputtext[i],end = '')
            print(" : 動詞")
        elif inputtext[i] == 'だ': # 形容動詞
            print(inputtext[i],end = '')
            print(" : 形容動詞")
        else :                     # 名詞
            print(" : 名詞")
    i += 1
    
# cutnav.pyの終わり
