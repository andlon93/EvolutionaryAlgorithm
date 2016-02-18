import random as rng
import copy
import OneMax as OM
import AdultSelection as AS
import ParentSelection as PS
import Crossover
###
def find_best_individual(gen):
	best_fitness = -1
	best_individual = None
	for individual in gen:
		if individual.fitness > best_fitness:
			best_individual = individual
			best_fitness = individual.fitness
	return best_individual

def EA_Loop(pop_size, Adult_size, Parent_size, children_size):
	# Initialise first child pool. mutate to pheno. fitness calc.
	children = []
	parents = []
	adults = []

	# --- Generate a population of pop_size children.
	for i in range(pop_size):
		children.append(OM.individual(20, 0.0005))

	Ngenerations = 1

	# --- Find best individual in population.
	best_individual = find_best_individual(children)
	print("#", Ngenerations, " --- Best individual:\n", "Fitness: ", best_individual.fitness, "Genotype: ", best_individual.genotype)


	# --- Run as long as the best individual has fitness below 1.
	while (best_individual.fitness < 1.0 and Ngenerations < 1000):
		Ngenerations += 1
		
		# --- Select N of the best individuals to be adults.
		adults = AS.Generational_Mixing(children+adults, Adult_size)

		# --- Make N children from the adults.
		children = Crossover.make_children(adults, children_size)

		best_individual = find_best_individual(children+adults)
		if Ngenerations%1==0:
			avg_fitness = 0
			isEqual=True
			temp = children[0].genotype
			for child in children:
				avg_fitness = avg_fitness + child.fitness/len(children)
				if temp != child.genotype:
					isEqual = False
			#print("isEqual: ", isEqual)
			#print("\n\n")
			print("#", Ngenerations, " --- Best individual:\n", "Fitness: ", best_individual.fitness, "Genotype: ", best_individual.genotype)
			print("Average fitness: ", avg_fitness)
#
#EA_Loop(100, 50, 50, 50)
EA_Loop(20, 10, 5, 20)