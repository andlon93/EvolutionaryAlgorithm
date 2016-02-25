import random as rng
import numpy as np
import matplotlib.pyplot as plt
import OneMax as OM
import LOLZ
import SurprisingSequences as SS
import AdultSelection as AS
import ParentSelection as PS
import Crossover as C
###
def find_best_individual(gen):
	best_fitness = -1
	best_individual = None
	for individual in gen:
		if individual.fitness > best_fitness:
			best_individual = individual
			best_fitness = individual.fitness
	return best_individual

def calculate_avg_std(survivors):

	# --- Calculate average fitness.
	avg_fitness = 0
	for survivor in survivors:
		avg_fitness += survivor.fitness
	avg_fitness = avg_fitness/len(survivors)

	# --- Calculate standard deviation of fitness.
	std_fitness = 0
	for survivor in survivors:
		std_fitness += (survivor.fitness - avg_fitness)**2
	std_fitness = np.sqrt(std_fitness/(len(survivors)-1))

	return avg_fitness, std_fitness
#
def EA_Loop(scaling, p_selection, adult_alg, Choose_problem, z, s, pop_size, generation_limit, NSplits, Crossover_rate, mutation_rate, bit_length):
	# Initialise first child pool. mutate to pheno. fitness calc.

	# --- Initialise population with random candidate solutions.
	children = []
	survivors = []
	parents = []

	if Choose_problem==0:
		print("Solving the One Max problem")
		goal=None
		for i in range(pop_size):
 			survivors.append(OM.individual(bit_length, mutation_rate, goal))
	elif Choose_problem==1:
		#print("Solving the LOLZ-prefix problem")
		for i in range(pop_size):
			survivors.append(LOLZ.individual(bit_length, z, mutation_rate))
	elif Choose_problem==2:
		print("Solving Locally Surprising Sequences")
		for i in range(pop_size*10):
			survivors.append(SS.individual(bit_length, s, mutation_rate, False))
	else:
		print("Solving Globally Surprising Sequences")
		for i in range(pop_size):
			survivors.append(SS.individual(bit_length, s, mutation_rate, True))

	# --- Initialize generation count.
	Ngenerations = 1

	# --- Find best individual in population.
	best_individual = find_best_individual(survivors)

	# Plot the best score in each generation
	plotting = [best_individual.fitness]
	plotting2 = [calculate_avg_std(survivors)[0]]
	#print("#", Ngenerations, " --- Best individual:\n", "Fitness: ", best_individual.fitness, "Genotype: ", best_individual.genotype)

	# --- Run as long as the best individual has fitness below 1.
	while (best_individual.fitness < 1.0 and Ngenerations < generation_limit):

		# --- Update generation count.
		Ngenerations += 1

		# --- Make N children from the survivors of the previous generation.
		#     Select parents.
		#     Recombine pairs of parents.
		#     Mutate the resulting offspring.
		#print("Generation: ", Ngenerations)
		children = C.make_children(Choose_problem, survivors, pop_size, NSplits, Crossover_rate, p_selection, scaling)
		#print("children made")
		# --- Select individuals for the next generation.
		#     N of the best individuals survive (fitness biased).
		survivors = adult_alg(children, parents, pop_size)

		# --- Calculate average fitness and standard deviation of fitness.
		avg_fitness, std_fitness = calculate_avg_std(survivors)

		# --- Find best individual in population.
		best_individual = find_best_individual(survivors)

		# --- For plotting
		plotting.append(best_individual.fitness)
		#plotting2.append(calculate_avg_std(survivors)[0])

		# --- Logging.	
		if Ngenerations%50==0: print("#", Ngenerations, "\nBest individual --- ", "Fitness: ", best_individual.fitness, "Genotype: ", best_individual.genotype, "\nAverage of fitness: ", avg_fitness, ". Standard deviation of fitness: ", std_fitness, ".\n")
		if best_individual.fitness == 1.0: print("#", Ngenerations, "\t Best individual is optimized!")
	#
	print("#", Ngenerations, "\nBest individual --- ", "Fitness: ", best_individual.fitness, "Genotype: ", best_individual.genotype)
	#if Choose_problem>1: print("Fitness: ",best_individual.fitness,"\nSequence: ", best_individual.genotype)
	if (best_individual.fitness == 1.0): return Ngenerations, True, plotting, plotting2
	else: return Ngenerations, False, plotting, plotting2
	#return Ngenerations
