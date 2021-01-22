#https://projecteuler.net/problem=20
num = 100
afterFactorial = 1

for i in range(1, num+1):
	afterFactorial *= i

digitCount = len(str(afterFactorial))
sum = 0
divider = 10
divider2 = 1

for i in range(1, digitCount+1):
	sum += ((afterFactorial%divider)-(afterFactorial%divider2))/divider2
	divider *= 10
	divider2 *= 10

print(sum)