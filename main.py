import math
import numpy
import random

# The Simulated Annealing algorithm will receive all possible solutions
# computed by GLPK and find the best one for this instance of mTTP problem
#
# @param iterations - number of iterations until you consider the current solution as the best
# @param tempInitial - initial temperature (algorithm variable) (greater then @tempFinal) 
# @param tempFinal - final/maximum temperature (algorithm variable)
# @param alpha - temperature variability value (between 0.0 and 1.0) 
# @return bestPS - best solution found
def simulatedAnnealing(iterations, tempInitial, tempFinal, alpha):
	# initialize already computed solution list
	PS = []
	# start with a random solution and assume that it is the best
	actualPS = INITIAL
		# PS.append(actualPS)
	bestPS = actualPS
	# compute this solution and assume that it is the best
	actualDist = computeSolution(actualPS)
	bestDist = actualDist
	# iterations counter
	counter = 0
	while counter < iterations:
		print("Iteration: " + str(counter) + "; Optimal: " + str(bestDist))
		actualTemp = tempInitial
		finalTemp = tempFinal
		actualDist = bestDist
		actualPS = bestPS
		while actualTemp > finalTemp:
			_actualPS = generateNeighbour(actualPS, PS)
			_actualDist = computeSolution(_actualPS)
				# PS.append(_actualPS)
			delta = _actualDist - actualDist
			if(delta < 0 or math.exp(-delta / actualTemp) > random.random()):
				actualDist = _actualDist
				actualPS = _actualPS
				if(_actualDist < bestDist and verifySolution(actualPS)):
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

def generateRandomGames():
	notFound = True
	while notFound:
		firstRow = random.sample(range(teams), teams)
		permutes = random.sample(range(teams), teams)
		games = list(firstRow[i:] + firstRow[:i] for i in permutes)

		for k in range(teams):
			value = 0
			for e in range(teams):
				if(games[e][k] == value):
					value += 1
				else:
					break
			if(value == teams):
				notFound = False
				return numpy.delete(games, k, 1)


# This function receives a possible solution for the mTTP problem and
# return a random neighbour based on it
#
# @param S - a possible solution for this instance
# @param PS - a list of already computed solutions
# @return neighbour - a random neighbour of this solution
def generateNeighbour(S, PS):
	games, local = simplifySolution(S)
	if(bool(random.getrandbits(1))):
		games, local = changeGames(games, local)
	else:
		local = changeLocal(local, games)
	neighbour = unsimplifySolution(games, local)
	return neighbour

# This function receives a list of locals and randomize it
#
# @param games - a list of games
# @param games - a list of locals
# @return local - the same local list but randomized
def changeLocal(local, games):
	a = random.randrange(int(rounds/2))
	b1 = random.randrange(teams)
	b2 = games[b1][a]

	local[b1][a] = 1 - local[b1][a]
	local[b2][a] = 1 - local[b2][a]

	return local

# This function receives a list of games and randomize it
#
# @param games - a list of games
# @param games - a list of locals
# @return games, local - the same game list but randomized and with locals adapted
def changeGames(games, local):
	p = int(rounds/2)

	# Line Invert
	if(bool(random.getrandbits(1))):
		a = random.randrange(teams)
		b = random.randrange(teams)
		while b == a:
			b = random.randrange(teams)

		auxGames = numpy.zeros((teams, p), dtype=int)
		auxLocal = numpy.zeros((teams, p), dtype=int)
		for k in range(p):
			for e in range(teams):
				if(e == a):
					auxGames[a][k] = games[b][k]
					auxLocal[a][k] = local[b][k]
				elif(e == b):
					auxGames[b][k] = games[a][k]
					auxLocal[b][k] = local[a][k]
				else:
					auxGames[e][k] = games[e][k]
					auxLocal[e][k] = local[e][k]
				if(auxGames[e][k] == a):
					auxGames[e][k] = b
				elif(auxGames[e][k] == b):
					auxGames[e][k] = a
		return auxGames, auxLocal

	# Column Invert
	else:
		a = random.randrange(p)
		b = random.randrange(p)
		while b == a:
			b = random.randrange(p)
		
		auxGames = numpy.zeros((teams, p), dtype=int)
		auxLocal = numpy.zeros((teams, p), dtype=int)
		for k in range(p):
			for e in range(teams):
				if(k == a):
					auxGames[e][a] = games[e][b]
					auxLocal[e][a] = local[e][b]
				elif(k == b):
					auxGames[e][b] = games[e][a]
					auxLocal[e][b] = local[e][a]
				else:
					auxGames[e][k] = games[e][k]
					auxLocal[e][k] = local[e][k]
		return auxGames, auxLocal

# This two functions convert a solution schema to a simple representation of it
#
# @param S - a possible solution for this instance
# @return games, local - two matrix with the same information simplified
def simplifySolution(S):
	p = int(rounds/2)
	games = numpy.zeros((teams, p), dtype=int)
	local = numpy.zeros((teams, p), dtype=int)
	for k in range(p):
		for i in range(teams):
			for j in range(teams):
				if(i != j):
					if(S[i][j][k] + S[j][i][k] == 1):
						games[i][k] = j
						games[j][k] = i
						local[i][k] = S[j][i][k]
						local[j][k] = S[i][j][k]
	return games, local

