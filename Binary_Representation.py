import math
import random
import os

def decodeChromosomeToIndividual(population):
    alpha = 0.0
    beta_x1 = 0.0
    beta_x2 = 0.0

    decoded_population = []
    for chromosome in population:
        for i in range(CHROMOSOME_LENGTH // 2):
            alpha += 2**(-(i + 1))
            beta_x1 += int(chromosome[i]) * 2**(-(i + 1))
            beta_x2 += int(chromosome[i + CHROMOSOME_LENGTH//2 - 1]) * 2**(-(i + 1))
            print(int(chromosome[i]), int(chromosome[CHROMOSOME_LENGTH//2 + i]))
            print(alpha)
        print()
        decoded_population.append((LOWER_LIMIT + (UPPER_LIMIT - LOWER_LIMIT) / alpha * beta_x1, LOWER_LIMIT + (UPPER_LIMIT - LOWER_LIMIT) / alpha * beta_x2))
    return decoded_population #Rumus Sesuai Buku



def initializePopulation():
    population = []
    for _ in range(POPULATION_SIZE):
        chromosome = ""
        for _ in range(CHROMOSOME_LENGTH):
            chromosome += str(random.randint(0,1))
        population.append(chromosome)
    return population


def fitnessCalculation(decoded_population):
    fitness_of_population = []
    a = 0.01
    for individual in decoded_population:
        x1 = individual[0]
        x2 = individual[1]
        fitness_of_population.append(1/(-(math.sin(x1) * - math.cos(x2) + 4/5 * math.exp(1 - (x1**2 + x2 ** 2) ** 0.5))) + a)
    return fitness_of_population

def parentSelection(fitness_of_population, population):
    sorted_fitness = sorted(fitness_of_population)

    # collect 2 largest fitness  
    return population[fitness_of_population.index(sorted_fitness[-1]), fitness_of_population.index(sorted_fitness[-2]) ]

def main():
    global LOWER_LIMIT, UPPER_LIMIT, POPULATION_SIZE, CHROMOSOME_LENGTH
    LOWER_LIMIT = -10
    UPPER_LIMIT = 10
    POPULATION_SIZE = 2
    CHROMOSOME_LENGTH = 8

    limitation_of_change = 3000
    change_credit = 0
    generation = 0
    best_fitness = float('-inf')
    best_individual = ""

    population = initializePopulation()
    print(population)

    while change_credit <= limitation_of_change:
        # Decode Cromosom to individual
        decoded_population = decodeChromosomeToIndividual(population)
        print(decoded_population)

        # Fitness Calculation
        fitness_of_population = fitnessCalculation(decoded_population)
        print(fitness_of_population)

        # Parent Selection
        # parent1, parent2 = parentSelection(fitness_of_population, population)
        # print(parent1, parent2)

        # # Recombination
        # child1, child2 = recombination(parent1,parent2)
        
        # # permutation
        # mutated_child1, mutated_child2 = mutation(child1, child2)

        # # Exchange Population
        # population = exchangePopulation(population, fitness_of_population, mutated_child1, mutated_child2)

    #     # if best_fitness < max(fitnessCalculation(population)):
    #     #     best_fitness = max(fitnessCalculation(population))
    #     #     best_individual = population[fitness_of_population.index(max(fitness_of_population))]
    #     #     change_credit = 0

    #     # os.system('cls')
    #     # print(f'Generation : {generation}\n')
    #     # print(f'BEST INDIVIDUAL')
    #     # print(f'x1 : {best_individual[0]}')
    #     # print(f'x2 : {best_individual[1]}\n')
    #     # print(f'BEST FITNESS: {best_fitness}\n')

    #     # change_credit += 1
    #     # generation += 1
        break

main()