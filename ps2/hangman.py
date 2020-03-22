# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import os
import sys

WORDLIST_FILENAME = os.path.join(sys.path[0], "words.txt")
VOWELS = ("a", "e", "i", "o", "u")

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
        




def get_guessed_word(word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ""
    for letter in word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_ "
    return guessed_word




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
   
    available_letters = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters

  


# Calculates the user's score based on guesses left and amount of unique letters in the word    
def user_score(guesses_left, secret_word):
    unique_letters = set()
    for l in secret_word:
        unique_letters.add(l)
    return (len(unique_letters) * guesses_left)




def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    # Use the following input function to manually set the secret word:
    # secret_word = input("Set the secret word. ")

    # Use this function to access a random secret word:
    secret_word = choose_word(wordlist)

    # Game introduction and setting up variables
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
    # separator spaces out guesses for improved usability
    separator = "---------------"
    guesses_left = 6
    warnings_left = 3
    letters_guessed = []


    # Loop for guessing the secret word
    while is_word_guessed(secret_word, letters_guessed) == False and guesses_left > 0:
        print(separator)

        # Tells the user how many guesses and warnings are left and what letters they can choose from
        print("You have {} guesses and {} invalid input warnings left.".format(guesses_left, warnings_left))
        print("Available letters: {}".format(get_available_letters(letters_guessed)))

        # Prompts the user to choose a letter
        guessed_letter = input("Please guess a letter: ").lower()


        # Responds to the user entering a number or symbol (the user begins with 3 warnings)
        if not guessed_letter.isalpha():

            # Takes away a guess if the user is out of warnings
            if warnings_left == 0:
                guesses_left -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess.")
            
            # Takes away 1 warning for invalid input, then reports using "warning" singular when the user has 1 warning left
            elif warnings_left == 2:
                warnings_left -= 1
                print("Oops! That is not a valid letter. You have {} warning left.".format(warnings_left))
            
            # Takes away 1 warning for invalid input, then reports using "warnings" plural when the user has 2 or 0 warnings left
            else:
                # Takes away 1 warning for invalid input
                warnings_left -= 1
                print("Oops! That is not a valid letter. You have {} warnings left.".format(warnings_left))
        

        # Responds to the user repeating a guess
        elif guessed_letter in letters_guessed:
            
            # Takes away a guess if the user is out of warnings
            if warnings_left == 0:
                guesses_left -= 1
                print("Oops! You already guessed that letter. You have no warnings left so you lose one guess.")
           
            # Takes away 1 warning for invalid input, then reports using "warning" singular when the user has 1 warning left
            elif warnings_left == 2:
                warnings_left -= 1
                print("Oops! You already guessed that letter. You have {} warning left.".format(warnings_left))
            
            # Takes away 1 warning for invalid input, then reports using "warnings" plural when the user has 2 or 0 warnings left
            else:
                warnings_left -= 1
                print("Oops! You already guessed that letter. You have {} warnings left.".format(warnings_left))
        
       
        # If the user guesses a letter in the word, adds letter guessed to guessed letter array
        elif guessed_letter in secret_word:
            letters_guessed += guessed_letter
            print("Good guess!: {}".format(get_guessed_word(secret_word, letters_guessed)))
        
        
        # If the user guesses a letter not in the word, takes away 1 guess for a consonant, 2 guesses for a vowel
        # Adds letter to guessed letter array        
        elif guessed_letter in VOWELS:
            letters_guessed += guessed_letter
            print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letters_guessed)))
            guesses_left -= 2
      
        else:
            letters_guessed += guessed_letter
            print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letters_guessed)))
            guesses_left -= 1
    


    # Ends the game when the user is out of guesses
    if guesses_left <= 0:
        print(separator)
        print("Sorry, you ran out of guesses. The word was {}.".format(secret_word))

    # Ends the game and displays the user's score when the user guesses the secret word
    else:
        print(separator)
        print("Congratulations, you won the game!")
        print("Your total score for the game is: {}".format(user_score(guesses_left, secret_word)))




# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
        '''
    my_word = my_word.replace(" ", "")
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if my_word[i] != other_word[i] and my_word[i] != "_":
                return False
            elif my_word[i] == "_" and other_word[i] in my_word:
                return False
        return True
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
             '''
    matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matches.append(word)
    printable_matches = " ".join(matches)
    if matches == []:
        print("No matches found.")
    else:
        print("Possible word matches are: {}".format(printable_matches))



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # Use the following input function to manually set the secret word:
    # secret_word = input("Set the secret word. ")

    # Use this function to access a random secret word:
    secret_word = choose_word(wordlist)

    # Game introduction and setting up variables
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
    # separator spaces out guesses for improved usability
    separator = "---------------"
    guesses_left = 6
    warnings_left = 3
    letters_guessed = []
    guessed_word = get_guessed_word(secret_word, [])


    # Loop for guessing the secret word
    while is_word_guessed(secret_word, letters_guessed) == False and guesses_left > 0:
        print(separator)

        # Tells the user how many guesses and warnings are left and what letters they can choose from
        print("You have {} guesses and {} invalid input warnings left.".format(guesses_left, warnings_left))
        print("Available letters: {}".format(get_available_letters(letters_guessed)))

        # Prompts the user to choose a letter
        guessed_letter = input("Please guess a letter: ").lower()


        # Responds to the user entering a number or symbol (the user begins with 3 warnings)
        if not guessed_letter.isalpha():

            # Shows hints if the user enters "*"
            if guessed_letter == "*":
                show_possible_matches(guessed_word)

            # Takes away a guess if the user is out of warnings
            elif warnings_left == 0:
                guesses_left -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess.")
            
            # Takes away 1 warning for invalid input, then reports using "warning" singular when the user has 1 warning left
            elif warnings_left == 2:
                warnings_left -= 1
                print("Oops! That is not a valid letter. You have {} warning left.".format(warnings_left))
            
            # Takes away 1 warning for invalid input, then reports using "warnings" plural when the user has 2 or 0 warnings left
            else:
                # Takes away 1 warning for invalid input
                warnings_left -= 1
                print("Oops! That is not a valid letter. You have {} warnings left.".format(warnings_left))
        

        # Responds to the user repeating a guess
        elif guessed_letter in letters_guessed:
            
            # Takes away a guess if the user is out of warnings
            if warnings_left == 0:
                guesses_left -= 1
                print("Oops! You already guessed that letter. You have no warnings left so you lose one guess.")
           
            # Takes away 1 warning for invalid input, then reports using "warning" singular when the user has 1 warning left
            elif warnings_left == 2:
                warnings_left -= 1
                print("Oops! You already guessed that letter. You have {} warning left.".format(warnings_left))
            
            # Takes away 1 warning for invalid input, then reports using "warnings" plural when the user has 2 or 0 warnings left
            else:
                warnings_left -= 1
                print("Oops! You already guessed that letter. You have {} warnings left.".format(warnings_left))
        
       
        # If the user guesses a letter in the word, adds letter guessed to guessed letter array
        elif guessed_letter in secret_word:
            letters_guessed += guessed_letter
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            print("Good guess!: {}".format(guessed_word))
        
        
        # If the user guesses a letter not in the word, takes away 1 guess for a consonant, 2 guesses for a vowel
        # Adds letter to guessed letter array        
        elif guessed_letter in VOWELS:
            letters_guessed += guessed_letter
            print("Oops! That letter is not in my word: {}".format(guessed_word))
            guesses_left -= 2
      
        else:
            letters_guessed += guessed_letter
            print("Oops! That letter is not in my word: {}".format(guessed_word))
            guesses_left -= 1
    


    # Ends the game when the user is out of guesses
    if guesses_left <= 0:
        print(separator)
        print("Sorry, you ran out of guesses. The word was {}.".format(secret_word))

    # Ends the game and displays the user's score when the user guesses the secret word
    else:
        print(separator)
        print("Congratulations, you won the game!")
        print("Your total score for the game is: {}".format(user_score(guesses_left, secret_word)))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