#
def main(Choose_problem, bit_length, z, s, pop_size, Crossover_rate, mutation_rate, adult_alg, parent_alg, scaling):
	#Choose_problem = 3 # 0==OneMax, 1==LOLZ, 2==LocalSS, 3==GlobalSS
	#adult_alg = 0 # 0==full repl., 1==over prod., 2==Gen. mixing 
	#parent_alg = 0 # 0==Global, 1==tournament
	#scaling = 3 # 0==fitness_prop, 1==sigma, 2==boltzmann, 3==rank
	#
	#z = 21
	#s = 15
	#
	N = 1
	sum_generations = 0
	std_generations = 0
	Nfails = 0
	#
	gen_limit = 100000
	#pop_size = 230
	NSplits = 5
	#Crossover_rate = 0.8
	#mutation_rate = 0.0001
	#bit_length = 37
	#
	#
	#plotting=[[]]*100
	#
	for i in range(N):
		if adult_alg==0:
			if parent_alg==0:
				if scaling==0:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.fitness_proportionate_scaling , PS.Global_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
				elif scaling==1:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.sigma_scaling , PS.Global_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
				elif scaling==2:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.boltzmann_scaling , PS.Global_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
				else:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.rank_scaling , PS.Global_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
			else:
				if scaling==0:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.fitness_proportionate_scaling , PS.Tournament_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
				elif scaling==1:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.sigma_scaling , PS.Tournament_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
				elif scaling==2:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.boltzmann_scaling , PS.Tournament_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
				else:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.rank_scaling , PS.Tournament_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
		elif adult_alg==1:
			if parent_alg==0:
				if scaling==0:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.fitness_proportionate_scaling , PS.Global_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
				elif scaling==1:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.sigma_scaling , PS.Global_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
				elif scaling==2:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.boltzmann_scaling , PS.Global_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
				else:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.rank_scaling , PS.Global_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
			else:
				if scaling==0:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.fitness_proportionate_scaling , PS.Tournament_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
				elif scaling==1:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.sigma_scaling , PS.Tournament_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
				elif scaling==2:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.boltzmann_scaling , PS.Tournament_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
				else:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.rank_scaling , PS.Tournament_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
		else:
			if parent_alg==0:
				if scaling==0:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.fitness_proportionate_scaling , PS.Global_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
				elif scaling==1:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.sigma_scaling , PS.Global_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
				elif scaling==2:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.boltzmann_scaling , PS.Global_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
				else:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.rank_scaling , PS.Global_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
			else:
				if scaling==0:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.fitness_proportionate_scaling , PS.Tournament_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
				elif scaling==1:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.sigma_scaling , PS.Tournament_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
				elif scaling==2:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.boltzmann_scaling , PS.Tournament_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
				else:Ngenerations, isDone, plots, plots2 = EA_Loop(PS.rank_scaling , PS.Tournament_Selection, AS.Full_Generational_Replacement, Choose_problem, z, s, pop_size, gen_limit, NSplits, Crossover_rate, mutation_rate, bit_length)
		if not isDone:Nfails += 1
		sum_generations += Ngenerations
		std_generations += (Ngenerations - sum_generations/(i+1))**2
		#if i%50==0:
		#	print("\nRuns: ", i+1)
		#	print("Number of fails: ", Nfails)
		#for i in range(len(plots)):
		#	plotting[i].append(plots[i])
	# --- Logging data for all the generations.
	#print('Average number of generations = ', sum_generations/N, ' Standard deviation of number of generations ~ ', np.sqrt(std_generations/(N-1)))
	#print('#fails: ', Nfails, ' / ', i+1, ' = ', Nfails/(i+1)*100, '%\n')
	return plots


	# --- Plotting
	'''plt.plot(range(1,len(plots)+1), plots, label='best individual')
	plt.plot(range(1,len(plots2)+1), plots2, label='average in population')
	plt.legend(loc='lower right')
	plt.xlabel('Number of generations')
	plt.ylabel('Fitness')
	plt.axis([0, len(plots), 0, 1])
	plt.show()'''
