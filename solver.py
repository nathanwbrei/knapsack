#!/usr/bin/python
# -*- coding: utf-8 -*-


def parse(data):
    lines = data.split('\n')
    capacity = int(lines[0].split()[1])
    values, weights = zip(*[map(int,l.split()) for l in lines[1:-1]])
    return capacity, values, weights


def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input

    # Slightly better greedy algorithm. Takes every item that will fit,
    # ordered by value/weight

    capacity, values, weights = parse(inputData)
    taken = [0]*len(values)
    
    reorganized = [(float(v)/w, i) for (v,w,i) in zip(values, weights, range(len(values)))]
    reorganized.sort(reverse=True)
    weight = 0
    value = 0

    while reorganized:
        
        i = reorganized.pop(0)[1]

        if weight + weights[i] <= capacity:
            weight += weights[i]
            value += values[i]
            taken[i] = 1

    # prepare the solution in the specified output format
    outputData = str(value) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, taken))
    return outputData


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

