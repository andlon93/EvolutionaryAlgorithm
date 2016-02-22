#from __future__ import division
import random as rng
#
class individual:
	genotype_Length = 0
	mutation_prob = 0
	genotype = []
	fitness = 0
	s = 0
	normalised_fitness = 0
	isGlobal = None
	### Constructor
	def __init__(self, n, m, mutation_prob, isGlobal, genotype=None):
		self.mutation_prob = mutation_prob
		self.genotype_Length = n
		self.genotype = genotype
		self.s = m
		if (self.genotype == None): self.make_Random_Genotype(n, m)
		self.isGlobal = isGlobal
		self.update_fitness()
	#
	def __repr__(self): return str(self.fitness)
	#
	### Function that: initialise a random list of length n, containing lists of 0s and 1s of length m
	#	Input:         int n: the length the list, int m: the length of each element in the list
	#   Outout:        Genotype
	def make_Random_Genotype(self, n, m):
		genotype=[]
		for i in range(n): genotype.append(rng.randint(0,m-1))
		self.genotype=genotype
	#
	### Function that: tries to mutate a bit with a given prob
	def try_to_mutate(self):
		isMutated = False
		for n in range(len(self.genotype)):
			if rng.random() < self.mutation_prob:
				isMutated = True
				old_value = self.genotype[n]
				while self.genotype[n]==old_value:
					self.genotype[n]=rng.randint(0,self.s-1)
		if isMutated: 
			self.update_fitness()
		return isMutated
	#
	### Function that: Calculate the fitness of the indidual
	#	Input:         self.genotypetype
	#   Outout:        Fitness value in interval [0, 1]
	def update_fitness(self):
		if self.isGlobal:
			#print("regner global")
			self.global_fitness()
		else:
			self.local_fitness()
	def global_fitness(self):
		all_sets = []
		E=0
		for i in range(0, len(self.genotype)-1):
			#print("Genom: ", self.genotype)
			mellomrom=0
			for n in range(i+1,len(self.genotype)):
				temp=[self.genotype[i],mellomrom,self.genotype[n]]
				#print("all_sets: ",all_sets)
				#print("Temp: ", temp)
				if temp not in all_sets:
					all_sets.append(temp)
				else:
					E+=1
					#print("PLUSSER paa E")
				mellomrom+=1
			#print("\n")
		#print("E:",E," -- 1 delt paa 1 +",E," er:",(1/(1+float(E))))
		self.fitness=1/(1+E)
	#
	def local_fitness(self):
		all_sets = [[self.genotype[0],self.genotype[1]]]
		E=0
		for i in range(2, len(self.genotype)):
			temp=[self.genotype[i-1],self.genotype[i]]
			#print("all_sets: ",all_sets)
			#print("Temp: ", temp)
			if temp not in all_sets: 
				all_sets.append(temp)
			else: 
				E+=1
				#print("plusser på E")
			#print("\n")
		#print("E:",E," -- 1 delt paa 1 +",E," er:",(1/(1+float(E))))
		self.fitness=1/(1+E)
if __name__ == '__main__':
	i = individual(6, 3, 0.001, True)
	print(i.genotype)
	#print(i.phenotype)
	print(i.fitness)