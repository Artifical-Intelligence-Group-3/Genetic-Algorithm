import math
import random
import os

def initializePopulation():

    #Real Chromosome Representaion [0,1] Interval

    population = []
    for _ in range(POPULATION_SIZE):
        population.append((random.uniform(0,1), random.uniform(0,1)))
    return population

def fitnessCalculation(decoded_population):
    return

def decodeChromosomeToIndividual(population):

    #Real Decoder from [0,1] Interval to [-10,-10] Interval
    return 

def parentSelection(fitness_of_population, population):
    return 


def recombination(parent1, parent2):

    #Recombination using single arithmetic crossover
    return
    
def mutation(child1, child2):
    
    # Uniform Mutation
    return

def exchangePopulation(population, fitness_of_population, child1, child2):
    return



def main():

    global POPULATION_SIZE, UPPER_LIMIT, LOWER_LIMIT, TARGET_MINIMUM_F
    POPULATION_SIZE = 20
    UPPER_LIMIT = 10
    LOWER_LIMIT = -10

    Limitation_of_change = 3000
    change_credit = 0
    generation = 0 
    best_fitness = float('-inf')
    best_individual = (0, 0)
    
    population = initializePopulation()
    while change_credit <= Limitation_of_change:
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

        if best_fitness < max(fitnessCalculation(population)):
            best_fitness = max(fitnessCalculation(population))
            best_individual = population[fitness_of_population.index(max(fitness_of_population))]
            change_credit = 0

        os.system('cls')
        print(f'Generation : {generation}\n')
        print(f'BEST INDIVIDUAL')
        print(f'x1 : {best_individual[0]}')
        print(f'x2 : {best_individual[1]}\n')
        print(f'BEST FITNESS: {best_fitness}\n')

        change_credit += 1
        generation += 1

main()

# # Decode Cromosom to individual
# decoded_population = decodeChromosomeToIndividual(population)
# print("============== DECODED POPULATION ============== ")
# print(decoded_population,"\n\n")

# # Fitness Calculation
# fitness_of_population = fitnessCalculation(decoded_population)
# print("============== FITNESS POPULATION ============== ")
# print(fitness_of_population,"\n\n")

# # Parent Selection
# parent1, parent2 = parentSelection(fitness_of_population, population)
# print(f'parent 1 : {parent1} \nparent 2 : {parent2}\n')

# # Recombination
# child1, child2 = recombination(parent1,parent2)
# print(f'child 1 : {child1} \nchild 2 : {child2}\n') 

# # permutation
# mutated_child1, mutated_child2 = mutation(child1, child2)
# print(f'mutated child 1 : {mutated_child1} \nmutated child 2 : {mutated_child2}\n') 

# # Exchange Population
# population = exchangePopulation(population, fitness_of_population, mutated_child1, mutated_child2)
# print("============== POPULATION ============== ")
# print(population,"\n\n")
