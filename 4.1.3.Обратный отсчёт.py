n = int(input())

for i in range(n+1):
    print('Осталось секунд %i' %(n-i))
print('Пуск!', "\n")
for i in reversed(range(n+1)):
    print('Осталось секунд %i' %(i))
print('Пуск!', "\n")