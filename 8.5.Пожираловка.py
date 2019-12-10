string = input()
print(string)
while len(string) > 2:
    string = string.replace(string[-1], "")
    string = string.replace(string[0], "")
    print(string)