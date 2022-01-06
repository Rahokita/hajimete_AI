# -*- coding: utf-8 -*-
"""
ニューラルネットワークによる人工無脳　ai7.py
使い方　c:\>python ai7.py
"""
# モジュールのインポート
import re
import math

# グローバル変数
INPUTNO = 4       # 入力層のセル数
HIDDENNO = 2      # 中間層のセル数

# 下請け関数の定義
# calcvalue()関数
def calcvalue(textdata):
    """文の特徴量からの評価値の計算"""
    count = [0 for i in range(4)]
    total = 0
    # 字種のカウント
    for chr in textdata:
        # 数え上げ
        chrkind = whatch(chr)
        count[chrkind] += 1
        total += 1
    # 特徴量の計算（字種の割合）
    e = [0.0 for i in range(4)]
    for i in range(4):
        e[i] = count[i]/total
    return forward(e)
# calcvalue()関数の終わり

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

# forward()関数
def forward(e):
    """順方向の計算"""
    # 変数の準備
    wh = [[4.267186249125082, 4.783508618083005, -9.531969382942577,\
           -0.30962291380862067, 0.5323794688254893], \
          [-0.11069226817193417, -1.4069112752484574, 1.6857146161892742, \
            0.011630022697666902, -1.8740302665072108]]
    wo =  [-10.143909160631921, 3.3354095313291645, -1.748717476682627]
    hi = [0.0 for i in range(HIDDENNO + 1)]
    # hiの計算
    for i in range(HIDDENNO):
        u = 0.0
        for j in range(INPUTNO):
            u += e[j] * wh[i][j]
        u -= wh[i][INPUTNO] # しきい値の処理
        hi[i] = f(u)
    # 出力oの計算
    o=0.0
    for i in range(HIDDENNO):
        o += hi[i] * wo[i]
    o -= wo[HIDDENNO] # しきい値の処理
    return f(o)
# forward()関数の終わり

# f()関数
def f(u):
    """伝達関数"""
    # シグモイド関数の計算
    return 1.0/(1.0 + math.exp(-u))
# f()関数の終わり

# メイン実行部
# 入力と応答
print("さくら：さて、どうしました？")
try:
    while True :  # 会話しましょう             
        inputline = input("あなた：")
        value = calcvalue(inputline)
        if value > 0.5:
            print("さくら：それが良いでしょう。")
        else:
            print("さくら：それはやめた方が良いでしょう。")
        print("（おすすめ度:",value,")")
except EOFError:
    print("さくら：それではお話を終わりましょう")

# ai7.pyの終わり
