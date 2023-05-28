#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Pythonはクラスのコンストラクタとして__init__という
  一つのメソッドしかサポートしていない  
# 代わりのコンストラクタを定義するには@classmethodを使う
# クラスメソッドポリモーフィズムを使う
"""

"""
MapReduceは、Googleが開発した大量のデータを効率的に処理するための
プログラミングモデルおよびその関連ツールです。大規模データ処理に特化していて、
分散システムで動作します。具体的には、データを複数のコンピュータノードに
分散させ、各ノードが部分的な処理を行い、その結果をまとめて全体の結果を生成します。

MapReduceの名前は、その2つの主要なステップから来ています：
MapステップとReduceステップです。

1. **Mapステップ**: 入力データは「キー/値」ペアとして考えられ、
このデータが「Map」関数に送られます。
各「Map」関数は、入力のキー/値ペアを処理し、一連の中間キー/値ペアを生成します。

2. **Reduceステップ**: 中間キー/値ペアは、「Reduce」関数に送られます。
各「Reduce」関数は、あるキーに関連付けられた全ての値を集め、
それらを一緒に処理して、より小さなセットの値を生成します。

これらのステップが全体のデータセットに対して繰り返され、
最終的な結果が生成されます。

MapReduceの主な利点は、プログラマが分散データ処理の詳細を気にすることなく、
簡単に大量のデータを処理することができる点です。
MapReduceは、データの分割、タスクの分配、マシンの故障からの回復、
結果の集計などをハンドリングします。
これにより、開発者はMap関数とReduce関数に焦点を当てることができます。

Hadoopは、MapReduceのオープンソース実装として広く知られています。
"""


import os
import random
from threading import Thread

class InputData:
    def read(self):
        # サブクラスで定義する必要のあるメソッド
        raise NotImplementedError

class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        # 各サブクラスで処理するデータに合わせた処理を実施することが出来る
        with open(self.path) as f:
            return f.read()

class Worker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError()

class LineCountWorker(Worker):
    # Workerのサブクラス
    # 改行('\n')をカウントする機能を実装したMapReduce関数
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))

def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers

def execute(workers):
    # 複数のスレッドに実行ステップをmapすることによって
    # これらのWorkerインスタンスを並列にreduceを繰り返し
    # 呼び出して、結果を1つの最終的な値にまとめる
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, *rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result

def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)

def write_test_files(tmpdir):
    os.makedirs(tmpdir)
    for i in range(100):
        with open(os.path.join(tmpdir, str(i)), 'w') as f:
            f.write('\n' * random.randint(0, 100))

tmpdir = 'test_inputs'
#write_test_files(tmpdir)

result = mapreduce(tmpdir)
print(f'There are {result} lines')



class GenericInputData:
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        # 各サブクラスで処理するデータに合わせた処理を実施することが出来る
        with open(self.path) as f:
            return f.read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)

config = {'data_dir': tmpdir}
result = mapreduce(LineCountWorker, PathInputData, config)
print(f'There are {result} lines')
