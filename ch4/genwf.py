# -*- coding: utf-8 -*-
"""
genwf.pyプログラム
	天気予報を”しゃべる”プログラム
	書き換え規則Ｃに従って天気予報を生成します
    書き換え規則Ｃ
	規則①	<文>→<地区＞＜時間帯＞＜天気＞
    規則②	<地区>→東京地方
    規則③	<地区>→福井県
    規則④	<時間帯>→今日は
    規則⑤	<時間帯>→明日は
    規則⑥	<天気>→＜天気＞ところにより＜天気＞
    規則⑦	<天気>→晴れ
    規則⑧	<天気>→曇り
    規則⑨	<天気>→雨
    実行には，テキスト形式で音声データを格納した、
    以下の8つのwavファイルが必要です．
    toukyouchihou.wav fukuiken.wav
    kyouha.wav asuha.wav
    hare.wav kumori.wav ame.wav
    tokoroniyori.wav
使い方　c:\>python genwf.py  
"""

# モジュールのインポート
import random
import winsound

# 下請け関数の定義
# sentence()関数
def sentence():
    """規則①   <文>→→<地区＞＜時間帯＞＜天気＞"""
    region()    # 地区の生成
    timezone()  # 時間帯の生成
    weather()   # 天気の生成
# sentence()関数の終わり

# region()関数
def region():
    """
      規則② <地区>→東京地方　
      規則③ <地区>→福井県
    """
    if(random.randint(0, 1) > 0):# 規則②
        winsound.PlaySound(toukyouwavdata, winsound.SND_MEMORY)
        print("東京地方", end = '')
    else: # 規則③
        winsound.PlaySound(fukuiwavdata, winsound.SND_MEMORY)
        print("福井県", end = '')

# region()関数の終わり

# timezone()関数
def timezone():
    """
      規則④	<時間帯>→今日は
      規則⑤	<時間帯>→明日は
    """
    if(random.randint(0, 1) > 0):# 規則④
        winsound.PlaySound(kyouhawavdata, winsound.SND_MEMORY)
        print("今日は", end = '')
    else: # 規則⑤
        winsound.PlaySound(asuhawavdata, winsound.SND_MEMORY)
        print("明日は", end = '')

# timezone()関数の終わり

# weather()関数
def weather():
    """
      規則⑥	<天気>→＜天気＞ところにより＜天気＞
      規則⑦	<天気>→晴れ 
      規則⑧	<天気>→曇り  
      規則⑨	<天気>→雨
    """
    rndn = random.randint(6, 9)
    if rndn == 6 :   # 規則⑥
        weather()
        winsound.PlaySound(tokorowavdata, winsound.SND_MEMORY)
        print("ところにより", end = '')
        weather()
    elif rndn == 7 : # 規則⑦
        winsound.PlaySound(harewavdata, winsound.SND_MEMORY)
        print("晴れ", end = '')
    elif rndn == 8 : # 規則⑧
        winsound.PlaySound(kumoriwavdata, winsound.SND_MEMORY)
        print("曇り", end = '')
    elif rndn == 9 : # 規則⑨
        winsound.PlaySound(amewavdata, winsound.SND_MEMORY)
        print("雨", end = '')
 
# weather()関数の終わり

# メイン実行部
# ファイルからの音声データの読み込み
toukyouwavfile = open("toukyouchihou.wav", mode = "rb")
toukyouwavdata = toukyouwavfile.read()
fukuiwavfile = open("fukuiken.wav", mode = "rb")
fukuiwavdata = fukuiwavfile.read()
kyouhawavfile = open("kyouha.wav", mode = "rb")
kyouhawavdata = kyouhawavfile.read()
asuhawavfile = open("asuha.wav", mode = "rb")
asuhawavdata = asuhawavfile.read()
harewavfile = open("hare.wav", mode = "rb")
harewavdata = harewavfile.read()
kumoriwavfile = open("kumori.wav", mode = "rb")
kumoriwavdata = kumoriwavfile.read()
amewavfile = open("ame.wav", mode = "rb")
amewavdata = amewavfile.read()
tokorowavfile = open("tokoroniyori.wav", mode = "rb")
tokorowavdata = tokorowavfile.read()

# 文の生成
for i in range(100):
    sentence()
    print()
 
# genwf.pyの終わり
