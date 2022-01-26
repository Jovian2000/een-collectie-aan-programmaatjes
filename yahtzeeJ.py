import random

dice = [1,2,3,4,5,6]
sets = []
rolledList = []
turn = 0
rolled = {}

diceA = 0
diceB = 0
diceC = 0
diceD = 0
diceE = 0

smallStraightList1 = [1,2,3,4]
smallStraightList2 = [2,3,4,5]
smallStraightList3 = [3,4,5,6]
largeStraightList1 = [1,2,3,4,5]
largeStraightList2 = [2,3,4,5,6]

aces = False
twos = False
threes = False
fours = False
fives = False
sixes = False

threeOfAKind = False
fourOfAKind = False
fullHouse = False
smallStraight = False
largeStraight = False
yahtzee = False
chance = False

scoresPart1 = {
    "Ace's": 0,
    "Two's": 0,
    "Threes": 0,
    "Fours": 0,
    "Fives": 0,
    "Sixes": 0,
    "Bonus Points": 0
}
scoresPart2 = {
    "Three of a kind": 0,
    "Four of a kind": 0,
    "Full House": 0,
    "Small Straight": 0,
    "Large Straight": 0,
    "Yathzee": 0,
    "Chance": 0,
}  

def showScore():
    print("\nUw score")
    for x, y in scoresPart1.items():
        print(x + ": " + str(y))
    for a, b in scoresPart2.items():
        print(a + ": " + str(b))

