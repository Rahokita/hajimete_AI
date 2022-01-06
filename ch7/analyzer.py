# -*- coding: utf-8 -*-
"""
analyzer.py
入力文の字種の割合により文の特徴量を作成します
4次元の特徴量ベクトルと、教師データを出力します
使い方　c:\>python analyzer.py < text.txt > data.txt
"""
# モジュールのインポート
import sys
import re

# 下請け関数の定義
# anastate()関数
def anastate(listdata):
    """文の特徴量の生成"""
    count = [0 for i in range(4)]
    total = 0
    # 字種のカウント
    for chr in listdata[0]:
        # 数え上げ
        chrkind = whatch(chr)
        count[chrkind] += 1
        total += 1
    # 特徴量出力（字種の割合と教師信号）
    for i in range(4):
        print(count[i]/total, ' ', end = '')
    print(listdata[1])
# anastate()関数の終わり

# whatch()関数
def whatch(ch):
    """字種の判定"""
    if re.match('[ぁ-ん]' , ch):  # ひらがな
        chartype = 0
    elif re.match('[ァ-ン]' , ch):# カタカナ
        chartype = 1
    elif re.match('[一-龥]' , ch):# 漢字
        chartype = 2
    else :                        # それ以外
        chartype = 3
    return chartype
# whatch()関数の終わり

# メイン実行部
# 読み込みと特徴量の計算
try:
    while True :  # 標準入力からの読み込み             
        inputline = input()
        inputlist = inputline.split()
        anastate(inputlist)
except EOFError:
    pass

# analyzer.pyの終わり
