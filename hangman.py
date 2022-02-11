import sys
import random

# simple quit function with a message
def quit_function():
    sys.exit("\n" + "See ya!")

# prints the start menu where you can choose the difficulty
def print_menu():
    print("DIFFICULTY LEVELS ") 
    print("\n" + "1. Easy - word < 6 letters and 6 lives ")
    print("2. Hard - word >= 6 letters and 3 lives ")
    difficulty = input("\n" + "Please choose a difficulty level or quit: ")
    while True:
        if difficulty == '1' or difficulty == '2':
            return difficulty
        elif difficulty.lower() == 'quit':
            quit_function()
        else:
            difficulty = input("\n" + "Please choose a difficulty level or quit: ")

# takes words from the txt file
def get_word_to_be_guessed(difficulty):
    word_list = []
    pair_list = []
    f = open("countries-and-capitals.txt", "r")
    lines = f.readlines()
    for pair in lines:
        pair = pair[:-1]
        pair_set = pair.split(' | ')
        pair_list.append(pair_set)
    for pair in pair_list:
        capital = pair[1]
        if len(capital) < 6 and difficulty == '1' or len(capital) >= 6 and difficulty == '2':
            word_list.append(pair)
        else:
            pass
    chosen_pair = random.choice(word_list)
    return chosen_pair[0].lower(), chosen_pair[1].lower()

# sets how many lives you have depending on the difficulty
def get_lives(difficulty): 
    if difficulty == "1":
        return 6
    elif difficulty == "2":
        return 3

# prints the word hidden by underlines
def print_unguessed_word(word, tried_letters):
    unguessed_word = ""
    for letter in word:
        if letter in tried_letters:
            unguessed_word += letter + " "
        elif letter == ' ':
            unguessed_word += ' '
        else:
            unguessed_word += "_ "
    print('\n' + unguessed_word.upper())

# displays the letters that are not in the word to be guessed 
def display_wrong_letters(letters, word):
    wrong_let_str = "\n" + 'Wrong letters are:'
    for letter in letters:
        if letter.isalpha() == True:
            if letter in word:
                pass
            else:
                wrong_let_str += ' ' + letter.upper()
        else:
            pass
    return wrong_let_str

# displays art that represents how many live you have
def display_hangman(lives, difficulty):
    hangman_pics = ['''
    +---+
    |   |
        |
        |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
        |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
    |   |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
   /|   |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
   /|\  |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
   /|\  |
   /    |
        |
   ========''','''
    +---+
    |   |
    o   |
   /|\  |
   / \  |
        |
   ========''']
    if difficulty == '1':
        print('\n'+ hangman_pics[(len(hangman_pics) - 1) - lives])
    elif difficulty == '2':
        print('\n'+ hangman_pics[(len(hangman_pics) - 1) - lives*2])

# gets the input of a letter and also validates
def get_letter(tried_letters, word): 
    status = False
    letter = input("\n" + "Guess a letter: ").lower()    
    while status == False:
        if letter.isalpha() == True and len(letter) == 1 and letter not in tried_letters:
            letter = letter
            status = True
        elif letter.isalpha() == True and len(letter) == 1 and letter  in tried_letters:
            letter = input("\n" + "You already tried this letter, please submit anoter: ")
            status = False
        elif letter == 'quit':
            status = True
        elif letter == word:
            status = True
        else:
            letter = input("\n" + "Character not valid please submit a letter: ")
            status = False
    return letter

# check if you type quit
def is_letter_quit(letter):
    if letter.lower() == "quit":
        return True
    else:
        return False

# checks if you won the game by guessing the word
def is_game_won(word, tried_letters):
    status = False
    for character in word:
        if character not in tried_letters:
            status = False
            break
        else:
            status = True
    return status

# checks if letter is in word
def is_letter_in_word(word, letter):
    if letter in word:
        return True
    else:
        return False


def main():
    difficulty = print_menu()
    hint, word = get_word_to_be_guessed(difficulty)
    lives = get_lives(difficulty)
    tried_letters = []
    while lives > 0 and is_game_won(word, tried_letters) == False:
        display_hangman(lives, difficulty)
        print_unguessed_word(word, tried_letters)
        if len(tried_letters) != 0:
            print('\n' + display_wrong_letters(tried_letters, word))  
        letter = get_letter(tried_letters, word)
        if letter == word:
            for char in word:
                tried_letters.append(char)     
        elif len(letter) == 1 and letter in 'abcdefghijklmnopqrstuvwxyz':
            tried_letters.append(letter)
        if is_letter_quit(letter):
            quit_function()
        elif not is_letter_in_word(word, letter):
            lives -= 1      
        else:
            pass  
        if lives == 1 and is_game_won(word, tried_letters) == False:
            print("\n" + "The correct answer is the capital of " + hint.capitalize())
    if lives == 0:
        display_hangman(lives, difficulty)
        print("\n" + "You have lost the game.")
    elif is_game_won(word, tried_letters):
        display_hangman(lives, difficulty)
        print_unguessed_word(word, tried_letters)
        print("\n" + "You have won the game!")


if __name__ == "__main__":
    main()
