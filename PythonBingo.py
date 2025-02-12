import random

random_number = []

for _ in range (25):
    while True:
        random_tal = random.randint(0,75)
        if random_tal not in random_number:
            random_number.append(random_tal)
            break
        else:
            continue

dator_bricka = [random_number[i:i+5] for i in range (0,25,5)]


spelar_bricka = []
for i in range (0,25)
  spelar_number = int(input (f"välj 25 nummer som du vill ha på din bricka {i+1} / 25"))
  if 1 <= tal <= 75
    if spelar_number not in 


spelar_number = [random.randint(0,75) for _ in range(25)]

spelar_bricka = [spelar_number[i:i+5] for i in range(0, 25, 5)]



  


rättnings_matris = []


for i  in  range(0,25):
    input (f"tryck för att byta nummer: {i+1} av 25!")
    if random_number[i] in spelar_number:
        print ("match")
        random_number[i] = "x"
        rättnings_matris.append("x")
    else:
        rättnings_matris.append (random_number[i])


for i in range(5):
    if all(element == "x"for element in random_number):
        bingo = True
        break
    else:
        bingo = False
        continue



if rättnings_matris.count("x") >= 1:
  bingo = True
else:
  bingo = False


print ("dator_bricka")
for row in dator_bricka:
    print (row)

print ("Spelare Bricka")
for row in spelar_bricka:
    print(row)


print("dator bricka rad 1")
print (*dator_bricka[0])

if bingo == True:
    print ("bingo")
