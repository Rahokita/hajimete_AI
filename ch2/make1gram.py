# -*- coding: utf-8 -*-
"""
make1gram.pyプログラム
文字を単位とした1-gramを作成します
使い方　c:\>python make1gram.py < (テキストデータ）
"""
# モジュールのインポート
import sys

# メイン実行部
# 解析対象文字列の読み込み
inputtext = sys.stdin.read()

# 1-gramの生成
for chr in inputtext:
    print(chr)   

# make1gram.pyの終わり