#
def run():
	not_done="1"
	while not_done=="1":
		z=0
		s=0
		print("Choose problem: 0=One Max, 1=LOLZ, 2=localSS, 3=globalSS")
		problem=input("input int: ")
		if problem=="0":
			bit_size = input("input bit length: ")
		if problem=="1":
			bit_size = input("input bit length: ")
			z=input("Z: ")
		elif problem == "2" or problem == "3":
			s=input("S: ")
			bit_size=input("L: ")
		pop_size=input("Population Size: ")
		Crossover_rate=input("Crossover rate: ")
		mutation_rate=input("Mutation rate: ")
		#
		print("Choose adult alg: 0=full repl., 1=over prod., 2=gen. mixing")
		adult_alg=input("input int: ")
		#
		print("parent selection: 0=tournament, 1=fitness prop., 2=sigma, 3=rank")
		p_select=input("input int: ")
		if p_select=="0":
			parent_alg=1
			scaling=0
		elif p_select=="1":
			parent_alg=0
			scaling=0
		elif p_select=="2":
			parent_alg=0
			scaling=1
		else:
			parent_alg=0
			scaling=3
		
		main(int(problem), int(bit_size), int(z), int(s), int(pop_size), float(Crossover_rate), float(mutation_rate), int(adult_alg), int(parent_alg), int(scaling))

		not_done=input("Do you wish to continue(1/0)? ")
		#
#
if __name__ == '__main__':
	#Crossover_rate = 0.8
	#mutation_rate = 0.0001
	#print("\n--- Tournament: eps:0.05 k=64")
	#s=main()
	#print("Global.\nS:15 bit:37")
	run()
	'''j=1
	temp=[]
	for mnb in range(j):
		p=main(1,0)
		print("tournament: ", mnb)
		temp.append(p)
	p1=[]
	for i in range(100):
		for n in range(j):
			s=0.0
			t=0.0
			#print(len(temp[n]), i)
			if len(temp[n]) > i:
				s+=temp[n][i]
				t+=1.0
		if (t>0.0): 
			#print("append")
			p1.append( s/t )
	print("en ferdig----------------------------------------------------------------------------------------------")
	temp=[]
	for mnb in range(j):
		p=main(0,0)
		print("fitness prop: ", mnb)
		temp.append(p)
	p2=[]
	for i in range(100):
		for n in range(j):
			s=0.0
			t=0.0
			if len(temp[n]) > i:
				s+=temp[n][i]
				t+=1.0
		if (t>0.0): 
			p2.append( s/t )
	#
	print("to ferdig----------------------------------------------------------------------------------------------")
	temp=[]
	for mnb in range(j):
		p=main(0,1)
		print("Sigma: ", mnb)
		temp.append(p)
	p3=[]
	for i in range(100):
		for n in range(j):
			s=0.0
			t=0.0
			if len(temp[n]) > i:
				s+=temp[n][i]
				t+=1.0
		if (t>0.0): 
			p3.append( s/t )

	#temp=[]
	#for mnb in range(j):
#		p=main(0,2)
#		temp.append(p)
#	p4=[]
#	for i in range(100):
#		for n in range(j):
#			s=0.0
#			t=0.0
###				t+=1.0
	#	if (t>0.0): 
	#		p4.append( s/t )
	print("tre ferdig----------------------------------------------------------------------------------------------")
	temp=[]
	for mnb in range(j):
		p=main(0,3)
		print("Rank: ", mnb)
		temp.append(p)
	p5=[]
	for i in range(100):
		for n in range(j):
			s=0.0
			t=0.0
			if len(temp[n]) > i:
				s+=temp[n][i]
				t+=1.0
		if (t>0.0):
			p5.append( s/t )
	#
	plt.plot(range(1,len(p1)+1), p1, label='Tournament')
	plt.plot(range(1,len(p2)+1), p2, label='Fitness proportionate')
	plt.plot(range(1,len(p3)+1), p3, label='Sigma scaling')
	#plt.plot(range(1,len(p4)+1), p4)#, label='Boltzmann scaling')
	plt.plot(range(1,len(p5)+1), p5, label='Rank scaling')
	#plt.plot(range(1,len(p6)+1), p6)#, label='Rank scaling')
	#plt.plot(range(1,len(p7)+1), p7)#, label='Rank scaling')
	#plt.plot(range(1,len(p8)+1), p8)#, label='Rank scaling')
	plt.legend(loc='lower right')
	plt.xlabel('Number of generations')
	plt.ylabel('Fitness')
	plt.axis([0, 100, 0.95*min(p1[0],p2[0],p3[0],p5[0]), 1.05])
	plt.show()'''

	'''pop_size = 220
	while pop_size < 300: 
		print("\n--- Population size: ",pop_size)
		pop_size += 20'''