# @param games, local - two matrix with a possible solution for this instance
# @return S - a matrix with the same information unsimplified
def unsimplifySolution(games, local):
	S = numpy.zeros((teams, teams, rounds), dtype=int)
	p = int(rounds/2)
	for k in range(p):
		for e in range(teams):
			e2 = games[e][k]
			S[e][e2][k] = 1 - local[e][k]
			S[e][e2][k+p] = local[e][k]
	return S

# This function receives a possible solution for the mTTP problem and
# return your respective Z
#
# @param S - a possible solution for this instance
# @return Z - the optimal value for this instance with this solution
def computeSolution(S):
	Z = 0
	for i in range(teams):
		for j in range(teams):
			Z += matches[i][j] * (S[i][j][0] + S[i][j][rounds-1])
	for k in range(1, rounds):
		for e in range(teams):
			for i in range(teams):
				for j in range(teams):
					Z += S[i][e][k-1] * S[j][e][k] * matches[i][j]
					Z += S[i][e][k-1] * S[e][j][k] * matches[i][e]
					Z += S[e][i][k-1] * S[j][e][k] * matches[e][j]
	return Z

# This sequence of functions verify if this solution is within the constraints
#
# @param S - a possible solution for this instance
# @return result - the verification result
def verifySolution(S):
	result = verifyConstraint1(S)
	result = result and verifyConstraint2(S)
	result = result and verifyConstraint3(S)
	result = result and verifyConstraint4And5(S)
	result = result and verifyConstraint6(S)
	result = result and verifyConstraint7(S)
	return result

def verifyConstraint1(S):
	for k in range(rounds):
		for i in range(teams):
			for j in range(teams):
				if(S[i][j][k] * S[j][i][k] != 0):
					return False
	return True

def verifyConstraint2(S):
	for k in range(rounds):
		for i in range(teams):
			sum = 0
			for j in range(teams):
				sum += S[i][j][k] + S[j][i][k]
			if(sum != 1):
				return False
	return True

def verifyConstraint3(S):
	for i in range(teams):
		for j in range(teams):
			if(i != j):
				sum = 0
				for k in range(int(rounds/2)):
					sum += S[i][j][k] + S[j][i][k]
				if(sum != 1):
					return False
	return True

def verifyConstraint4And5(S):
	for k in range(rounds-3):
		for j in range(teams):
			sum = 0
			for i in range(teams):
				sum += S[i][j][k] + S[i][j][k+1] + S[i][j][k+2] + S[i][j][k+3]
			if(sum < 1 or sum > 3):
				return False
	return True

def verifyConstraint6(S):
	p = int(rounds/2)
	for k in range(p):
		for i in range(teams):
			for j in range(teams):
				if(i != j):
					cond1 = S[i][j][k] * (S[i][j][k+p]-1)
					cond2 = S[j][i][k] * (S[j][i][k+p]-1)
					cond3 = -(-((1-S[i][j][k]) * (1-S[j][i][k])) * -((1-S[i][j][k+p]) * (1-S[j][i][k+p])))
					if(cond1 + cond2 + cond3 != -1):
						return False
	return True

def verifyConstraint7(S):
	p = int(rounds/2)
	for k in range(p):
		for i in range(teams):
			for j in range(teams):
				if(i != j):
					cond1 = (S[i][j][k]-1) * S[j][i][k] * S[i][j][k+p]
					cond2 = (S[j][i][k]-1) * S[i][j][k] * S[j][i][k+p]
					cond3 = -(-((1-S[i][j][k]) * (1-S[j][i][k])) * -((1-S[i][j][k+p]) * (1-S[j][i][k+p])))
					if(cond1 + cond2 + cond3 != -1):
						return False
	return True


################################################################################



instance = "circ8"

# Get initial parameters
matches = []
with open("instancias/" + instance + ".txt", 'r') as f:
    matches = [[int(num) for num in line.split()] for line in f]
matches = numpy.array(matches)
teams = len(matches)
rounds = 2*teams - 2

gamesInit = []
localInit = []
with open("entradas/len" + str(teams) + ".txt", 'r') as f:
    gamesInit = [[int(num.split(',')[0]) for num in line.split()] for line in f]
with open("entradas/len" + str(teams) + ".txt", 'r') as f:
	localInit = [[int(num.split(',')[1]) for num in line.split()] for line in f]
gamesInit = numpy.array(gamesInit)
localInit = numpy.array(localInit)

# Print them
print("teams = " + str(teams))
print("rounds = " + str(rounds))
print("matches = \n" + str(matches))
print("gamesInit = \n" + str(gamesInit))
print("localInit = \n" + str(localInit))

INITIAL = unsimplifySolution(gamesInit, localInit)
if(verifySolution(INITIAL)):
	print("#### VALID INSTANCE ####")
else:
	print("#### INVALID INSTANCE : BE CAREFULL ####")

bestSolution = simulatedAnnealing(200, 200, 20, 0.5)
Z = computeSolution(bestSolution)
print("Solution = \n" + str(bestSolution))
print("Z = " + str(Z))

gamesEnd, localEnd = simplifySolution(bestSolution)
print("games = \n" + str(gamesEnd))
print("local = \n" + str(localEnd))