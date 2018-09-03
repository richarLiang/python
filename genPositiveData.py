# -*- encoding: utf-8 -*-

import os
import random


class RandomData(object):

    def __init__(self, path):
        self.path = path

    def generateRandomNmber(self, rows=100, cols=10, dataRangeFrom=0, dataRangeTo=100):
        matrix = []
        for i in range(rows):
            tempList = []
            for j in range(cols):
                tempList.append(random.randint(dataRangeFrom, dataRangeTo))
            matrix.append([str(o) for o in tempList])
        with open(self.path, "w") as file:
            for row in matrix:
                file.write(' '.join(row) + '\n')


if __name__ == '__main__':
    genData = RandomData('./data/positiveData.txt')
    genData.generateRandomNmber(100, 10, -100, 100)
