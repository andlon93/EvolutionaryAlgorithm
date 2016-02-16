import random as rng
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
### Function that: Select parents
#	Input:         list of the individs that may become parents, number of parents to make
#   Outout:        Parents
def Global_Selection(generation, number_of_parents):
	# List of parents
	parents = []

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
if __name__ == '__main__':
	for n in range(20):
		l=[]
		for n in range(50):
			l.append(OM.individual(50, 0.05))
		#print(len(l))
		b= Global_Selection(l, 20)
		print(len(l), len(b))
