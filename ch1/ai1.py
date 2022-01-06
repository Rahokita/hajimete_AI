# -*- coding: utf-8 -*-
"""
初めての人工無脳プログラム ai1.py
このプログラムは、常に決まった返答を返す人工無脳です
本当に無能ですね
使い方　c:\>python ai1.py
"""

# メイン実行部
print("さくら：メッセージをどうぞ")
try:
    while True :  # 会話しましょう             
        inputline = input("あなた：")
        print("さくら：ふ～ん、それで？")
except EOFError:
    print("さくら：ばいば～い")

# ai1.pyの終わり
