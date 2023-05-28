#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MyBaseClass:
    def __init__(self, value):
        self.value = value

class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)

class TimesTwo:
    def __init__(self):
        if hasattr(self, 'value'):
            self.value *= 2
        else:
            sys.ex

class PlusFive:
    def __init__(self):
        self.value += 5


# Superクラスの定義順:
# MyBaseClass --> TimesTwo --> PlusFive
class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        # Superクラスの呼び出し順:
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


# Superクラスの定義順がことなるが:
# MyBaseClass --> PlusFive --> PlusFive
class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        # Superクラスの呼び出し順は上と一緒:
        MyBaseClass.__init__(self, value)
        print(self.value)
        TimesTwo.__init__(self)
        print(self.value)
        PlusFive.__init__(self)
        print(self.value)


foo = OneWay(5)
print('First ordering is (5 * 2) + 5 = ', foo.value)

bar = AnotherWay(5)
print('Second ordering is ', bar.value)
# クラスの継承順が異なっても演算結果同じになるので、
# このコードを初めて見る人にはわかりづらい実装になっている


# 次にダイヤモンド継承問題を考える。
# ダイヤモンド継承とは A-B, A-C, B-D & C-Dのような継承関係をいう
class TimesSeven(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 7


class PlusNine(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 9


class ThisWay(TimesSeven, PlusNine):
    def __init__(self, value):
        TimesSeven.__init__(self, value)
        PlusNine.__init__(self, value)

foo = ThisWay(5)
print('Should be (5 * 7) + 9 = 44 but is ', foo.value)
# これはPlusNineの__init__を実行したタイミングで
# MyBaseClass.__init__()が実行され、そのタイミングで
# self.value が5にセットされてしまうためである。
      
# この問題を解決するためにはsuperとメソッド解決順序
# Method Resolution Orcer: MROを利用する。
# MROはC3線形化と呼ばれるアルゴリズムに従ってスーパークラス
# の初期化手順を定義する

class TimesSevenCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 7


class PlusNineCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value += 9


class GoodWay(TimesSevenCorrect, PlusNineCorrect):
    def __init__(self, value):
        super().__init__(value)


foo = GoodWay(5)
print("Should be 7 * (5 + 9) = 98 and is ", foo.value)


# 呼び出し順は以下の手法で確認できる
mro_str = '\n'.join(repr(cls) for cls in GoodWay.mro())
print(mro_str)
# Goodway(5) --> TimesSevenCorrect.__init__ --> 
# PlusNineCorrect.__init__ --> MyBaseClass.__init__
# の順で呼び出され、ダイヤモンドの頂点に達すると、
# 初期化メソッドは、__init__メソッドが呼ばれたのと逆順で
# 実行される
# self.value <- 5 (5)
# self.value + 9 (14)
# self.value * 7 (98)


# 以下の3つは等価
class ExplicitTrisect(MyBaseClass):
    # Trisect : 三等分する
    def __init__(self, value):
        super(ExplicitTrisect, self).__init__(value)
        self.value /= 3

class AutomaticTrisect(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value)
        self
        self.value /= 3

class ImplicitTrisect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        # Pytnonのコンパイラが自動的にた正しい引数(__class__, self)を
        # 補うのでインスタンスの初期化時にこれらの引数の指定は必須ではない
        self.value /= 3

assert ExplicitTrisect(9).value  == 3
assert AutomaticTrisect(9).value == 3
assert ImplicitTrisect(9).value  == 3
