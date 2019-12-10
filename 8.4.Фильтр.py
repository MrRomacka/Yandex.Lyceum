N = int(input())

for i in range(N):
    string = input()
    if string.find('####') == 0:
        continue
    else:
        string = string.replace("%%", "")
    print(string)