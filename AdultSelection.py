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


# GAMMEL KODE:

### Function that: is run from EA loop. 
###                Bool chooses which selection alg is to be used.
#   Input:         list of children and parents and bool for each alg
#   Output:        list of new parents
'''def Adult_Selection(A1, A2, A3, children, parents, number_of_parents):
	# Full replacement. All parents die and all children become parents
	if A1: 
		print("Full_Replacement")
		return children
		#return Full_Replacement(children)
	# Over production. all parents die. some children become parents
	elif A2:
		print("Over_Production")
		return Over_Production(children, number_of_parents)
	# Mix of parents and children become parents
	else:
		print("Generational_Mixing")
		return Generational_Mixing(children, parents, number_of_parents)'''
#
#
'''### Function that: replace all adults with new children
#   Input:         list of children and parents
#   Output:        list of new parents
#def Full_Replacement(children):
#	return children
#
#'''
### Function that: replace all adults with new children.
###                But not all children can become adults
#   Input:         list of children and parents
#   Output:        list of new parents
'''def Over_Production(children, number_of_parents):
	# A list of the new parents for this generation
	new_parents = []

	#Iterate through all new parents.
	for new_parent in range(number_of_parents):
		strongest = None
		index = None

		# Pick the strongest child
		for i in range(len(children)):
			if (strongest == None or strongest.fitness < children[i].fitness):
				strongest = children[i]
				index = i

		# Add strongest child to new parents
		new_parents.append(strongest)

		#Remove strongest child from children so it wont be chosen again.
		children.pop(index)

	# Return the list containing the new parents
	return new_parents'''
#
#