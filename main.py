matches = []
with open('instancias/N8.txt', 'r') as f:
    matches = [[int(num) for num in line.split()] for line in f]

numEquipes = len(matches)
print("numEquipes = " + str(numEquipes))

print("matches = [")
for x in range(numEquipes):
	for y in matches[x]:
		print('{:4d}'.format(y), end=", ")
	print("")
print("]")





