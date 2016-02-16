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
### Function that: replace all adults with new children
#   Input:         list of children and parents
#   Output:        list of new parents
#def Full_Replacement(children):
#	return children
#
#
### Function that: replace all adults with new children.
###                But not all children can become adults
#   Input:         list of children and parents
#   Output:        list of new parents
def Over_Production(children, number_of_parents):
	new_parents = []
	for new_parent in range(number_of_parents):
		strongest = None
		index = None
		for i in range(len(children)):
			if (strongest == None or strongest.fitness < children[i].fitness):
				strongest = children[i]
				index = i
		new_parents.append(strongest)
		children.pop(index)
	return new_parents
#
#
### Function that: mix parents and children.
#   Input:         list of children and parents
#   Output:        list of new parents
def Generational_Mixing(children, parents):
	pass

if __name__ == '__main__':
	children = []
	n=50
	for n in range(n):
		children.append(OM.individual(20, 0.05))
		print(children[-1].fitness)
	print("\n",len(children),"\n")
	new_parents = Over_Production(children, 20)
	print("\n",len(new_parents),"\n")
	for parent in new_parents:
		print(parent.fitness)