#https://projecteuler.net/problem=30
def findSum(num):
    num = str(num)
    digitLength = len(num)
    sum = 0
    for i in range(0,digitLength):
        sum += int(num[i])**5
    return sum
    
sum = 0    
for i in range(2,300000): #I tried by giving different values
    if i == findSum(i):
        sum += i
        
print(sum)