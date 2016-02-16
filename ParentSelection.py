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

		#Update fitness
		individ.fitness = individ.fitness/summ