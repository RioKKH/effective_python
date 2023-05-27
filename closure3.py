#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
クロージャと nonlocal キーワードを組み合わせることで、
特定の状態を保持する必要がある関数や、動的な振る舞いを
持つ関数を作成できます。クロージャを使用することで、
関数の内部と外部のスコープを適切に分離し、関数の再利用性や
保守性を向上させることができます。
nonlocal キーワードは、クロージャをより柔軟に使い、
外部の変数を操作するための重要な手段です。
クロージャと組み合わせて使用することで、状態の保持や動的な
振る舞いを持つ関数を実現することができます。
"""

def outer_function():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    def decrement():
        nonlocal count
        count -= 1
        return count

    return increment, decrement


increment_func, decrement_func = outer_function()
print(increment_func()) # Output: 1
print(increment_func()) # Output: 2
print(decrement_func()) # Output: 1
current_cnt = decrement_func()
print(current_cnt)
