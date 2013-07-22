#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import scipy.weave as w 
from random import randint

def parse(data):

    # parse the input
    lines = data.split('\n')

    firstLine = lines[0].split()
    items = int(firstLine[0])
    capacity = int(firstLine[1])

    values = []
    weights = []

    for i in range(1, items+1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    return capacity, values, weights

def getdata(filename):
    with open(filename, 'r') as f:
        return ''.join(f.readlines())



def solveIt(inputData):

    def fitness(indiv):
        value =  sum(v*t for (v,t) in zip(values, indiv)) 
        weight = sum(w*t for (w,t) in zip(weights, indiv))
        return value*(weight<=capacity)
    
    def modify(soln):
        newsoln = soln[:]
        for i in range(randint(1,20)):
            newsoln[randint(0,items-1)] = randint(0,1)
        return newsoln
    
    capacity, values, weights = parse(inputData)
    items = len(values)
    print "Capacity: %d" % capacity
    print "Items: %d" % items
    
    soln = [0]*items
    fit = fitness(soln)
    for i in range(1000000):
        soln2 = modify(soln)
        fit2 = fitness(soln2)
        if fit2>fit:
            soln = soln2
            fit = fit2

            print "Iteration %d: %d | %d" % (i, fit2, fit)
    
    # prepare the solution in the specified output format
    outputData = str(fit) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, soln))
    return outputData


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        print solveIt(getdata(fileLocation))
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

