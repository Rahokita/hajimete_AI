# -*- coding: utf-8 -*-
"""
しゃべる人工無脳プログラム　ai4.py
このプログラムは、音声で返答する人工無脳です
ただし、返答内容は固定です
返答を記録したwavファイル（fuun.wav,sounano.wav,soukamo.wav,
byebye.wav)が必要です
使い方　c:\>python ai4.py
"""
# モジュールのインポート
import winsound
import random

# 下請け関数の定義
# reply()関数
def reply():
    """人工無脳の返答作成（ランダム）"""
    rndn = random.randint(1, 4)
    if rndn == 1 :   
        print("さくら：ふ～ん，それで？")
        winsound.PlaySound(fuunwavdata, winsound.SND_MEMORY)
    elif rndn == 2 :
        print("さくら：そうなの？")
        winsound.PlaySound(sounanowavdata, winsound.SND_MEMORY)
    else :
        print("さくら：そうかもしれないわね・・・")
        winsound.PlaySound(soukamowavdata, winsound.SND_MEMORY)

# reply()関数の終わり

# メイン実行部
# ファイルからの音声データの読み込み
fuunwavfile = open("fuun.wav", mode = "rb")
fuunwavdata = fuunwavfile.read()
sounanowavfile = open("sounano.wav", mode = "rb")
sounanowavdata = sounanowavfile.read()
soukamowavfile = open("soukamo.wav", mode = "rb")
soukamowavdata = soukamowavfile.read()
byebyewavfile = open("byebye.wav", mode = "rb")
byebyewavdata = byebyewavfile.read()

# 入力と応答
print("さくら：メッセージをどうぞ")
try:
    while True :  # 会話しましょう             
        inputline = input("あなた：")
        reply()   # 人工無脳の返答
except EOFError:
    print("さくら：ばいば～い")
    winsound.PlaySound(byebyewavdata, winsound.SND_MEMORY)

# ai4.pyの終わり
