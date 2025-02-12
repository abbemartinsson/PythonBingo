import random

playerCard = []
compCard = []
cardSize = 5

def printCard(card):
    for i in range(5):
        print(card[i*cardSize:(i+1)*cardSize])

while len(compCard) < 25:
    compInput = random.randint(1, 75)
    if compInput not in compCard:
        compCard.append(compInput)

printCard(compCard)

for i in range (1,26):
    while True:
        try:
            playerInput = int(input(f"skriv in 25 nummer mellan 1 och 75, {i}/25: "))
            if 1<= playerInput <=75:
                if playerInput not in playerCard:
                    playerCard.append(playerInput)
                    break
                else:
                    print("Du har redan valt detta nummret, skriv ett nytt")
            else:
                print("Skriv ett nummer mellan 1 och 75!")
        except ValueError:
            print("Skriv ett giltigt nummer!")

print(f"Här är dina nummer:")
printCard(playerCard)
print(f"Här är datorns kort:")
printCard(compCard)

def winCheck(card, playerNumbers):
    for i in range(cardSize):
        if all(card[i * cardSize + j] in playerNumbers for j in range(cardSize)):
            return True
    for i in range(cardSize):
        if all(card[j * cardSize + i] in playerNumbers for j in range(cardSize)):
            return True
    if all(card[i * (cardSize + 1)] in playerNumbers for i in range(cardSize)):
        return True
    if all(card[(i + 1) * (cardSize - 1)] in playerNumbers for i in range(cardSize)):
        return True
    return False

playerBingo = False

playerNumbers = set(playerCard)

if winCheck(compCard, playerNumbers):
        playerBingo = True

if playerBingo:
    print("Du har bingo!")
    
else:
    print("Du har inte bingo")