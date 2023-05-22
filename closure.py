#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
クロージャ（closure）は、関数とその関数が作成された環境（スコープ）
との結びつきを持つ概念です。クロージャは、関数とその関数が参照する変数
（自由変数）との結びつきを保持し、関数が呼び出された時にその環境を再現
することができます。

クロージャは、以下の特徴を持ちます:

    関数内で別の関数を定義し、内部の関数が外部の関数の変数にアクセスする
    場合にクロージャが作成されます。
    クロージャは、内部の関数を外部に返すことができます。その際、内部の関数は
    外部の環境（スコープ）との結びつきを保持します。
    クロージャは、関数として呼び出すことができます。

"""

def outer_function(x):
    def inner_function(y):
        # 内部の関数が外部の関数の変数"x"にアクセスしているので、
        # クロージャが作成されている。
        return x + y 
    return inner_function

closure = outer_function(5) # inner_functionが返されclosureに代入される 
result  = closure(3) # closureはinner_functionなので3はyに代入される
print(result) # 結果としてxの5とyの3の和が返され、Output: 8となる
