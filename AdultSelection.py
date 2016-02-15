### Function that: is run from EA loop. 
###                Bool chooses which selection alg is to be used.
#   Input:         list of children and parents and bool for each alg
#   Output:        list of new parents
def Adult_Selection(A1, A2, A3, children, parents):
	if A1: 
		print("Full_Replacement")
		return Full_Replacement(children, parents)
	elif A2:
		print("Over_Production")
		return Over_Production(children, parents)
	else:
		print("Generational_Mixing")
		return Generational_Mixing(children, parents)


### Function that: replace all adults with new children
#   Input:         list of children and parents
#   Output:        list of new parents
def Full_Replacement(children, parents):
	return children


### Function that: replace all adults with new children.
###                But not all children can become adults
#   Input:         list of children and parents
#   Output:        list of new parents
def Over_Production(children, parents):
	pass


### Function that: mix parents and children.
#   Input:         list of children and parents
#   Output:        list of new parents
def Generational_Mixing(children, parents):
	pass
