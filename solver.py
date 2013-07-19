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
        return value*(weight<=capacity)
    
    def random_cohort(population, items):
        cohort = []
        while len(cohort)<population: 
            gene = [0]*items
            gene[randint(0,len(gene)-1)] = 1
            fit = fitness(gene, values, weights, capacity)
            if fit>0:
                cohort.append((fit, gene))
        return cohort 

    def crossover(parent1, parent2):
        items = len(parent1)
        start = randint(0, items-1)
        end = randint(start+1, items)
        gene = list(parent1)
        gene[start:end] = parent2[start:end]
        return gene 

    def mutation(indiv, n=2):
        for i in range(n):
            pos = randint(0, len(indiv)-1)
            indiv[pos] = randint(0,1) 
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

        randomgene = [0]*items
        randomgene[randint(0,items-1)]=1
        randomfit = fitness(randomgene, values, weights, capacity)

        newcohort = [cohort[0], (randomfit, randomgene)]
        while len(newcohort) < len(cohort):

            parent1 = cohort[draw(cohort, total)][1]
            parent2 = cohort[draw(cohort, total)][1]
            
            newindiv = crossover(parent1, parent2)
            newindiv = mutation(newindiv)
           
            while True:
                fit = fitness(newindiv, values, weights, capacity)
                if fit>0:
                    break
                if 1 not in newindiv:
                    newindiv[randint(0,items-1)]=1
                else:
                    newindiv[newindiv.index(1)] = 0
            newcohort.append((fit, newindiv))

        newcohort.sort(reverse=True)
        return newcohort


    # Genetic algorithm approach
    # Knapsack seems ideal for this

    capacity, values, weights = parse(inputData)
    items = len(values)
    print "Capacity: %d" % capacity
    print "Items: %d" % items
    
    population = 100
    iterations = 5000


    cohort = random_cohort(population, items) 
    for i in range(iterations):

        print "Iteration %d: %d" % (i, cohort[0][0])
        cohort = selection(cohort)
        print zip(*cohort)[0] 
        print "-"*80

    
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

