import random as rng
#
class individual:
	goal_string = []
	genotype_Length = 0
	mutation_prob = 0
	genotype = []
	fitness = 0
	### Constructor
	def __init__(self, n, mutation_prob):
		self.mutation_prob = mutation_prob
		self.genotype_Length = n
		self.make_Random_Genotype(n)
		self.update_fitness()

	def __init__(self, n, mutation_prob, goal_string=None, genotype=None):
		self.goal_string = goal_string
		if self.goal_string==None:
			self.goal_string=[1]*n
		self.mutation_prob = mutation_prob
		self.genotype_Length = n
		self.genotype = genotype
		if (self.genotype == None):
			self.make_Random_Genotype(n)
		self.update_fitness()

	def __repr__(self):
		return str(self.fitness)

	### Function that: initialise a random list of 0s and 1s of length n
	#	Input:         int n: the length
	#   Outout:        Genotype
	def make_Random_Genotype(self, n):
		genotype = []
		for i in range(n):
			genotype.append(rng.randrange(0,2))
		self.genotype = genotype

	### Function that: make self.genotypetype based on the genotype
	#	Input:         
	#   Outout:        self.genotypetype
	def try_to_mutate(self):

		is_mutated = False

		# Iterate through all bits in the genotype
		for i in range(len(self.genotype)): 

			# try_to_mutate with probability prob
			if rng.random() < self.mutation_prob:
				if self.genotype[i] == 1: 
					self.genotype[i] = 0
				else: 
					self.genotype[i] = 1
				self.update_fitness()
				is_mutated = True
		return is_mutated

		#print(self.genotype)

	### Function that: Calculate the fitness of the indidual
	#	Input:         self.genotypetype
	#   Outout:        Fitness value in interval [0, 1]
	def update_fitness(self):
		#self.fitness = sum(self.genotype)/self.genotype_Length
		fit = 0
		for i in range(len(self.genotype)):
			if self.genotype[i] == self.goal_string[i]:
				fit += 1
		self.fitness = fit/self.genotype_Length
#
#
if __name__ == '__main__':
	individ = individual(20, 0.0005)
	print(individ.genotype)
	print('Fitness: ', individ.fitness,"\n")
	for i in range(10):
		if (individ.try_to_mutate()):
			print(individ.genotype)
			print('Fitness: ', individ.fitness,"\n")