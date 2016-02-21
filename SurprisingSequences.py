import random as rng
#
class individual:
	genotype_Length = 0
	mutation_prob = 0
	genotype = []
	fitness = 0
	normalised_fitness = 0
	z = None
	### Constructor
	def __init__(self, n, m, mutation_prob, genotype=None):
		self.mutation_prob = mutation_prob
		self.genotype_Length = n
		self.genotype = genotype
		if (self.genotype == None): self.make_Random_Genotype(n, m)
		self.update_fitness()
	#
	def __repr__(self): return str(self.fitness)
	#
	### Function that: initialise a random list of 0s and 1s of length n
	#	Input:         int n: the length
	#   Outout:        Genotype
	def make_Random_Genotype(self, n):
		genotype = []
		for i in range(n):
			genotype.append(rng.randrange(0,2))
		self.genotype = genotype