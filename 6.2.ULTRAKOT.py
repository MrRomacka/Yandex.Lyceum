N = int(input())
result = 'Нет'

for i in range(N):
    finding = input()
    if "кот" in finding.lower():
        result = "МЯУ"
    elif "пёс" in finding.lower():
        result = 'НЕТ'

print(result)