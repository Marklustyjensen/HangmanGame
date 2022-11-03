import random
import string

# Here I import the list of words from the file words.py
from Words import words
from Animation import animation

# Here I define a fuction that will go into the long list of word in the "words.py" file and randomly pick one
def get_word(words):
    word = random.choice(words)

    return word.upper()

def hangman():
    word = get_word(words) # Here I assign the selected word from the get_word fuction to the word in the game
    word_letters = set(word) # Here I break the selected word into seperate letters and put them into a list
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # Here I create an empty list to store the letters the user has guesses during the game

    # Here I check if the word chosen by the computer contains either a "-" or a " ". If thats the case I have the computer 'guess' for those. That way they are automatically put into the solution, and the user only have to guess letters, and not symbols
    if "-" in word:
            auto_guess = "-"
            used_letters.add(auto_guess)
            word_letters.remove(auto_guess)
    elif " " in word:
        auto_guess = " "
        used_letters.add(auto_guess)
        word_letters.remove(auto_guess)

    # Here I set the amount of lives I want to give the user playing the game
    lives = 11

    while len(word_letters) > 0 and lives > 0:

        animation(lives)

        # Here I break the list containing the guessed letters up into a string where each letter is seperated by a space
        print("Letters already gussed: ", " ".join(used_letters))

        # Here I print the progress of the user
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word: ", " ".join(word_list))

        # Now I ask the user to guess a letters
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
        elif user_letter in used_letters:
            print("You have already guessed this letter, please try another letter.")
        else:
            print("Invalid character. Please enter a valid character")

    if lives == 0:
        animation(lives)
        print("The word was " + word + ".")
    else:
        print("You guessed the word", word, "!!!!!")

# Here I call an instance of the game for the player to play
hangman()
