# -*- coding: utf-8 -*-
"""
backprop41.pyプログラム
4入力1出力版のbackprop.pyプログラムです
バックプロパゲーションによるニューラルネットワークの学習  
誤差の推移や、学習結果となる結合荷重などを出力します
使い方　c:\>python backprop41.py < data.txt
"""
# モジュールのインポート
import math
import sys
import random

# グローバル変数
INPUTNO = 4       # 入力層のセル数
HIDDENNO = 2      # 中間層のセル数
ALPHA = 3         # 学習係数
MAXINPUTNO = 100  # データの最大個数
BIGNUM = 100.0    # 誤差の初期値
ERRLIMIT = 0.01  # 誤差の上限値
SEED = 65535      # 乱数のシード

# 下請け関数の定義
# getdata()関数
def getdata(e):
    """学習データの読み込み"""
    n = 0   # データセットの個数
    # データの入力
    for line in sys.stdin : 
        e[n] = [float(num) for num in line.split()]
        n += 1
    return n 
# getdata()関数の終わり

# forward()関数
def forward(wh,wo,hi,e):
    """順方向の計算"""
    #hiの計算
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

# olearn()関数
def olearn(wo,hi,e,o):
    """出力層の重み学習"""
    # 誤差の計算
    error = (e[INPUTNO] - o) * o * (1 - o)
    # 重みの学習
    for i in range(HIDDENNO):
        wo[i] += ALPHA * hi[i] * error
    # しきい値の学習
    wo[HIDDENNO] += ALPHA * (-1.0) * error
    return 
# olearn()関数の終わり

# hlearn()関数
def hlearn(wh,wo,hi,e,o):
    """中間層の重み学習"""
    # 中間層の各セルjを対象
    for j in range(HIDDENNO):
        errorj = hi[j] * (1 - hi[j]) \
                 * wo[j] * (e[INPUTNO] - o) * o * (1 - o)
        # i番目の重みを処理
        for i in range(INPUTNO):
            wh[j][i] += ALPHA * e[i] * errorj
        # しきい値の学習
        wh[j][INPUTNO] += ALPHA * (-1.0) * errorj
    return 
# hlearn()関数の終わり

# メイン実行部
# 乱数の初期化
random.seed(SEED)

# 変数の準備
wh = [[random.uniform(-1,1) for i in range(INPUTNO + 1)]
       for j in range(HIDDENNO)]        # 中間層の重み
wo = [random.uniform(-1,1)
      for i in range(HIDDENNO + 1)]     # 出力層の重み
e = [[0.0 for i in range(INPUTNO + 1)] 
      for j in range(MAXINPUTNO)]       # 学習データセット
hi = [0 for i in range(HIDDENNO + 1)]   # 中間層の出力
totalerr = BIGNUM                       # 誤差の評価

# 結合荷重の初期値の出力
print(wh,wo)

# 学習データの読み込み
n = getdata(e)
print("学習データの個数:",n)

# 学習
count = 0
while totalerr > ERRLIMIT :
    totalerr = 0.0
    for j in range(n):
        # 順方向の計算
        output = forward(wh,wo,hi,e[j])
        # 出力層の重みの調整
        olearn(wo,hi,e[j],output)
        # 中間層の重みの調整
        hlearn(wh,wo,hi,e[j],output)
        # 誤差の積算
        totalerr += (output - e[j][INPUTNO]) * (output - e[j][INPUTNO]) 
    count += 1
    # 誤差の出力
    print(count," ",totalerr)
# 結合荷重の出力
print(wh,wo)

# 学習データに対する出力 
for i in range(n):
    print(i,":",e[i],"->",forward(wh,wo,hi,e[i]))

# backprop41.pyの終わり
