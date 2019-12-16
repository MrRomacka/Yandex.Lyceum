""""
str = input().split()
summ = 0
buf = input().split()
m, k = int(buf[0]), int(buf[1])
for elem in str[m:k + 1]:
    summ += int(elem)
print(summ)

"""

lst = [int(x) for x in input().split()]
m, k = [int(y) for y in input().split()]
print(sum(lst[m:k + 1]))