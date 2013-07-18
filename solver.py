#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import scipy.weave as w 


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

    # True dynamic programming
    # scipy/weave inlined C code makes it faster

    capacity, values, weights = parse(inputData)
    taken = [0]*len(values)
    items = len(values)
    #print "Capacity: %d" % capacity
    #print "Items: %d" % items
    #print "Est running time: %ds" % (capacity*items/20000000.)
    
    # Recurrance relation assumes 1-indexing   
    weights = [0] + list(weights)
    values = [0] + list(values)

    soln = np.zeros((capacity+1, len(weights)), dtype=np.uint32)
    code = """
    for (int j=1;j<=items;j++){
        for (int k=0;k<=capacity;k++){
            if (int(weights[j]) > k){
                soln(k,j) = soln(k,j-1);
            } else {
                soln(k,j) = fmax(soln(k,j-1), soln(k-int(weights[j]),j-1) + int(values[j]));
            }
        }
    }
    """
    w.inline(code, ['soln','weights','values','capacity','items'], type_converters=w.converters.blitz)

    # Backtrace to find which items we have taken
    j = len(taken)
    k = capacity
    while j>0:
        #print "soln(%d, %d) = %d" % (k,j,soln[k,j])
        if soln[k,j] != soln[k,j-1]:
            k -= weights[j]
            taken[j-1] = 1
        j -= 1

    value = soln[capacity, len(taken)]

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

