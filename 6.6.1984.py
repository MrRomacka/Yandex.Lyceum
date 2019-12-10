war = "Евразия"
peace = "Остазия"
N = int(input())

for i in range(N):
    question = input()
    if "война" in question.lower():
        print(war)
    elif "мир" in question.lower():
        print(peace)
    elif "меняем" in question.lower():
        war, peace = peace, war