def checkScore():
    global sets, rolledList, scoresPart1, scoresPart2, aces, twos, threes, fours, fives, sixes, threeOfAKind, fourOfAKind, fullHouse, smallStraight, largeStraight, yahtzee, chance
    acesPoints = 0
    twosPoints = 0
    threesPoint = 0
    foursPoint = 0
    fivesPoint = 0
    sixesPoint = 0
    threeOfAKindPoints = 0
    fourOfAKindPoints = 0
    fullHousePoints = 0
    smallStraightPoints = 0
    largeStraightPoints = 0
    yahtzeePoints = 0
    chancePoints = 0
    count1 = rolledList.count(1)
    count2 = rolledList.count(2)
    count3 = rolledList.count(3)
    count4 = rolledList.count(4)
    count5 = rolledList.count(5)
    count6 = rolledList.count(6)
    print("\nU kunt kiezen uit:")
    if aces == False:
        if count1 > 0:
            acesPoints = count1 * 1
        print("ace's: " + str(acesPoints))
    if twos == False:
        if count2 > 0:
            twosPoints = count2 * 2
        print("two's: " + str(twosPoints))
    if threes == False:
        if count3 > 0:
            threesPoint = count3 * 3
        print("threes: " + str(threesPoint))
    if fours == False:
        if count4 > 0:
            foursPoint = count4 * 4
        print("fours: " + str(foursPoint))
    if fives == False:
        if count5 > 0:
            fivesPoint = count5 * 5
        print("fives: " + str(fivesPoint))
    if sixes == False:
        if count6 > 0:
            sixesPoint = count6 * 6
        print("sixes: " + str(sixesPoint)) 
    if threeOfAKind == False:
        if count1 == 3 or count2 == 3 or count3 == 3 or count4 == 3 or count5 == 3 or count6 == 3:
            threeOfAKindPoints = rolledList[0] + rolledList[1] + rolledList[2] + rolledList[3] + rolledList[4]
        print("three of a kind: " + str(threeOfAKindPoints))
    if fourOfAKind == False:
        if count1 == 4 or count2 == 4 or count3 == 4 or count4 == 4 or count5 == 4 or count6 == 4:
            fourOfAKindPoints = rolledList[0] + rolledList[1] + rolledList[2] + rolledList[3] + rolledList[4]
        print("four of a kind: " + str(fourOfAKindPoints))
    if fullHouse == False:
        if (count1 == 3 or count2 == 3 or count3 == 3 or count4 == 3 or count5 == 3 or count6 == 3) and (count1 == 2 or count2 == 2 or count3 == 2 or count4 == 2 or count5 == 2 or count6 == 2):
            fullHousePoints = 25
        print("full house: " + str(fullHousePoints))
    if smallStraight == False:
        if (1 in rolledList and 2 in rolledList and 3 in rolledList and 4 in rolledList) or (2 in rolledList and 3 in rolledList and 4 in rolledList and 5 in rolledList) or (3 in rolledList and 4 in rolledList and 5 in rolledList and 6 in rolledList):
            smallStraightPoints = 30
        print("small straight: " + str(smallStraightPoints))
    if largeStraight == False:
        if (count1 == 1 and count2 == 1 and count3 == 1 and count4 == 1 and count5 == 1) or (count2 == 1 and count3 == 1 and count4 == 1 and count5 == 1 and count6 == 1):
            largeStraightPoints = 40
        print("large straight: " + str(largeStraightPoints))
    if yahtzee == False:
        if count1 == 5 or count2 == 5 or count3 == 5 or count4 == 5 or count5 == 5 or count6 == 5:
            yahtzeePoints = 50
        print("yahtzee: " + str(yahtzeePoints))
    if chance == False:
        chancePoints = rolledList[0] + rolledList[1] + rolledList[2] + rolledList[3] + rolledList[4]
        print("chance: " + str(chancePoints))
    askChoice = input("\nUw keuze:\n")
    if askChoice == "ace's" and aces == False:
        scoresPart1["Ace's"] = acesPoints
        aces = True
    elif askChoice == "two's" and twos == False: 
        scoresPart1["Two's"] = twosPoints 
        twos = True
    elif askChoice == "threes" and threes == False:
        scoresPart1["Threes"] = threesPoint
        threes = True
    elif askChoice == "fours" and fours == False:
        scoresPart1["Fours"] = foursPoint
        fours = True
    elif askChoice == "fives" and fives == False:
        scoresPart1["Fives"] = fivesPoint
        fives = True
    elif askChoice == "sixes" and sixes == False:
        scoresPart1["Sixes"] = sixesPoint
        sixes = True
    elif askChoice == "three of a kind" and threeOfAKind == False:
        scoresPart2["Three of a kind"] = threeOfAKindPoints
        threeOfAKind = True
    elif askChoice == "four of a kind" and fourOfAKind == False: 
        scoresPart2["Four of a kind"] = fourOfAKindPoints
        fourOfAKind = True
    elif askChoice == "full house" and fullHouse == False:
        scoresPart2["Full House"] = fullHousePoints
        fullHouse = True
    elif askChoice == "small straight" and smallStraight == False:
        scoresPart2["Small Straight"] = smallStraightPoints
        smallStraight = True
    elif askChoice == "large straight" and largeStraight == False:
        scoresPart2["Large Straight"] = largeStraightPoints 
        largeStraight = True
    elif askChoice == "yahtzee" and yahtzee == False:
        scoresPart2["Yathzee"] += yahtzeePoints
        if yahtzeePoints == 0:
            yahtzee = True
    elif askChoice == "chance" and chance == False:
        scoresPart2["Chance"] = chancePoints
        chance = True
    else:
        print(dontUnderstand())
        checkScore()
    rollDiceA()
    rollDiceB()
    rollDiceC()
    rollDiceD()
    rollDiceE()
    
def rollDiceA():
    global diceA
    diceA = random.choice(dice)
def rollDiceB():
    global diceB
    diceB = random.choice(dice)
def rollDiceC():
    global diceC
    diceC = random.choice(dice)
def rollDiceD():
    global diceD
    diceD = random.choice(dice)
def rollDiceE():
    global diceE
    diceE = random.choice(dice)

def showRoll():
    global rolled
    print("")
    rolled = {
    "Dobbelsteen A": diceA,
    "Dobbelsteen B": diceB,
    "Dobbelsteen C": diceC,
    "Dobbelsteen D": diceD,
    "Dobbelsteen E": diceE
    }
    for k, v in rolled.items():
        print(k + ": " + str(v))

def holdDiceA():
    global diceA, sets
    holdA = input("Wilt u Dobbelsteen A houden?(Ja/Nee)\nAntwoord: ")
    if holdA == "Ja" or holdA == "ja":
        holdDiceB()
    elif holdA == "Nee" or holdA == "nee":
        rollDiceA()
        holdDiceB()
    else:
        print(dontUnderstand())
        holdDiceA()
def holdDiceB():
    global diceB, sets
    holdB = input("Wilt u Dobbelsteen B houden?(Ja/Nee)\nAntwoord: ")
    if holdB == "Ja" or holdB == "ja":
        holdDiceC()
    elif holdB == "Nee" or holdB == "nee":
        rollDiceB()
        holdDiceC()
    else:
        print(dontUnderstand())
        holdDiceB()
