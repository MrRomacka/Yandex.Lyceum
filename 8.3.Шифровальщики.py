letter = input()
cipher = []

for i in range(len(letter)):
    cipher.append(ord(letter[i]))

print(*cipher)