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

