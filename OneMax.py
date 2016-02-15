import random as rng

class individual:
	fitness = 0
	genotype = []
	phenotype = []

	def __init__(self, n):
		self.genotype = self.makeRandomInit(n)


	### Function that: initialise a random list of 0s and 1s of length n
	#	Input:         int n: the length
	#   Outout:        The list of length n.
	def makeRandomInit(self, n):
		genotype = []
		for i in range(n):
			genotype.append(rng.randrange(0,2))
		return genotype



if __name__ == '__main__':
	individ = individual(20)
	print(individ.genotype)