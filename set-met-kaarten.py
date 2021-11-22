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