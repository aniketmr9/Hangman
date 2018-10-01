word = input("Enter word to guess:").upper()
vowels = ["A", "E", "I", "O", "U"]
print(type(vowels))
numberOfUniqueLetterToGuess = []
for i in word:
    if i in vowels:
        print(i, end=" ")
    else:
        print("_", end=" ")
        if i not in numberOfUniqueLetterToGuess:
            numberOfUniqueLetterToGuess.append(i)
print()
#print(numberOfUniqueLetterToGuess)
guessedLetterList = []
hangman = 5
while hangman > 0 and (len(guessedLetterList) != len(numberOfUniqueLetterToGuess)):
    guessedLetter = input("Guess a consonant letter:").upper()
    if guessedLetter in vowels:
        guessedLetter = input("Please enter a consonant only:").upper()
    elif guessedLetter in guessedLetterList:
        print("You have already guessed", guessedLetter)
        guessedLetter = input("Guess a consonant letter:").upper()
    if guessedLetter in word:
        guessedLetterList.append(guessedLetter)
        for i in word:
            if i in vowels:
                print(i, end=" ")
            elif i in guessedLetterList:
                print(i, end=" ")
            else:
                print("_", end=" ")
    else:
        chancesLeft = hangman - 1
        hangman -= 1
        print(chancesLeft, "guesses left")
    print()
#print(guessedLetterList)
if hangman == 0:
    print("You lost ;/")
else:
    print("Congratulations!!! You won :-)")