def holdDiceC():
    global diceC, sets
    holdC = input("Wilt u Dobbelsteen C houden?(Ja/Nee)\nAntwoord: ")
    if holdC == "Ja" or holdC == "ja":
        holdDiceD()
    elif holdC == "Nee" or holdC == "nee":
        rollDiceC()
        holdDiceD()
    else:
        print(dontUnderstand())
        holdDiceC()
def holdDiceD():
    global diceD, sets
    holdD = input("Wilt u Dobbelsteen D houden?(Ja/Nee)\nAntwoord: ")
    if holdD == "Ja" or holdD == "ja":
        holdDiceE()
    elif holdD == "Nee" or holdD == "nee":
        rollDiceD()
        holdDiceE()
    else:
        print(dontUnderstand())
        holdDiceD()
def holdDiceE():
    global diceE, sets
    holdE = input("Wilt u Dobbelsteen E houden?(Ja/Nee)\nAntwoord: ")
    if holdE == "Nee" or holdE == "nee":
        rollDiceE()
    elif (holdE != "Ja") and (holdE != "ja"):
        print(dontUnderstand())
        holdDiceE()
    
def roll():
    global turn, sets, rolledList, diceA, diceB, diceC, diceD, diceE
    showRoll()
    holdDiceA()
    turn += 1
    rollAsk = input("\nWilt u nog een keer rollen?(Ja/Nee)\n")
    if turn < 2 and (rollAsk == "Ja" or rollAsk == "ja"):
        roll()
    else:        
        showRoll()
        sets = rolled.values()
        rolledList = list(sets)
        print(rolledList)
        checkScore()
        showScore()
        if aces == True and twos == True and threes == True and fours == True and fives == True and sixes == True and threeOfAKind == True and fourOfAKind == True and fullHouse == True and smallStraight == True and largeStraight == True and yahtzee == True and chance == True:
            score1 = scoresPart1.values()
            score2 = scoresPart2.values()
            totalScore1 = sum(score1)
            totalScore2 = sum(score2)
            print("klaar")
            if totalScore1 >= 63:
                scoresPart2["Bonus Points"] = 35
                totalScore1 += 35
                print("U 1ste gedeelte krijgt nog een bonus (+35 punten)")
            showScore()
            totalScore = totalScore1 + totalScore2
            print("Dit is uw totale punten: " + str(totalScore))
            again()
        else:
            sets = []
            rolledList = [] 
            turn = 0
            roll()

def dontUnderstand():
    return "Sorry, dat begreep ik niet"

def again():
    global aces, twos, threes, fours, fives, sixes, threeOfAKind, fourOfAKind, fullHouse, smallStraight, largeStraight, yahtzee, chance, scoresPart1, scoresPart2, turn, rolledList, sets
    askPlayer = input("Wil je nog een keer spelen?(Ja/Nee)\n")
    if askPlayer == "Ja" or "ja":
        aces = False
        twos = False
        threes = False
        fours = False
        fives = False
        sixes = False
        threeOfAKind = False
        fourOfAKind = False
        fullHouse = False
        smallStraight = False
        largeStraight = False
        yahtzee = False
        chance = False
        scoresPart1["Ace's"] = 0
        scoresPart1["Two's"] = 0
        scoresPart1["Three's"] = 0
        scoresPart1["Four's"] = 0
        scoresPart1["Five's"] = 0
        scoresPart1["Six"] = 0
        scoresPart1["Bonus Points"] = 0
        scoresPart2["Three of a kind"] = 0
        scoresPart2["Four of a kind"] = 0
        scoresPart2["Full House"] = 0
        scoresPart2["Small Straight"] = 0
        scoresPart2["Large Straight"] = 0
        scoresPart2["Yathzee"] = 0
        scoresPart2["Chance"] = 0
        turn = 0
        rolledList = []
        sets = []
        roll()
    else: 
        print("Dank u wel voor het spelen!")
 
def begin():
    print("Welkom!")
    askBegin = input("Wilt u spelen?(Ja/Nee)\n")
    if askBegin == "Ja" or askBegin == "ja":
        roll()

rollDiceA()
rollDiceB()
rollDiceC()
rollDiceD()
rollDiceE()

begin()

