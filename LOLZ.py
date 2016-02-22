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
	def __init__(self, n, z, mutation_prob, genotype=None):
		self.mutation_prob = mutation_prob
		self.genotype_Length = n
		self.genotype = genotype
		if (self.genotype == None): self.make_Random_Genotype(n)
		self.z = z
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
	#
	### Function that: mutate with a probability 
	#	Input:         
	#   Outout:        boolean: isMutated
	def try_to_mutate(self):
		is_mutated = False
		# Iterate through all bits in the genotype
		for i in range(len(self.genotype)): 
			# try_to_mutate with probability prob
			if rng.random() < self.mutation_prob:
				if self.genotype[i] == 1: self.genotype[i] = 0
				else: self.genotype[i] = 1
				self.update_fitness()
				is_mutated = True
		return is_mutated
	#
	''' --- START Fitness functions --- '''
	### Function that: Calculate the fitness of the indidual
	#	Input:         self.genotypetype
	#   Outout:        Fitness value in interval [0, 1]
	def update_fitness(self):
		if self.genotype[0] == 1: self.onesFitness()
		else: self.zerosFitness()
	#
	def onesFitness(self):
		#print("ones")
		fitness = 0
		for bit in self.genotype:
			if bit != 1:
				break
			fitness += 1
		self.fitness = fitness/self.genotype_Length
	#
	def zerosFitness(self):
		#print("zeros")
		fitness = 0
		for i in range(self.genotype_Length):
			if i < self.z and self.genotype[i] == 0:
				fitness += 1
			else:
				break
		self.fitness = fitness/self.genotype_Length
	''' --- END Fitness functions --- '''
	#
if __name__ == '__main__':
	individ = individual(10, 5, 0.05, [0,0,0,0,0,1,1,1,1,0])
	print(individ.genotype)
	print(individ.fitness)
	for i in range(10):
		if(individ.try_to_mutate()):
			print(individ.genotype)
			print(individ.fitness)