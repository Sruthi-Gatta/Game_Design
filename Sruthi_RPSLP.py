import random


def player():
    """
        Ask user to input objects
        Check if the input is valid
        If the input is valid, return a string that represents the object
        Else print out error message and keep asking until getting a valid input
    """

    your_input = input(
        "What do you want ? R (Rock) / P (Paper) / S (Scissors) / L (Lizard) / V (Spock) : ")
    if your_input == "R":
        return "R"
    elif your_input == "P":
        return "P"
    elif your_input == "S":
        return "S"
    elif your_input == "L":
        return "L"
    elif your_input == "V":
        return "V"
    else:
        print(f"{your_input} : INVALID ENTRY")
        return player()


def computer():
    """Computer randomly picks an object and returns the string"""

    rand_comp = random.randrange(0, 5)
    if rand_comp == 0:
        return "R"
    elif rand_comp == 1:
        return "P"
    elif rand_comp == 2:
        return "S"
    elif rand_comp == 3:
        return "L"
    elif rand_comp == 4:
        return "V"
    else:
        return "INVALID"


def game():
    """
    Return True if player wins else False
    If a tie happens, the process is repeated until a winner is found
    Print out messages for each round
    Print out winner if found and return bool
    """

    player_ip = player()
    computer_ip = computer()
    print(f"player_input: {player_ip}")
    print(f"computer_input: {computer_ip}")

    if player_ip == computer_ip:
        print("Oh , its a tie. The Game is still on")
        return game()
    elif player_ip == "S" and computer_ip == "P":
        print("Hurray! You Won")
        return True
    elif player_ip == "P" and computer_ip == "R":
        print("Hurray! You Won")
        return True
    elif player_ip == "R" and computer_ip == "L":
        print("Hurray! You Won")
        return True
    elif player_ip == "L" and computer_ip == "V":
        print("Hurray! You Won")
        return True
    elif player_ip == "V" and computer_ip == "S":
        print("Hurray! You Won")
        return True
    elif player_ip == "S" and computer_ip == "L":
        print("Hurray! You Won")
        return True
    elif player_ip == "L" and computer_ip == "P":
        print("Hurray! You Won")
        return True
    elif player_ip == "P" and computer_ip == "V":
        print("Hurray! You Won")
        return True
    elif player_ip == "V" and computer_ip == "R":
        print("Hurray! You Won")
        return True
    elif player_ip == "R" and computer_ip == "S":
        print("Hurray! You Won")
        return True
    else:
        print("Loser, the Computer Wins !")
        return False


game()

import unittest
from RPS import *


class RPS_unit(unittest.TestCase):
    def test_player(self):
        assert player() in ['R', 'P', 'S', 'L', 'V']

    def test_computer(self):
        assert computer() in ['R', 'P', 'S', 'L', 'V']

    def test_game(self):
        assert type(game()) is bool


if __name__ == '__main__':
    unittest.main()

