import random as rng

class individual:
	fitness = 0
	genotype = []
	phenotype = []

	def __init__(self, n):
		self.genotype = self.make_Random_Genotype(n)


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
	def make_Phenotype(self):
		pass

	### Function that: Calculate the fitness of the indidual
	#	Input:         phenotype
	#   Outout:        Fitness value
	def Fitness(self):
		pass


if __name__ == '__main__':
	individ = individual(20)
	print(individ.genotype)