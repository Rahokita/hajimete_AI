# -*- coding: utf-8 -*-
"""
gens1.pyプログラム
書き換え規則による文の生成プログラムその1
書き換え規則Aに従って文を生成します
  書き換え規則　A
    規則①   <文>→<名詞句＞＜動詞句＞
  　規則②　 <名詞句>→＜名詞＞は
　　規則③　 <動詞句>→＜動詞＞
使い方　c:\>python gens1.py  
"""
# モジュールのインポート
import random

# 下請け関数の定義
# sentence()関数
def sentence():
    """規則①   <文>→<名詞句＞＜動詞句＞"""
    np() # 名詞句の生成
    vp() # 動詞句の生成
# sentence()関数の終わり

# np()関数
def np():
    """規則②　 <名詞句>→＜名詞＞は"""
    print(nlist[random.randint(0, len(nlist) - 1)], end = '')
    print("は", end = '')
# np()関数の終わり

# vp()関数
def vp():
    """規則③　 <動詞句>→＜動詞＞"""
    print(vlist[random.randint(0, len(nlist) - 1)])
# vp()関数の終わり


# メイン実行部
# 名詞リストと動詞リストの設定
nlist = ['私', '彼', '彼女']
vlist = ['歩く', '走る', '泳ぐ' ,'寝る']

# 文の生成
for i in range(50):
    sentence()
 
# gens1.pyの終わり
