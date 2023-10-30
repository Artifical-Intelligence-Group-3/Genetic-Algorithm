if max(fitnessCalculation(decodeChromosomeToIndividual(population))) > best_fitness:
            best_fitness = max(fitnessCalculation(decodeChromosomeToIndividual(population)))
            best_individual = population[fitness_of_population.index(max(fitness_of_population))]
            change_credit = 0