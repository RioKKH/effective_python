#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
項目37
組み込み型の深い入れ子にはせずクラスを作成する

辞書を要素として含む辞書
非常に読みづらいコード例
"""
from collections import defaultdict

class BySubjectGradebook:

    def __init__(self):
        # オブジェクトの動的な内部状態を保存するのに辞書型の変数を用いる
        # Dictionaryの中にDictionaryが存在するデータ構造になっている
        # まずは外側のdict
        self._grades = {}

    def add_student(self, name):
        # 次に内側のdictを定義する。 defaultdictを用いる
        # defaultdictはキーが存在しない場合にデフォルト値を返す。
        # 下の場合にはdefault値がlistになっているので、存在しない
        # キーを指定した場合には[]を返す
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


def main():
    book = BySubjectGradebook()
    book.add_student('Albert Einstein')
    book.report_grade('Albert Einstein', 'Math', 75)
    book.report_grade('Albert Einstein', 'Math', 65)
    book.report_grade('Albert Einstein', 'Gym', 90)
    book.report_grade('Albert Einstein', 'Gym', 95)

    print(book.average_grade('Albert Einstein'))


if __name__ == '__main__':
    main()

