# een-collectie-aan-programmaatjes
## F1.6.02.O2
```python
groceriesDict = {}
while True: 
    yesOrNo = input("Wilt u iets toevoegen aan u boodschappenlijstje?(y/n)\n")
    if yesOrNo == "Y" or yesOrNo == "y":
        what = input("Wat wilt u toevoegen aan u boodschappenlijst?\n")
        howMuch = int(input("Hoeveel?\n"))
        if what in groceriesDict:
            groceriesDict[what] += howMuch 
        else: 
            groceriesDict.update({what: howMuch})
    elif yesOrNo == "N" or yesOrNo == "n": 
        break
    else:
        print("Sorry, dat begrijp ik niet")
print("")
print("Boodschappenlijst:")
for a, b in groceriesDict.items():
    print(a, b)
# De for loop zorgt ervoor dat wat er in de dictionary zit onder elkaar is gezet
```
## F1.6.02.O3
``` python
import random
deck = ["Joker 1", "Joker 2"]
cardsButNotNumbers = ["aas", "boer", "vrouw", "heer"]
def cardsImport(typeCards):
    for i in range(2,11):
# append zorgt ervoor dat hij iets toevoegd in de lijst 
        deck.append(typeCards + " " +str(i))
    for e in cardsButNotNumbers:
        deck.append(typeCards + " " + e)
cardsImport("Klaver")
cardsImport("Harten")
cardsImport("Schoppen")
cardsImport("Ruiten")
# random.shuffle zorgt ervoor dat hij de list van deck door elkaar haalt
random.shuffle(deck)
for i in range(7): 
    print("Kaart " + str(i + 1) + ": " + deck[i])
print("")
print(deck)
print("Er zitten " + str(len(deck)) + " kaarten")
```
## F1.6.02.O4
``` python 
import string
import random
alphabetLowercase = list(string. ascii_lowercase)
alphabetUppercase = list(string. ascii_uppercase)
numbers = list(string.digits)
symbols = ["@","#","$","%","&","_","?"]
password = []
trys = 0
upper = 0
lower = 0
numbersCount = 0
symbolsCount = 0
while True:
    password.extend(random.choice(alphabetLowercase + alphabetUppercase))
    password.extend(random.choices(alphabetLowercase + alphabetUppercase + symbols, k=2))
    password.extend(random.choices(alphabetLowercase + alphabetUppercase + numbers + symbols, k=20))
    password.extend(random.choice(alphabetLowercase + alphabetUppercase + numbers))
    for i in range(len(password)):
        if password[i] in numbers:
            numbersCount += 1
        if password[i] in symbols:
            symbolsCount += 1
        if (password[i]>= "a" and password[i]<="z"):
            lower += 1
        elif(password[i]>= "A" and password[i]<="Z"):
            upper += 1
    if lower >= 8 and (upper >= 2 and upper <= 6) and symbolsCount == 3 and (numbersCount >= 4 and numbersCount <= 7):
        break
    password.clear()
    upper = 0
    lower = 0
    numbersCount = 0
    symbolsCount = 0
print("\nUw password:")
print("".join(password))
print("\nKleine letters: " + str(lower))
print("Grote letters: " + str(upper))
print("Symbolen: " + str(symbolsCount))
print("Getallen: " + str(numbersCount))
```