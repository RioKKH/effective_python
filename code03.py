#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
bytesとstrの違いを知っておく
python3では文字列データを表すのにbytesとstrの2つがある。
"""

def main():
    # bytes
    print('\n\nbytes:')
    a = b'h\x65llo' # 生の符号なし8ビットからなる
    # x65(16進数の65) を10進数に直すと101になる
    print(list(a))  # [104, 101, 108, 108, 111]
    print(a) # b'hello' 通常はASCIIエンコーディングで表示される

    # str
    # strのインスタンスはテキスト文字を表すUnicodeコードポイントを含む
    print('\n\nstr:')
    a = 'a\u0300 propos'
    print(list(a))
    print(a)

    a = "これは？"
    print(list(a))
    print(type(a))
    print(a)


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value # strのインスタンス

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value # bytesのインスタンス

if __name__ == '__main__':
    main()
    print(repr(to_str(b'foo')))
    print(repr(to_str('bar')))

    print(repr(to_bytes(b'foo')))
    print(repr(to_bytes('bar')))
