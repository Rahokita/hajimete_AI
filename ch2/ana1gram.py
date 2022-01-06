# -*- coding: utf-8 -*-
"""
ana1gram.pyプログラム
1-gram出現頻度リストの作成
使い方　c:\>python ana1gram.py < (日本語テキストデータ）
"""
# モジュールのインポート
import sys
import collections
import pprint

# メイン実行部
# 解析対象文字列の読み込み
inputtext = sys.stdin.read()

# 1-gramの生成と並べ替え
c = collections.Counter(list(inputtext))
pprint.pprint(c)

# ana1gram.pyの終わり
