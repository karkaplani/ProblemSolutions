#https://projecteuler.net/problem=53
def factoriel(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

def combination(a,b):
    return factoriel(a)/(factoriel(b)*factoriel(a-b))
    
result = 0
for i in range(1,101):
    for j in range(1,101):
        if(combination(i,j) > 1000000):
            result += 1

print(result)    