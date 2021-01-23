#https://projecteuler.net/problem=28
#In the pattern, numbers' increasing ratio increases by 2 in every 4th element
endNum = 1001*1001
sum = 1
accel = 2
counter = 1

i = 3
while i < endNum+1:
    sum += i
    i += accel
    counter += 1
    if counter%4==0:
        accel += 2
     
print(sum)   