#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
項目37
組み込み型の深い入れ子にはせずクラスを作成する

各教科の点数に重みを付けたうえで集計する
"""

from collections import defaultdict

class WeightedGradebook:

    def __init__(self):
        # オブジェクトの動的な内部状態を保存するのに辞書型の変数を用いる
        # 外型のdict
        self._grades = {}

    def add_student(self, name):
        # defaultdictはキーが存在しない場合にデフォルト値を返す。
        # 下の場合にはdefault値がlistになっているので、存在しない
        # キーを指定した場合には[]を返す
        self._grades[name] = defaultdict(list) # 内側のdict

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]

        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight

            score_sum += subject_avg / total_weight
            score_count += 1

        return score_sum / score_count


def main():
    book = WeightedGradebook()
    book.add_student('Albert Einstein')
    book.report_grade('Albert Einstein', 'Math', 75, 0.05)
    book.report_grade('Albert Einstein', 'Math', 65, 0.15)
    book.report_grade('Albert Einstein', 'Math', 70, 0.80)
    book.report_grade('Albert Einstein', 'Gym', 100, 0.40)
    book.report_grade('Albert Einstein', 'Gym', 85, 0.60)

    print(book.average_grade('Albert Einstein'))


if __name__ == '__main__':
    main()

