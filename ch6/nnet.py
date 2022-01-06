# -*- coding: utf-8 -*-
"""
nnet.pyプログラム
単純なニューラルネットワークの計算
三つの神経細胞からなるニューラルネットワークです  
使い方　c:\>python nnet.py
"""
# モジュールのインポート
import math

# グローバル変数
INPUTNO = 2       # 入力数
HIDDENNO = 2      # 中間層の神経細胞の数

# 下請け関数の定義
# forward()関数
def forward(wh,wo,hi,e):
    """順方向の計算"""
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
    #ステップ関数の計算
    if u >= 0:
        return 1.0
    else:
        return 0.0
# f()関数の終わり

# メイン実行部
wh = [[1,-1,0.5],[-1,1,0.5]]            # 中間層の結合荷重
wo = [1,1,0.5]                          # 出力層の結合荷重
hi = [0 for i in range(HIDDENNO + 1)]   # 中間層の出力
e = [0.0 for i in range(INPUTNO)]       # 入力データ

# 計算の本体
try:
    while True:
        e[0]  = float(input("x1:"))
        e[1]  = float(input("x2:")) 
        print(e,"->",forward(wh,wo,hi,e))
except EOFError:
    print("計算を終わります")

# nnet.pyの終わり
