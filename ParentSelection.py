import random as rng
import copy
import OneMax as OM
### Function that: normalise the fitness of a generation.
###				   The sum of all fitnesses will be 1
#	Input:         list of all individuals in the generation
#   Outout:        Void
def normalise(generation):
	# The sum of all fitnesses from all individuals
	summ = 0

	#Iterate through all individuals in the generation
	for individ in generation:

		#add each individuals fitness to the sum
		summ += individ.fitness

	##Iterate through all individuals and update fitness
	for individ in generation:

		#Update individuals fitness
		individ.fitness = individ.fitness/summ
#
### Function that: Select parents globally
#	Input:         list of the individs that may become parents, number of parents to make
#   Outout:        Parents
def Global_Selection(temp, number_of_parents):
	generation = copy.deepcopy(temp) # MÅ FIKSES!!
	# List of parents
	parents = []
	#
	'''elitism = 4
	for n in range(elitism):
		best_fitness = 0
		best_individual = None
		index = 0
		for i in range(len(generation)):
			if generation[i].fitness > best_fitness:
				best_fitness = generation[i].fitness
				best_individual = generation[i]
				index = i
		parents.append(best_individual)
		#print(index)
		generation.pop(index)'''
	#
	for q in range(number_of_parents):
		#print ("Iterasjon: ",q)

		# Get a random number between 0.0 and 1.0
		number = rng.random()
		#print(number)

		#Normalise the individuals fitness to represent probabilities
		normalise(generation)

		# Each individuals part of the roulette wheel
		min_prob = 0

		# Iterate through the individuals
		for i in range(len(generation)):
			# If random number is within the part of roulette wheel,
			# individ is chosen to become parent
			fit = generation[i].fitness
			#print("fit: ", fit,"  From: ",min_prob, "  To:", fit+min_prob)
			if number < min_prob + fit and number >= min_prob:
				#print("Denne ble valgt")
				parents.append(generation[i])
				generation.pop(i)

				if len(parents) == number_of_parents: return parents
				break
			min_prob += fit
			#print("\n")
	#return the list of new parents
	return parents
#
### Function that: Select parents locally
#	Input:         list of the individs that may become parents, number of parents to make
#   Outout:        Parents
def Local_Selection(generation, number_of_parents, k, epsilon):
	# List of lists with members of each tournament
	tournaments = []

	# One iteration for each tournament
	#for i in range(number_of_parents):


	pass
#
if __name__ == '__main__':
	l=[]
	for n in range(50):
		l.append(OM.individual(50, 0.05))
	b= Global_Selection(l, 20)
	print(len(l), len(b))
