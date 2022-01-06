# -*- coding: utf-8 -*-
"""
gens2.pyプログラム
書き換え規則による文の生成プログラムその2
書き換え規則Bに従って文を生成します
  書き換え規則B
      規則①	<文>→<名詞句＞＜動詞句＞
　　　規則②	<名詞句>→＜形容詞句＞＜名詞＞は
　　　規則③	<名詞句>→＜名詞＞は
　　　規則④	<動詞句>→＜動詞＞
　　　規則⑤	<動詞句>→＜形容詞＞
　　　規則⑥	<動詞句>→＜形容動詞＞
　　　規則⑦	<形容詞句>→＜形容詞＞＜形容詞句＞
　　　規則⑧	<形容詞句>→＜形容詞＞
使い方　c:\>python gens2.py  
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
    """
      規則②　<名詞句>→＜形容詞句＞＜名詞＞は　
      規則③　<名詞句>→＜名詞＞は
    """
    if(random.randint(0, 1) > 0):
        ap()
    print(nlist[random.randint(0, len(nlist) - 1)], end = '')
    print("は", end = '')
# np()関数の終わり

# vp()関数
def vp():
    """
　　　規則④	<動詞句>→＜動詞＞
　　　規則⑤	<動詞句>→＜形容詞＞
　　　規則⑥	<動詞句>→＜形容動詞＞
    """
    rndn = random.randint(4, 6)
    if rndn == 4 :   # 規則４
        print(vlist[random.randint(0, len(vlist) - 1)], end = '')
    elif rndn == 5 : # 規則５
        print(alist[random.randint(0, len(alist) - 1)], end = '')
    else :           # 規則６
        print(dlist[random.randint(0, len(dlist) - 1)], end = '')    
# vp()関数の終わり

# ap()関数
def ap():
    """
　　　規則⑦	<形容詞句>→＜形容詞＞＜形容詞句＞
　　　規則⑧	<形容詞句>→＜形容詞＞
    """
    print(alist[random.randint(0, len(alist) - 1)], end = '')
    if(random.randint(0, 1) > 0):      
        ap()    
# ap()関数の終わり

# メイン実行部
# 名詞リストと動詞リストの設定
nlist = ['私', '彼', '彼女']
vlist = ['歩く', '走る', '泳ぐ' ,'寝る']
alist = ['赤い', '青い']
dlist = ['静かだ', '暖かだ']

# 文の生成
for i in range(50):
    sentence()
    print()
 
# gens2.pyの終わり
