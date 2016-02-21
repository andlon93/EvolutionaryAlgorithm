import random as rng
import numpy as np
import copy
import OneMax as OM
### Function that: normalise the fitness of a generation.
###				   The sum of all fitnesses will be 1
#	Input:         list of all individuals in the generation
#   Outout:        Void
def normalise_fitness(generation):
	# --- Initialize the sum of all fitnesses.
	summ = 0
	#print("generation", generation)
	# --- Iterate through all individuals in the generation
	#     to sum up all fitnesses.
	for individ in generation:
		summ += individ.fitness
	#print(summ)

	# --- Iterate through all individuals and update fitness 
	#     to the normalized value.
	#summm = 0
	for individ in generation:
		individ.normalised_fitness = individ.fitness/summ
		#summm += individ.normalised_fitness
	#print("\nShould Be 1: ",summm)
#
#
# --- Function: Fitness proportionate.
#     Input:  list of individuals
#     Output: none, but the fitness of the individuals are scaled.
def fitness_proportionate_scaling(individuals):

	# --- Calculate average fitness and standard deviation.
	avg_fitness = 0
	for individual in individuals:
		avg_fitness += individual.fitness
	avg_fitness = avg_fitness/len(individuals)

	# --- Scale fitness values by dividing by averge fitness.
	for individual in individuals:
		individual.fitness = individual.fitness/avg_fitness
#
# --- Function: Sigma scaling.
#     Input:  list of individuals
#     Output: none, but the fitness of the individuals are scaled.
def sigma_scaling(individuals):

	# --- Calculate average fitness and standard deviation.
	avg_fitness = 0
	for individual in individuals:
		avg_fitness += individual.fitness
	avg_fitness = avg_fitness/len(individuals)
	std_fitness = 0
	for individual in individuals:
		std_fitness += (individual.fitness - avg_fitness)**2
	std_fitness = np.sqrt(std_fitness/(len(individuals)-1))

	# --- Scale fitness values by sigma scaling conversion.
	for individual in individuals:
		if std_fitness < 1.0e-6:
			individual.fitness = 1.0
		else:
			individual.fitness = 1.0 + (individual.fitness - avg_fitness) / (2*std_fitness)
#
#
# --- Function: Boltzmann scaling.
#     Input:  list of individuals
#     Output: none, but the fitness of the individuals are scaled.
def boltzmann_scaling(individuals, T):

	# --- Calculate average of exp(f(i)/T) for the hole generation.
	avg_exp = 0
	for individual in individuals:
		avg_exp += np.exp(individual.fitness/T)
	avg_exp = avg_exp/len(individuals)

	# --- Scale fitness values by boltzmann scaling conversion.
	for individual in individuals:
		individual.fitness =  np.exp(individual.fitness/T) / avg_exp
#
#
# --- Function: Rank .
#     Input:         list of individuals
#     Output:        none, but the fitness of the individuals are scaled.
def rank_scaling(individuals):
	
	# --- Set the expected values of the least and best ﬁt individuals, respectively.
	min_fitness = 0.5 
	max_fitness = 2 - min_fitness
	#for individual in individuals:
	#	min_fitness = individual.fitness if (individual.fitness < min_fitness) else min_fitness
	#	max_fitness = individual.fitness if (individual.fitness > max_fitness) else max_fitness 
	
	# --- Selects the N individuals with the best fitness.
	individuals = sorted(individuals, key=lambda individual: individual.fitness)

	# --- Scale fitness values by rank scaling conversion.
	for rank in range(1, len(individuals)+1):
		individuals[rank-1].fitness = min_fitness + (max_fitness - min_fitness) * (rank - 1) / (len(individuals)-1)
#
#
### Function that: Select parents globally
#	Input:         list of the individs that may become parents, number of parents to make
#   Outout:        Parents
def Global_Selection(individuals, number_of_parents):
	
	# --- Initialize list of parents.
	parents = []
	avg=0.0

	# --- Scale the individuals fitness.
	#fitness_proportionate_scaling(individuals)

	# --- Normalise the individuals fitness to be in the interval [0, 1]
	normalise_fitness(individuals)

	# --- Sort the array of indivduals with respect to fitness.
	individuals = sorted(individuals, key=lambda individual: individual.fitness)
	#print('i: ', individuals)

	# --- Pick N parents.
	#while len(parents) < number_of_parents:
	for qwerty in range(number_of_parents):
		# ---- Get a random number between 0.0 and 1.0
		number = rng.random()

		# --- Minimum probability.
		minProb = 0.0

		# --- Find the corresponding individual in the roulette wheel.
		#     If the random number is within individual's part of 
		#     the roulette wheel that individ is chosen to become parent.
		for i in range(len(individuals)):
			fit = individuals[i].normalised_fitness
			#print(minProb, ' <= ', number, ' < ', (minProb+fit))
			if minProb <= number and number < minProb + fit:
				#print(minProb*100, ' <= ', number*100, ' < ', (minProb+fit)*100)
				new_parent = individuals[i]
				#new_parent.update_fitness()
				parents.append(new_parent)
				avg += (i+1)
				if len(parents) == number_of_parents:
					#for ind in individuals:
					#	ind.update_fitness()
					return parents#, avg/number_of_parents
				break
			minProb += fit

#
### Function that: Select parents locally
#	Input:         list of the individs that may become parents, number of parents to make
#   Outout:        Parents
def Tournament_Selection(adults, N_parents, eps, N):

	# --- The list containing the chosen parents.
	parents = []

	# --- Runs while not all parents have been chosen.
	while (len(parents) < N_parents):

		# --- Pick N random adults and put them in the "pool".
		pool = make_pool(adults, N)

		# --- Sort the pool of individuals.
		pool = sorted(pool, key=lambda individual: individual.fitness)

		# --- Generate a random number.
		rnd = rng.random()

		# --- The best individual from the pool is chosen with
		#     a probabilty (1-eps), the next best chosen with 
		#     probability (1-eps)*eps, the i'th best with 
		#     probability (1-eps)*eps^(i-1).
		for i in range(1, N+1):
			if rnd < (1-eps)*eps**(i-1):
				parents.append(pool[N-i])
				break

	return parents

def make_pool(adults, N):
	pool = []
	while len(pool) < N:
		chosen = adults[rng.randint(0, len(adults)-1)]
		if chosen not in pool:
			pool.append(chosen)
	return pool
#
if __name__ == '__main__':
	
	#avg2 = 0.0
	#std2 = 0.0
	N = 100
	for i in range(N):
		adults = []
		for it in range(20):
			adults.append(OM.individual(20, 0.05))
		parents = Global_Selection(adults, 20)
		#print(avg)
		#avg2 += avg
		#std2 += (avg - avg2/(i+1))**2
	#print('avg: ', avg2/N)
	#print('std: ', np.sqrt(std2/(N-1)) )
	print(len(adults), len(parents))
