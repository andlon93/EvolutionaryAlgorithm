import random as rng
#
class individual:
	genotype = []
	phenotype = []

	### Constructor
	def __init__(self, n, mutation_prob):
		self.genotype = self.make_Random_Genotype(n)
		self.phenotype = self.make_Phenotype(self.genotype, mutation_prob)
		self.fitness = self.Fitness()

	### Function that: initialise a random list of 0s and 1s of length n
	#	Input:         int n: the length
	#   Outout:        Genotype
	def make_Random_Genotype(self, n):
		genotype = []
		for i in range(n):
			genotype.append(rng.randrange(0,2))
		return genotype

	### Function that: make phenotype based on the genotype
	#	Input:         
	#   Outout:        Phenotype
	def make_Phenotype(self, geno, prob):
		# The list of phenotype bits
		pheno = []

		# Iterate through all bits in the genotype
		for bit in geno:

			# mutate with probability prob
			if rng.random() < prob:
				if bit == 1: 
					pheno.append(0)
				else: 
					pheno.append(1)
			else:
				pheno.append(bit)

		# Return the phenotype
		return pheno

	### Function that: Calculate the fitness of the indidual
	#	Input:         phenotype
	#   Outout:        Fitness value
	def Fitness(self):
		fitness = 0
		for bit in self.phenotype:
			if bit == 1:
				fitness += 1
		return fitness
#
#
if __name__ == '__main__':
	individ = individual(20, 0.05)
	print(individ.genotype)
	print(individ.phenotype)
	print(individ.fitness)
