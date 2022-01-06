# -*- coding: utf-8 -*-
"""
prep.pyプログラム
改行コードと、青空文庫のルビを取ります
使い方　c:\>python prep.py < (青空文庫のテキストデータ）
"""
# モジュールのインポート
import sys
import re

# メイン実行部
# 解析対象文字列の読み込み
inputtext = sys.stdin.read()

# 文字列の加工
outputtext = inputtext.replace('\n', '')         # 改行の削除
outputtext = re.sub('《.+?》', '', outputtext)   # ルビ《》の削除
outputtext = re.sub('｜', '', outputtext)        # ルビ開始記号｜の削除
outputtext = re.sub('［＃.+?］', '', outputtext) # 入力者注［＃］の削除
print(outputtext)

# prep.pyの終わり
