#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
__call__メソッドはクラスのインスタンスがどこかで、
APIフックのように関数引数として使われてもよいことを
示唆する。
これは新たにコードを読んだ人に、クラスの目的が状態を
持つクロージャとして働く事である、という強い手がかりを
与える
"""

from collections import defaultdict

current = {
    'green': 12,
    'blue': 3
}

increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]

class BetterCountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

counter = BetterCountMissing()
assert counter() == 0
assert callable(counter)


counter = BetterCountMissing()
result = defaultdict(counter, current) # __call__を信頼する
for key, amount in increments:
    result[key] += amount

assert counter.added == 2
