import math
import random
import os



def main()
    global LOWER_LIMIT, UPPER_LIMIT, POPULATION_SIZE, CHROMOSOME_LENGTH
    LOWER_LIMIT = -10
    UPPER_LIMIT = 10
    POPULATION_SIZE = 20
    CHROMOSOME_LENGTH = 8

    limitation_of_change = 3000
    change_credit = 0
    generation = 0
    best_fitness = float('-inf')
    best_individual = ""

    population = initializePopulation()

    while change_credit <= limitation_of_change:
        # Decode Cromosom to individual
        decoded_population = decodeChromosomeToIndividual(population)

        # Fitness Calculation
        fitness_of_population = fitnessCalculation(decoded_population)

        # Parent Selection
        parent1, parent2 = parentSelection(fitness_of_population, population)

        # Recombination
        child1, child2 = recombination(parent1,parent2)
        
        # permutation
        mutated_child1, mutated_child2 = mutation(child1, child2)

        # Exchange Population
        population = exchangePopulation(population, fitness_of_population, mutated_child1, mutated_child2)

        # if best_fitness < max(fitnessCalculation(population)):
        #     best_fitness = max(fitnessCalculation(population))
        #     best_individual = population[fitness_of_population.index(max(fitness_of_population))]
        #     change_credit = 0

        # os.system('cls')
        # print(f'Generation : {generation}\n')
        # print(f'BEST INDIVIDUAL')
        # print(f'x1 : {best_individual[0]}')
        # print(f'x2 : {best_individual[1]}\n')
        # print(f'BEST FITNESS: {best_fitness}\n')

        # change_credit += 1
        # generation += 1

main()