import random

names = []
namesDict = {}
lottery = []
namesPulled = []
nameLimit = 2
a = ""

print("\nLootjes generator. Voer de namen in. \n(stop = hele programma stoppen)")
print("Namen:")

while True:
    names.append(input(""))
    if "stop" in names:
        names.clear()
        break
    if len(names) > nameLimit:
        if "klaar" in names:
            break
        print("U heeft genoeg namen. Als u de lootjes wilt trekken, typ 'klaar'.")
    else: 
        print("U moet nog " + str(nameLimit - len(names) + 1) + " namen invoeren") 
names.remove("klaar")

names = list(dict.fromkeys(names))
lottery.extend(names)

def pullingNames():
    global lottery, namesPulled, a
    a = random.choice(lottery)
    namesPulled.append(a)
    lottery.remove(a)

for x in range(len(names)):
    if names[x] in lottery: 
        lottery.remove(names[x])
        pullingNames()
        lottery.append(names[x])
    else:    
        pullingNames()
    print(names)
    print(lottery)
    print(a)

for i in range(len(names)):    
    namesDict.update({names[i]: namesPulled[i]})
print("")
for m, n in namesDict.items():
    print(m + ": " + n)
        