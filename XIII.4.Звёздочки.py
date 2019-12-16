#Str = input().split()
#for x in Str:
    #print("*" * int(x))

print(*['*' * int(elem) for elem in input().split()], sep='\n')