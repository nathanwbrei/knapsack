#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

def parse(data):
    lines = data.split('\n')
    capacity = int(lines[0].split()[1])
    values, weights = zip(*[map(int,l.split()) for l in lines[1:-1]])
    return capacity, values, weights


def getdata(filename):
    with open(filename, 'r') as f:
        return ''.join(f.readlines())



def solveIt(inputData):

    # Memoization-in-lieu-of-dynamic-programming
    # Similar-ish performance, requires much less work to write

    capacity, values, weights = parse(inputData)
    taken = [0]*len(values)
    items = len(values)
    
    # Recurrance relation assumes 1-indexing   
    weights = [0] + list(weights)
    values = [0] + list(values)

    soln = np.zeros((capacity+1, len(weights)), dtype=np.uint32)
    for j in xrange(1,len(taken)+1):
        print "%d/%d: %d%% finished..." % (j, items, j*100./items)
        for k in xrange(capacity+1):
            if weights[j] > k:
                soln[k,j] = soln[k,j-1]
            else:
                soln[k,j] = max(soln[k,j-1],
                                soln[k-weights[j],j-1]+values[j])

    # This is where the magic happens
    value = soln[capacity, len(taken)]


    # Backtrace to find which items we have taken
    j = len(taken)
    k = capacity
    while j>0:
        #print "soln(%d, %d) = %d" % (k,j,soln(k,j))
        if soln[k,j] != soln[k,j-1]:
            k -= weights[j]
            taken[j-1] = 1
        j -= 1


    # prepare the solution in the specified output format
    outputData = str(value) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, taken))
    return outputData


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        print solveIt(getdata(fileLocation))
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

