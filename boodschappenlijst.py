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

 

