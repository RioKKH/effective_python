#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PEP8スタイルガイドに従う


class CapializeWord:

    def __init__(self):
        print("constructor")
        _protected_variable: int = 0
        __private_variable: int = 0

    @classmethod
    def class_method(cls):
        print("class method") 
        
    def lowercase_underscore(self):
        print("lowercase and underscore")


def main() -> None:
    try:
        c = CapializeWord()

    except CapializeWordAsException as e:
        print("Exception: ", e)
