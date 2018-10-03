import random

file = open("words.txt", "r")
lines = file.read().split(",")
random.shuffle(lines)
print(lines)
print(len(lines))


def verifyInput(guessedLetter, vowels, guessedLetterList):
    if not (guessedLetter.isalpha() and len(guessedLetter) == 1):
        print("Please enter a single alphabet")
        return False
    elif guessedLetter in guessedLetterList:
        print("You have already guessed", guessedLetter)
        return False
    elif guessedLetter in vowels:
        print("Please enter a consonant")
        return False
    else:
        return True


def hangmanGame(wordCount):
    word = lines[wordCount].upper()
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
    #print(numberOfUniqueLetterToGuess)
    guessedLetterList = []
    hangman = 5
    while hangman > 0 and (len(guessedLetterList) != len(numberOfUniqueLetterToGuess)):
        while True:
            guessedLetter = input("Guess a letter:").upper()
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
        #print(guessedLetterList)
    if hangman == 0:
        print("You lost -_-\n")
        print("Correct word was", word)
        exit(1)
    else:
        print("\nYou have guessed the word correctly\n")
        wordCount += 1
        hangmanGame(wordCount)


if __name__ == "__main__":
    hangmanGame(0)

