# Game_Design
'''
Game Rules
    Scissors cuts Paper
    Paper covers Rock
    Rock crushes Lizard
    Lizard poisons Spock
    Spock smashes Scissors
    Scissors decapitates Lizard
    Lizard eats Paper
    Paper disproves Spock
    Spock vaporizes Rock
    Rock crushes Scissor

Objects are entered by abbreviation: Rock (R), Paper (P), Scissors (S), Lizard (L), Spock (V)
'''


def player() -> str:
    # ask user to input objects
    # check if the input is valid
    # if the input is valid, return a string that represents the object
    # else print out error message and keep asking until getting a vaild input



def computer() -> str:
    # randomly picks an object and return the string
    


def game() -> bool:
    # return True if player wins else False
    # if a tie happens, the process is repeated until a winner is found
    # print out messages for each round
    # print out winner if found and return bool
    


# unit test of outputs for functions
assert player() in ['R','P','S','L','V']
assert computer() in ['R','P','S','L','V']
assert type(game()) is bool
