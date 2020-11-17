import random

from phrase import Phrase, target
from helpers import summarize


popSize = 500
population = []
bestScore = 0
generation = 1

for i in range (popSize):
    population.append(Phrase()) # Phrase () is to create a new object

"""
for i in range (popSize):
    print(population[i].getContents())
"""

while bestScore < len(target):

    for i in range (popSize):
        population[i].getFitness()

        if population[i].fitness > bestScore:
            bestScore = population[i].fitness
            summarize(generation, population[i].getContents(),bestScore)


    
    matingPool = []

    parents = population[:] # copy over list

    population = [] # empty list

    for i in range (popSize):
        for j in range (parents[i].fitness):
            matingPool.append(parents[i])


    for i in range(popSize):
        x = random.choice(range(len(matingPool)))
        y = random.choice(range(len(matingPool)))

        child = matingPool[x].crossover(matingPool[y])

        child.mutate()

        population.append(child)
    
    generation += 1
