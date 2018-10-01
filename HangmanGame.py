import string


def verifyInput(guessedLetter, vowels, guessedLetterList):
    if (guessedLetter.isalpha() and len(guessedLetter) == 1) and (guessedLetter not in guessedLetterList) and (guessedLetter not in vowels):
        return True
    else:
        print("error in input")
        return False

while True:
    word = input("Enter word to guess:").upper()
    if word.isalpha() and len(word) >= 5:
        break
    else:
        print("Please enter at least a 5 letters long word without numbers or special character")

vowels = ["A", "E", "I", "O", "U"]
numberOfUniqueLetterToGuess = []
for i in word:
    if i in vowels:
        print(i, end=" ")
    else:
        print("_", end=" ")
        if i not in numberOfUniqueLetterToGuess:
            numberOfUniqueLetterToGuess.append(i)
print()
print(numberOfUniqueLetterToGuess)
guessedLetterList = []
hangman = 5
while hangman > 0 and (len(guessedLetterList) != len(numberOfUniqueLetterToGuess)):
    while True:
        guessedLetter = input("Guess a consonant letter:").upper()
        if verifyInput(guessedLetter, vowels, guessedLetterList):
            break

    if guessedLetter in word:
        guessedLetterList.append(guessedLetter)
        for i in word:
            if i in vowels or i in guessedLetterList:
                print(i, end=" ")
            else:
                print("_", end=" ")
    else:
        chancesLeft = hangman - 1
        hangman -= 1
        print(chancesLeft, "guesses left")
    print()
    print(guessedLetterList)
if hangman == 0:
    print("You lost ;/")
else:
    print("Congratulations!!! You won :-)")

