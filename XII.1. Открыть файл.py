file_name = 'Duck.txt'
file_in = open(file_name, 'r')

lst = [int(elem) for elem in file_in.read().split()]
print(lst)

file_in.close()

file_suck = 'Suck.txt'
with open(file_suck, 'r') as file_in:
    lst = [int(elem) ** 2 for elem in file_in.read().split()]
    print(lst)

lstt = []
with open('Duck.txt') as file_uh:
    for elem in lstt:
        # file_uh.write(str(elem) + '\n')
        print(elem, file=file_uh)

