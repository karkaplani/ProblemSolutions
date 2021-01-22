#https://projecteuler.net/problem=15
#It will reach the end by going 20 unit right, and 20 to bottom
#The formula is overall!/right!*bottom!
overall = 40
oneSide = 20
fOverall = 1
fOneSide = 1

for i in range(1, overall+1):
	fOverall *= i

for i in range(1, oneSide+1):
	fOneSide *= i

result = fOverall/(fOneSide*fOneSide)
print(result)