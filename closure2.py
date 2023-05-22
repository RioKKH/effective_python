#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
クロージャは、関数の再利用性やコードの構造化に役立ちます。
特に、関数の内部で定義された関数が外部の変数や状態にアクセス
する必要がある場合や、関数の振る舞いを動的に変更する必要が
ある場合にクロージャが有用です。
"""

def counter():
    """
    カウンタの作成
    """
    count = 0

    def increment():
        """
        nonlocal キーワードは、クロージャ内で外部のスコープにある
        変数を参照・変更するために使用されます。クロージャ内の関数が
        外部の変数を参照する場合、その変数は通常、ローカルスコープ
        ではなくグローバルスコープとして扱われます。しかし、nonlocal
        キーワードを使用することで、クロージャ内の関数が外部変数を
        直接参照することができます。
        """
        nonlocal count
        count += 1
        return count

    return increment


# プライベート変数の実現
def private_variable():
    secret = "This is a secret"

    def get_secret():
        return secret

    return get_secret


# 関数の振る舞いをカスタマイズ
def multiply_by(n):
    def multiplier(x):
        return n * x

    return multiplier


counter1 = counter()
print(counter1()) # Output: 1
print(counter1()) # Output: 2

counter2 = counter()
print(counter2()) # Output: 1

# プライベート変数の実現
secret_variable = private_variable()
print(secret_variable()) # Output: "This is a secret"


# 関数の振る舞いをカスタマイズ
multiply_by_2 = multiply_by(2)
multiply_by_3 = multiply_by(3)

print(multiply_by_2(4)) # Output: 8
print(multiply_by_3(4)) # Output: 12


