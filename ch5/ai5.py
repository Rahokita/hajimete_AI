# -*- coding: utf-8 -*-
"""
プロダクションルールを用いた人工無能　ai5.py
使い方　c:\>python ai5.py
"""
# モジュールのインポート
import random

# 下請け関数の定義
# answer()関数
def answer(inputline, prule):
    """ 応答文の生成 """
    #  マッチするルールの個数を調べる
    no = 0
    for singlep in prule:
        if rulematch(inputline, singlep):
            no += 1
    if no == 0: # マッチするルールがない
        print("さくら： どうぞ続けてください")
    else: # 少なくとも１つはマッチするルールがある
        limit = random.randint(0, no - 1)
        no = 0
        for singlep in prule:
            if rulematch(inputline, singlep):
                if no == limit:
                    print("さくら：",singlep[4])
                    break
                no += 1
        
# answer()関数の終わり

# rulematch()関数
def rulematch(inputline, singlep):
    """ 入力にマッチするルールを探す """
    count = 0
    for i in range(4):
        if singlep[i] == "":
            count += 1
        elif singlep[i] in inputline:
            count += 1
    if count ==4:
        return True
    else:
        return False
# rulematch()関数の終わり

# メイン実行部
# プロダクションルールの設定
prule = [["先生","","","","私のことでなくあなたのことを話しましょう"],
         ["母","","","","お母さんが気がかりですか"],
         ["私","","","","どうぞあなたのことを聞かせてください"],
         ["先生","私","","","どうしてそう聞くのですか"],
         ["昨日","私","","","なるほど，それでどうしましたか"],
         ["東京","福井","","","どちらが良いと思いますか"],
         ["先生","相談","","","相談の内容はどんなことでしょう"],
        ]

# 入力と応答
print("さくら：さて、どうしました？")
try:
    while True :  # 会話しましょう             
        inputline = input("あなた：")
        answer(inputline, prule) # プロダクションルールによる応答文生成
except EOFError:
    print("さくら：それではお話を終わりましょう")

# ai5.pyの終わり
