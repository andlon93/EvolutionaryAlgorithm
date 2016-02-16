import OneMax as OM

### Function that: is run from EA loop. 
###                Bool chooses which selection alg is to be used.
#   Input:         list of children and parents and bool for each alg
#   Output:        list of new parents
def Adult_Selection(A1, A2, A3, children, parents, number_of_parents):
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
		return Generational_Mixing(children, parents, number_of_parents)
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
def Over_Production(children, number_of_parents):
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
	return new_parents
#
#
### Function that: mix parents and children.
#   Input:         list of children and parents
#   Output:        list of new parents
def Generational_Mixing(children, parents, number_of_parents):
	# A list of the new parents for this generation
	new_parents = []

	#Iterate through all new parents.
	for new_parent in range(number_of_parents):
		strongest = None
		index = None
		isChild = False

		#Find the strongest of all children and parents
		for i in range(len(children)):
			if (strongest == None or strongest.fitness < children[i].fitness):
				strongest = children[i]
				index = i
				isChild = True
		for i in range(len(parents)):
			if (strongest == None or strongest.fitness < parents[i].fitness):
				strongest = parents[i]
				index = i
				isChild = False
		# Add strongest individual to new parents
		new_parents.append(strongest)
		
		#Remove indidual from its list
		if isChild == True: children.pop(index)
		else: parents.pop(index)

	# Return the new parents
	return new_parents

if __name__ == '__main__':
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