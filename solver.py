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

    def fitness(indiv, values, weights, capacity):
        value =  sum(v*t for (v,t) in zip(values, indiv)) 
        weight = sum(w*t for (w,t) in zip(weights, indiv))
        print "value="+str(value)
        return value*(weight<=capacity)
    
    def random_individual(items, rate=.05):
        gene = [0]*items
        for i in range(int(rate*items)):
            gene[randint(0,len(gene)-1)] = 1
        return (fitness(gene, values, weights, capacity), gene)

    def crossover(indiv1, indiv2):
        items = len(indiv1[1])
        start = randint(0, items-1)
        end = randint(start+1, items)
        indiv = list(indiv1)
        indiv[start:end] = indiv2[start:end]
        return (fitness(indiv, values, weights, capacity), indiv)

    def mutation(indiv, rate):
        for i in range(int(len(indiv)*rate)):
            pos = randint(0, len(indiv))
            indiv[pos] = int(not(indiv[pos]))
        return indiv
    

    def draw(cohort, total):
        have = 0
        want = randint(0, total)
        index = -1
        while have<want:
            index += 1
            have += cohort[index][0]
        return index


    def selection(cohort):
        # Sample proportional to fitness
        cohort.sort(reverse=True)
        total = sum(zip(*cohort)[0])
        newcohort = []
        for i in range(len(cohort)):
            newindiv = cohort[draw(cohort, total)][1]
            newcohort.append((fitness(newindiv, values, weights, capacity), newindiv))
        return newcohort


    # Genetic algorithm approach
    # Knapsack seems ideal for this

    capacity, values, weights = parse(inputData)
    items = len(values)
    print "Capacity: %d" % capacity
    print "Items: %d" % items
    
    population = 100
    mutation_rate = .05
    iterations = 50

    cohort = [random_individual(items) for i in range(population)]
    for i in range(iterations):

        cohort = selection(cohort)
        print "-"*80
        for j in range(items):
            print cohort[j]
            print "-"*80
        raw_input("Done with iteration" + str(i))

    value,taken = cohort[0]


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

