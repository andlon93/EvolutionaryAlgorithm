import copy

# --- Function:  
#     All adults from the previous generation are removed,
#     and all children gain free entrance to the adult pool.
#     Input:         list of children
#     Output:        list of new adults
def Full_Generational_Replacement(children, N):

	# --- Returns all children if #children = #population.
	if(len(children) == N):
		return children

	# --- Selects the N individuals with the best fitness.
	return sorted(children, key=lambda individual: individual.fitness)[len(children)-N:]
#
#
# --- Function:  
#     All previous adults die, but m (the maximum size of the
#     adult pool) is smaller than n (the number of children).
#     Hence, the children must compete among themselves for the 
#     m adult spots, so selection pressure is signiﬁcant. 
#     Input:         list of children
#     Output:        list of new adults
def Over_Production(children, N):

	# --- Selects the N individuals with the best fitness.
	return sorted(children, key=lambda individual: individual.fitness)[len(children)-N:]
#
#
# --- Function:  
#     The m adults from the previous generation do not die, so 
#     they and the n children compete in a free-for-all for the 
#     m adult spots in the next generation. Selection pressure 
#     on juveniles is extremely high, since they are competing
#     with some of the best individuals that have evolved so far.
#     Input:         list of children and parents
#     Output:        list of new adults
def Generational_Mixing(children, adults, N):

	# --- Selects the N individuals with the best fitness.
	return sorted(children + adults, key=lambda individual: individual.fitness)[len(children + adults)-N:]

if __name__ == '__main__':
	# TESTING THE METHODS ABOVE
	import OneMax as OM
	children = []
	parents = []
	n=50
	for n in range(n):
		children.append(OM.individual(20, 0.05))
		parents.append(OM.individual(20, 0.05))
		print(children[-1].fitness)
	print("\n",len(children),"\n")
	print("\n",len(parents),"\n")
	#new_parents = Over_Production(children, 20)
	new_parents = Generational_Mixing(children, parents, 20)
	print("\n",len(new_parents),"\n")
	for parent in new_parents:
		print(parent.fitness)