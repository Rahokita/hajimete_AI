# -*- coding: utf-8 -*-
"""
ana3gram.pyプログラム
3-gram出現頻度リストの作成
使い方　c:\>python ana3gram.py < (日本語テキストデータ）
"""
# モジュールのインポート
import sys
import collections
import pprint

# メイン実行部
# 解析対象文字列の読み込み
inputtext = sys.stdin.read()

# 3-gramの生成
ngram = [ ]
for i in range(len(inputtext) - 2):
    ngram.append(inputtext[i:i+3])
# 並べ替え
c = collections.Counter(ngram)
pprint.pprint(c)

# ana3gram.pyの終わり
