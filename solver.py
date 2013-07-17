#!/usr/bin/python
# -*- coding: utf-8 -*-

from memoize import memoize

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
    
    # Recurrance relation assumes 1-indexing   
    weights = [0] + list(weights)
    values = [0] + list(values)

    @memoize
    def soln(k,j):
        if j==0:
            return 0
        elif weights[j] > k:
            return soln(k,j-1)
        else:
            return max(soln(k,j-1), 
                       soln(k-weights[j],j-1) + values[j])


    # This is where the magic happens
    value = soln(capacity, len(taken))


    # Backtrace to find which items we have taken
    j = len(taken)
    k = capacity
    while j>0:
        #print "soln(%d, %d) = %d" % (k,j,soln(k,j))
        if soln(k,j) != soln(k,j-1):
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

