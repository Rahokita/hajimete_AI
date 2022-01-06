# -*- coding: utf-8 -*-
"""
and.pyプログラム
単体の人工神経細胞の計算
論理積（AND）と同等の計算をする神経細胞です  
使い方　c:\>python and.py
"""
# モジュールのインポート
import math

# グローバル変数
INPUTNO = 2       # 入力数

# 下請け関数の定義
# forward()関数
def forward(w,e):
    """順方向の計算"""
    #計算の本体
    u = 0.0
    for i in range(INPUTNO):
        u += e[i] * w[i]
    u -= w[INPUTNO] # しきい値の処理
    # 出力値の計算
    o = f(u)
    return o
# forward()関数の終わり

# f()関数
def f(u):
    """伝達関数"""
    # ステップ関数の計算
    if u >= 0:
        return 1.0
    else:
        return 0.0
# f()関数の終わり

# メイン実行部
w = [1.0,1.0,1.5]        # 重みとしきい値(論理積の計算)
e = [0.0 for i in range(INPUTNO)] # 入力データ
# 計算の本体
try:
    while True:
        e[0]  = float(input("x1:"))
        e[1]  = float(input("x2:")) 
        print(e,"->",forward(w,e))
except EOFError:
    print("計算を終わります")

# and.pyの終わり
