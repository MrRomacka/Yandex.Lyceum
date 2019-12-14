N = int(input())
List = []
for i in range(N):
    List.append(input())
ListN2 = [elem for elem in List if elem[-1] == '5' or elem[-1] == '4']

print(*List, '', *ListN2, sep='\n')