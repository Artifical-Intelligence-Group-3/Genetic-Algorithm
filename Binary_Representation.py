import math
import random
import os

    
def recombination(parent1,parent2):
    
    #Uniform Crossover

    child1 = ""
    child2 = ""
    
    for i in range(CHROMOSOME_LENGTH):
        if random.randint(0,1) == 0:
            child1 += parent1[i]
            child2 += parent2[i]
        else:
            child1 += parent2[i]
            child2 += parent1[i]
    
    return child1, child2

def mutation(child1, child2):

    mutated_child_list = [child1 , child2]

    for _, iter_child in mutated_child_list:
        for gen ,iter_gen in range(CHROMOSOME_LENGTH):
            if random.uniform(0,1) < POSSIBLE_MUTATION:
                mutated_child_list[iter_child][iter_gen] = str(int[gen] + 1 % 2)

    return mutated_child_list[0], mutated_child_list[1]
            

def exchangePopulation(population, fitness_of_population, child1, child2):
    new_population = population
    new_generation = [child1, child2]
    fitness_of_new_generation = fitnessCalculation(decodeChromosomeToIndividual(new_generation))
    sorted_fitness_of_old_population = sorted(fitness_of_population)

    for i in range(2):
        for j in range(-1, -POPULATION_SIZE - 1, 1):
            if sorted_fitness_of_old_population(j) < fitness_of_new_generation[i]:
                new_population[fitness_of_population.index(sorted_fitness_of_old_population[j])] = new_generation[i]
                break

    return new_population



def main():
    global LOWER_LIMIT, UPPER_LIMIT, POPULATION_SIZE, CHROMOSOME_LENGTH, POSSIBLE_MUTATION
    LOWER_LIMIT = -10
    UPPER_LIMIT = 10
    POPULATION_SIZE = 20
    CHROMOSOME_LENGTH = 8
    POSSIBLE_MUTATION = 1 / (20 * 8)

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

        break

main()