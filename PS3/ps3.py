# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string
import os
import sys

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = os.path.join(sys.path[0], "words.txt")

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    
    # Converts entered word to lowercase
    lower_word = word.lower()

    # Retrieves and sums points per letter
    letter_points = 0
    for letter in lower_word:
        letter_points += SCRABBLE_LETTER_VALUES[letter]

    # Calculates points based on word length and letters in hand
    length_points = (7 * len(lower_word) - 3 * (n - len(lower_word)))
    
    # Combines the two score components.
    # If the word length/letters in hand component < 1, it is not included in the word score.
    word_score = 0
    if length_points > 1:
        word_score = (letter_points * length_points)
    else:
        word_score = letter_points

    return word_score
    

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).
    One vowel per hand is a wildcard: '*'.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    
    # Calculates how many vowels to load for the hand.
    num_vowels = int(math.ceil(n / 3))

    # Chooses vowels. One is a wildcard ("*"), the rest are random.
    hand["*"] = 1
    for _ in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    # Randomly chooses consonants.
    for _ in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
   
    # Copies the hand into a new variable.
    new_hand = hand.copy()
    
    # Converts letters in the word to lowercase.
    word = word.lower()

    # For letters in the word that are also in the hand:
    for i in word:
        if i in new_hand:
        
        # If the value for the letter key in the dictionary == 1, the key is removed from the dictionary.
            if new_hand.get(i) == 1:
                del new_hand[i]
       
        # If the value for the letter key > 1, the value is decreased by 1.
            else:
                new_hand[i] -= 1

    # Nothing is done for letters that are not in the hand.
    
    return new_hand

#
# Problem #3: Test word validity
#

def valid_with_wild(word, word_list):
    '''
    If at least one word in the word list is possible given the 
    placement in the word of "*", modifies the word to contain 
    the vowel. Otherwise, returns an invalid word.
    '''
        
    # Copies word and converts to lowercase.
    working_word = word.lower()

    # If the word contains a wildcard ("*"):
    if "*" in working_word:

        # Replaces "*" with each vowel.
        for vowel in VOWELS:
            working_word = word.lower().replace("*", vowel)
            
            # If the new word is valid, returns that word.
            if working_word in word_list:
                return working_word
        
        # If no new words are valid, returns an invalid word.
        return working_word
    
    # Returns the original word if no wildcard.
    else:
        return working_word


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    # Retrieves the word for testing.
    dict_word = valid_with_wild(word, word_list)
    
    # Copies the hand.
    working_hand = hand.copy()
    # Tests if the word is in the word list.
    if dict_word in word_list:

        # Tests if all the letters in the word are in the hand.
        for letter in word:
            if letter in working_hand:

              # Removes the letter from the working hand:  
                # If the value for the letter key in the dictionary == 1, the key is removed from the dictionary.
                if working_hand.get(letter) == 1:
                    del working_hand[letter]
       
                # If the value for the letter key > 1, the value is decreased by 1.
                else:
                    working_hand[letter] -= 1
    
            # Returns false if any letter is not in the hand, 
            # or if a letter is repeated in the word more times than it exists in the hand.
            else:
                return False

        # Returns true if all letters in the word are in the hand.
        return True

    # Returns false if the word is not in the word list.
    else:
        return False
    

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """

    hand_len = 0
    for letter in hand:
        # Adds the quantity of each letter in the hand.
        hand_len += hand[letter]
    return hand_len


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # Keeps track of the total score.
    total_score = 0
    n = calculate_handlen(hand)

    # As long as there are still letters in the hand:
    while n > 0:

        # Displays the hand.
        print("Current hand: {}".format(display_hand(hand)))
        
        # Asks user for input.
        word = input('Enter word, or "!!" to indicate that you are finished: ')

        # If the input is two exclamation points, ends the hand, tells the user the score.
        if word == "!!":
            break
            
        # If the user enters a word:
        else:

            # If the word is valid, tells the user how many points the word earned,
            # and the updated total score.
            if is_valid_word == True:
                total_score += get_word_score(word, n)
                print('"{}" earned {} points. Total: {} points'.format(word, get_word_score(word, n), total_score))

            # If the word is not valid, rejects word.
            else:
                print("That is not a valid word. Please choose another word.")
            
            # Updates the user's hand.
            hand = update_hand(hand, word)
        
    # Game is over, tells the user the total score
    if n == 0:
        print("Ran out of letters. Total score for this hand: {} points".format(total_score))
    else:
        print("Total score: {} points".format(total_score))
    
    # Return the total score as result of function
    return total_score



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    pass  # TO DO... Remove this line when you implement this function
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    print("play_game not implemented.") # TO DO... Remove this line when you implement this function
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    n = 7
    hand = deal_hand(n)
    play_hand(hand, word_list)
