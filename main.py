import random
import math

# Get initial parameters
matches = []
with open('instancias/N4.txt', 'r') as f:
    matches = [[int(num) for num in line.split()] for line in f]

# Print them
numEquipes = len(matches)
print("numEquipes = " + str(numEquipes))

print("matches = [")
for x in range(numEquipes):
	for y in matches[x]:
		print('{:4d}'.format(y), end=", ")
	print("")
print("]")

# The Simulated Annealing algorithm will receive all possible solutions
# computed by GLPK and find the best one for this instance of mTTP problem
#
# @param iterations - number of iterations until you consider the current solution as the best
# @param tempInitial - initial temperature (algorithm variable) (greater then @tempFinal) 
# @param tempFinal - final/maximum temperature (algorithm variable)
# @param alpha - temperature variability value
# @return bestPS - best solution found
def simulatedAnnealing(iterations, tempInitial, tempFinal, alpha):
	# start with a random solution and assume that it is the best
	actualPS, bestPS = random.choice(PS)
	# compute this solution and assume that it is the best
	actualDist, bestDist = computeSolution(actualPS)
	# iterations counter
	counter = 0
	while counter < iterations:
		actualTemp = tempInitial
		finalTemp = tempFinal
		actualDist = bestDist
		actualPS = bestPS
		while actualTemp > finalTemp:
			_actualPS = chooseNeighbour(actualPS, PS)
			_actualDist = computeSolution(_actualPS)
			delta = _actualDist - actualDist
			if(delta < 0 or math.exp(-delta / actualTemp) > random.random()):
				actualDist = _actualDist
				actualPS = _actualPS
				if(_actualDist < bestDist):
					bestDist = actualDist
					bestPS = actualPS
			actualTemp *= alpha
		counter += 1
	return bestPS

# This function generates a random valid solution for the mTTP problem
#
# @return S - a random possible solution for this instance
def generateRandomSolution():
	S = None
	return S

# This function receives a possible solution for the mTTP problem and
# return a random neighbour based on it
#
# @param S - a possible solution for this instance
# @return neighbour - a random neighbour of this solution
def chooseNeighbour(S):
	neighbour = None
	return neighbour

# This function receives a possible solution for the mTTP problem and
# return your respective Z
#
# @param S - a possible solution for this instance
# @return Z - the optimal value for this instance with this solution
def computeSolution(S):
	Z = 0
	return Z
