N = int(input())

numbers = []

for i in range(N):
    numbers.append(input())

begin = int(input())
end = int(input())
summary = 0

for j in range(begin - 1, end):
    summary += int(numbers[j])

print(summary)