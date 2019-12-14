import random
a = random.randint(1,100)
count = 0
while a !=1:
    print('Ха-ха. Ты попался в Ловушку Джокера!')
    a = random.randint(1, 100)
    count = count + 1

print('End! You won!')
print (count)

