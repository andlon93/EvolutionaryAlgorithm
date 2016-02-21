import random as rng
import numpy as np
import copy
import matplotlib.pyplot as plt
import OneMax as OM
import LOLZ
import AdultSelection as AS
import ParentSelection as PS
import Crossover
###
def find_best_individual(gen):
	best_fitness = -1
	best_individual = None
	for individual in gen:
		if individual.fitness > best_fitness:
			best_individual = individual
			best_fitness = individual.fitness
	return best_individual

def calculate_avg_std(survivors):

	# --- Calculate average fitness.
	avg_fitness = 0
	for survivor in survivors:
		avg_fitness += survivor.fitness
	avg_fitness = avg_fitness/len(survivors)

	# --- Calculate standard deviation of fitness.
	std_fitness = 0
	for survivor in survivors:
		std_fitness += (survivor.fitness - avg_fitness)**2
	std_fitness = np.sqrt(std_fitness/(len(survivors)-1))

	return avg_fitness, std_fitness

def EA_Loop(isOneMax, pop_size, generation_limit, NSplits, Crossover_rate, mutation_rate, bit_length):
	# Initialise first child pool. mutate to pheno. fitness calc.

	# --- Initialise population with random candidate solutions.
	children = []
	survivors = []

	if isOneMax:
		for i in range(pop_size):
 			survivors.append(OM.individual(bit_length, mutation_rate))
	else:
		for i in range(pop_size):
			survivors.append(LOLZ.individual(bit_length, 21, mutation_rate)) 

	# --- Initialize generation count.
	Ngenerations = 1

	# --- Find best individual in population.
	best_individual = find_best_individual(survivors)

	# Plot the best score in each generation
	plotting = [best_individual.fitness]
	plotting2 = [calculate_avg_std(survivors)[0]]
	#print("#", Ngenerations, " --- Best individual:\n", "Fitness: ", best_individual.fitness, "Genotype: ", best_individual.genotype)

	# --- Run as long as the best individual has fitness below 1.
	while (best_individual.fitness < 1.0 and Ngenerations < generation_limit):

		# --- Update generation count.
		Ngenerations += 1

		# --- Make N children from the survivors of the previous generation.
		#     Select parents.
		#     Recombine pairs of parents.
		#     Mutate the resulting offspring.
		#print("survivors: ", len(survivors))
		children = Crossover.make_children(isOneMax, survivors, pop_size, NSplits, Crossover_rate)

		# --- Select individuals for the next generation.
		#     N of the best individuals survive (fitness biased).
		survivors = AS.Full_Generational_Replacement(children, pop_size)
		#survivors = AS.Over_Production(children, pop_size)
		#survivors = AS.Generational_Mixing(children, survivors, pop_size)

		# --- Calculate average fitness and standard deviation of fitness.
		avg_fitness, std_fitness = calculate_avg_std(survivors)

		# --- Find best individual in population.
		best_individual = find_best_individual(survivors)

		# --- For plotting
		#plotting.append(best_individual.fitness)
		#plotting2.append(calculate_avg_std(survivors)[0])

		# --- Logging.	
		#if Ngenerations%1000==0: print("#", Ngenerations, "\nBest individual --- ", "Fitness: ", best_individual.fitness, "Genotype: ", best_individual.genotype, "\nAverage of fitness: ", avg_fitness, ". Standard deviation of fitness: ", std_fitness, ".\n")
		#if best_individual.fitness == 1.0: print("#", Ngenerations, "\t Best individual is optimized!")
		
	if (best_individual.fitness == 1.0): return Ngenerations, True, plotting, plotting2
	else: return Ngenerations, False, plotting, plotting2
	#return Ngenerations
#
def main(pop_size):
	isOneMax = True
	N = 200
	sum_generations = 0
	std_generations = 0
	Nfails = 0
	gen_limit = 100
	NSplits = 5
	Crossover_rate = 0.2
	mutation_rate = 0.0005
	bit_length = 40
	for i in range(N):
		Ngenerations, isDone, plots, plots2 = EA_Loop(isOneMax, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
		if not isDone:
			Nfails += 1
		sum_generations += Ngenerations
		std_generations += (Ngenerations - sum_generations/(i+1))**2
	
	# --- Logging data for all the generations.
	print('Average number of generations = ', sum_generations/N, ' Standard deviation of number of generations ~ ', np.sqrt(std_generations/(N-1)))
	print('#fails: ', Nfails, ' / ', i+1, ' = ', Nfails/(i+1)*100, '%\n')

	# --- Plotting
	'''plt.plot(range(1,len(plots)+1), plots, label='best individual')
	plt.plot(range(1,len(plots2)+1), plots2, label='average in population')
	plt.legend(loc='lower right')
	plt.xlabel('Number of generations')
	plt.ylabel('Fitness')
	plt.axis([0, len(plots), 0, 1])
	plt.show()'''
#
if __name__ == '__main__':
	pop_size = 50
	#print("\n--- Population size: ",pop_size)
	#main(pop_size)
	while pop_size < 201: 
		print("\n--- Population size: ",pop_size)
		main(pop_size)
		pop_size += 10