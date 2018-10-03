import random

# fetching comma separated words from a file, adding the words into a list and shuffling the list
file = open("words.txt", "r")
lines = file.read().split(",")
random.shuffle(lines)


# checks if the letter guessed is an alphabet, consonant and hasn't been guessed already
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


# main game
def hangmanGame(wordCount):
    # getting a word from a list of words
    word = lines[wordCount].upper()
    # defining vowels array
    vowels = ["A", "E", "I", "O", "U"]
    # defining list to store unique consonants from word
    numberOfUniqueLetterToGuess = []
    for i in word:
        # if i(letter in word) is a vowel display the letter
        if i in vowels:
            print(i, end=" ")
        # else display a dash
        else:
            print("_", end=" ")
            # if word is not already in unique consonant list add the word
            if i not in numberOfUniqueLetterToGuess:
                numberOfUniqueLetterToGuess.append(i)
    print()
    # list to store unique consonants guessed by user
    guessedLetterList = []
    # number of wrong guesses allowed (can be increased to give more guesses)
    hangman = 5
    # number of guesses is more than 0 and length of unique guessed letter is not equal to length of
    # list containing unique consonants
    while hangman > 0 and (len(guessedLetterList) != len(numberOfUniqueLetterToGuess)):
        while True:
            # accepting guessed letter from user
            guessedLetter = input("Guess a letter:").upper()
            # verifying input
            if verifyInput(guessedLetter, vowels, guessedLetterList):
                break
        # if guesses letter is in word add it to unique guessed letter list
        if guessedLetter in word:
            guessedLetterList.append(guessedLetter)
            for i in word:
                # if i(letter in word) is vowel or is in unique guessed letter list display it
                if i in vowels or i in guessedLetterList:
                    print(i, end=" ")
                # else display dash
                else:
                    print("_", end=" ")
        else:
            # if wrong letter is guessed decrement chances left
            chancesLeft = hangman - 1
            hangman -= 1
            print(chancesLeft, "guesses left")
        print()
    # if 0 number of guesses are left display the correct word and end game
    if hangman == 0:
        print("You lost -_-\n")
        print("Correct word was", word)
        exit(1)
    # if user guesses the word correctly recursive call hangmanGame with incremented word count to get the next word
    else:
        print("\nYou have guessed the word correctly\n")
        wordCount += 1
        hangmanGame(wordCount)


if __name__ == "__main__":
    hangmanGame(0)

