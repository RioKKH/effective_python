#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
項目37
組み込み型の深い入れ子にはせずクラスを作成する
"""

class SimpleGradebook:

    def __init__(self):
        # オブジェクトの動的な内部状態を保存するのに辞書型の変数を用いる
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


def main():
    book = SimpleGradebook()
    book.add_student('Isaac Newton')
    book.report_grade('Isaac Newton', 90)
    book.report_grade('Isaac Newton', 95)
    book.report_grade('Isaac Newton', 85)

    print(book.average_grade('Isaac Newton'))


if __name__ == '__main__':
    main()

