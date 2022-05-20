import random
import string
import time

def start_game_display_message():
    print("\nWelcome to Hangman by Erub Khan.")
    name = input("Enter your name: ")
    print("\nHello", name, "! Goodluck!\n")
    time.sleep(1)
    print("Loading Hangman...")
    print("Let's play!\n")
    time.sleep(1)
    print("Guess the word by choosing a letter to fill in the blanks.\n")

def readfile(filename):
    word_list = []
    file = open(filename, "rt")

    for line in file:
        line = line.strip()
        word_list.append(line)

    file.close()
    return word_list

def generate_word(word_list):
    num = random.randint(0, len(word_list)-1) #randint is inclusive 
    return word_list[num]

def build_hangman(word, right_guesses, mistakes): #right_guesses is a list of correct letters guessed
    print_list = []
    #put blank spaces for the un-guessed letters
    for i in range(0, len(word)):
        print_list.append("__")

    #replace the blank spaces with the letters from right_guesses
    #TRACE ON PAPER for better understanding    
    for i in range(0, len(word)):
        for letter in right_guesses:
            if word[i] == letter:
                print_list[i] = letter

    #print the word so far
    for letter in print_list:
        print(" ", letter, " ", end="")
        

    if mistakes == 0:
        print("")
        print(" _____ ")
        print(" |   |")
        print(" | ")
        print(" | ")
        print(" | ")
        print(" | ")
        print("_|_______")
        print("")
    elif mistakes == 1:
        print("")
        print(" _____ ")
        print(" |   |")
        print(" |   O")
        print(" | ")
        print(" | ")
        print(" | ")
        print("_|_______")
        print("")
    elif mistakes == 2:
        print("")
        print(" _____ ")
        print(" |   |")
        print(" |   O")
        print(" |   |")
        print(" |   |")
        print(" | ")
        print("_|_______")
        print("")
    elif mistakes == 3:
        print("")
        print(" _____ ")
        print(" |   |")
        print(" |   O")
        print(" |   |/")
        print(" |   |")
        print(" | ")
        print("_|_______")
        print("")
    elif mistakes == 4:
        print("")
        print(" _____ ")
        print(" |   |")
        print(" |   O")
        print(" |  \|/")
        print(" |   |")
        print(" | ")
        print("_|_______")
        print("")
    elif mistakes == 5:
        print("")
        print(" _____ ")
        print(" |   |")
        print(" |   O")
        print(" |  \|/")
        print(" |   |")
        print(" |    \_")
        print("_|_______")
        print("")
    elif mistakes == 6:
        print("")
        print(" _____ ")
        print(" |   |")
        print(" |   O")
        print(" |  \|/")
        print(" |   |")
        print(" | _/ \_")
        print("_|_______")
        print("")

def get_letter(alphabets_list):
    user_letter = input("Guess your letter: ")
    while True:
        for letter in alphabets_list:
            if user_letter.lower() == letter:
                return letter.lower()
                break
        user_letter = input("Incorrect. Enter a letter: ")
            
def check_letter(word, letter):
    for every_letter in word:
        if every_letter == letter:
            return True
    return False

def check_repeated_letter(total_letters_guessed, letter):
    for every_letter in total_letters_guessed:
        if letter == every_letter:
            return True #letter already in list
    return False

def game_result(word, right_guesses):
    print_list = []
    #put blank spaces for the un-guessed letters
    for i in range(0, len(word)):
        print_list.append("__")

    for i in range(0, len(word)):
        for letter in right_guesses:
            if word[i] == letter:
                print_list[i] = letter

    for item in print_list:
        if item == "__":
            return False

    return True


def play(run):
    word_list = readfile("words.txt")
    mistakes = 0
    right_guesses = []
    total_letters_guessed = []
    
    alphabets = string.ascii_lowercase
    alphabets_list = list(alphabets)

    #stop the game
    if run == 'no':
        return False
    
    start_game_display_message()
    word = generate_word(word_list)
    #print(word) #get rid of later

    build_hangman(word, right_guesses, mistakes)

    while mistakes != 6:
        letter = get_letter(alphabets_list) 

        #if letter is correct, build word
        if (check_letter(word, letter)):
            #if letter has not been guessed
            if letter not in total_letters_guessed:
                right_guesses.append(letter)
                total_letters_guessed.append(letter)
                build_hangman(word, right_guesses, mistakes)

            #if letter has been guessed
            else:
                print("You have already guessed this letter.")
                          
            if (game_result(word, right_guesses)): 
                print("You've won!")
                break
            
        #if letter is incorrect, build hangman
        else:
            if letter in total_letters_guessed:
                print("You have already guessed this letter.")
            else:
                print("Incorrect guess.")
                mistakes += 1
                total_letters_guessed.append(letter)
                build_hangman(word, right_guesses, mistakes)     
                
            if mistakes == 6:
                print("You've lost.")
                print("The word was " + word + ". Better luck nextime!")

    return True   


def main():
    run = 'yes'
    play(run)
    while True:
        time.sleep(1)
        run = input("\nWould you like to play again? Enter 'yes' or 'no': ")
        if run.lower() == 'yes':
            play(run)
        elif run.lower() == 'no':
            print("\nThank-you for playing Hangman!")
            break
        

main()


