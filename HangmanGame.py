import string
while True:
    word = input("Enter word to guess:").upper()
    if word.isalpha():
        break
    else:
        print("Please enter a word without numbers")

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

guessedLetterList = []
hangman = 5
while hangman > 0 and (len(guessedLetterList) != len(numberOfUniqueLetterToGuess)):
    while True:
        guessedLetter = input("Guess a consonant letter:").upper()
        if len(guessedLetter) != 1 or guessedLetter not in string.ascii_letters:
            print("Please enter a single alphabet:")
        else:
            break
    if guessedLetter in vowels:
        while True:
            guessedLetter = input("Please enter a consonant only:").upper()
            if len(guessedLetter) != 1 or guessedLetter not in string.ascii_letters:
                print("Please enter a single alphabet:")
            else:
                break
    elif guessedLetter in guessedLetterList:
        print("You have already guessed", guessedLetter)
        while True:
            guessedLetter = input("Guess a consonant letter:").upper()
            if len(guessedLetter) != 1 or guessedLetter not in string.ascii_letters:
                print("Please enter a single alphabet:")
            else:
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

if hangman == 0:
    print("You lost ;/")
else:
    print("Congratulations!!! You won :-)")
