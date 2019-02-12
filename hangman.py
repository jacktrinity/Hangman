from os import system, name
from random import choice


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


class Hangman:

    def __init__(self):
        word_bank = ["APPLE", "ORANGE", "STRAWBERRY", "BANANA", "BLUEBERRY"]

        self.life = 0

        self.word = choice(word_bank)  # A random word from our word bank. Is alter throughout the game.
        self.display_word = self.word  # If player lose, the entire word will be display.

        self.guess = ""
        self.guess_box = []
        self.word_tile()

        self.start_game()

    # The function handles our game feature.
    def start_game(self):
        print("Guessed letters: {}".format(self.guess))
        self.game_board()
        self.display_guess_box()

        self.win_lose()
        self.user_input()

    # Display our Hangman board
    def game_board(self):
        if self.life == 0:
            print("  ------")
            print("       |")
            print("       |")
            print("       |")
            print("       |")
            print("    ------")
        elif self.life == 1:
            print("  ------")
            print("  O    |")
            print("       |")
            print("       |")
            print("       |")
            print("    ------")
        elif self.life == 2:
            print("  ------")
            print("  O    |")
            print("  |    |")
            print("       |")
            print("       |")
            print("    ------")
        elif self.life == 3:
            print("  ------")
            print("  O    |")
            print(" \|    |")
            print("       |")
            print("       |")
            print("    ------")
        elif self.life == 4:
            print("  ------")
            print("  O    |")
            print(" \|/   |")
            print("       |")
            print("       |")
            print("    ------")
        elif self.life == 5:
            print("  ------")
            print("  O    |")
            print(" \|/   |")
            print("  |    |")
            print("       |")
            print("    ------")
        elif self.life == 6:
            print("  ------")
            print("  O    |")
            print(" \|/   |")
            print("  |    |")
            print(" /     |")
            print("    ------")
        elif self.life == 7:
            print("  ------")
            print("  O    |")
            print(" \|/   |")
            print("  |    |")
            print(" / \   |")
            print("    ------")

    # Nicely display our letters
    def display_guess_box(self):
        guess_string = "".join(self.guess_box)
        print(guess_string)

    # Makes our guess_box at the beginning
    def word_tile(self):
        for i in range(len(self.word)):
            self.guess_box.append(" _ ")

    # Get valid user_input
    def user_input(self):
        guess_input = input("Please enter a letter: ")
        guess_upper = guess_input.upper()
        possible_guess = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if guess_upper in self.guess:
            print("You have already guessed {}.".format(guess_upper))
            return self.user_input()
        elif len(guess_upper) == 1 and guess_upper in possible_guess:
            self.check_word(guess_upper)
        else:
            print("Invalid Input")
            return self.user_input()

    # Check the user_input with our word and update our game variable
    def check_word(self, guess_upper):
        if guess_upper in self.word:
            while guess_upper in self.word:
                index = self.word.find(guess_upper)
                self.guess_box[index] = " {} ".format(guess_upper)

                temp_word_list = list(self.word)
                temp_word_list[index] = " "
                self.word = "".join(temp_word_list)

            self.guess += guess_upper + " "
        else:
            self.guess += guess_upper + " "
            self.life += 1

        clear()
        self.start_game()

    # Check to see when the game is over
    def win_lose(self):
        if " _ " not in self.guess_box:
            print("You Win!")
            quit()
        elif self.life == 7:
            print("The word is {}.".format(self.display_word))
            print("You Lose")
            quit()


Hangman()
