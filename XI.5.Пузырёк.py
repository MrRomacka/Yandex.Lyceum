###
#N = int(input())

#List = [input() for i in range(int(input()))]

#for i in range(n - 1):
#    for j in range(n - 1 - i):
#        if List[j] > List[j + 1]:
#            List[j + 1], List[j] = List[j], List[j + 1]

#print(List)


N = int(input())

List = [input() for i in range(int(input()))]

for i in range(n - 1):
    for j in range(n - 1 - i):
        if len(List[j]) > len(List[j + 1]):
            List[j + 1], List[j] = List[j], List[j + 1]

print(List)
