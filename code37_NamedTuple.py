#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
1. 辞書の辞書や、タプルの辞書といった複雑な入れ子構造は作らない
2. 軽量で変更不能なデータコンテナであるnamedtupleをうまく利用する
3. クラスの内部状態を保持する変数が複雑になった場合には、ヘルパー
   クラスを用いて記録管理を行う
"""
from collections import defaultdict
from collections import namedtuple

Grade = namedtuple('grade', ('score', 'weight'))


class Subject:
    """1つの科目を表すクラスを書く

    Attributes:
        _grades (list): list of grades
    """

    def __init__(self):
        """Initialize Subject class
        """
        self._grades = []

    def report_grade(self, score, weight):
        """Report grades

        This method reports the grade of each individual
        
        Args:
            score (int): score as integer
            weight (float): weight for the each subject

        Returns:
            None: No returns
        """
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            #print(grade) # grade(score=xx, weight=yy)
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student:
    def __init__(self):
        self._subjects = defaultdict(Subject)

    def get_subject(self, name):
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count

    
class Gradebook:
    def __init__(self):
        self._students = defaultdict(Student)

    def get_student(self, name):
        return self._students[name]


if __name__ == '__main__':
    book = Gradebook()
    albert = book.get_student('Albert Einstein')

    math = albert.get_subject('Math')
    math.report_grade(75, 0.05)
    math.report_grade(65, 0.15)
    math.report_grade(70, 0.80)

    gym = albert.get_subject('Gym')
    gym.report_grade(100, 0.40)
    gym.report_grade(85, 0.60)

    print(albert.average_grade())
