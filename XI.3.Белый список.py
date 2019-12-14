WhitePower = int(input())
WhiteList = []
for i in range(WhitePower):
    WhiteList.append(input())

Number = int(input())
Requests = []
for k in range(Number):
    Quest = input()
    if Quest in WhiteList:
        Requests.append(Quest)

print(*Requests, sep='\n')