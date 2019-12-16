#str = input().split()
#for elem in str[2::3]:
    #print(elem, sep=' ')

print(*(elem for elem in input().split()[2::3]), sep=' ')