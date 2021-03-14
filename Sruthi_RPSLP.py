import random
from random import randrange

converter = {'Rock': 0, 'Spock': 1, 'Paper': 2, 'Lizard': 3, 'Scissors': 4}
objects = {'R': 'Rock', 'V': 'Spock', 'P': 'Paper', 'L': 'Lizard', 'S': 'Scissors'}


# Retrieves the number (aka value) of the corresponding name (aka key)
def name_to_number(name):
    if name in converter.keys():
        return converter[name]
    else:
        print ("Error: There is no '" + name + "' in " + str(converter.keys()))


def player():
    flag = True
    user_input = raw_input("Player: please enter your choice")
    while flag:
        if objects.keys().__contains__(user_input):
            flag = False
            print "Valid input", objects.__getitem__(user_input)
        else:
            print "Not a valid input, enter a valid input"
    return user_input


def computer():
    computer_choice = random.choice(objects.keys())
    return computer_choice


def game():
    # converts name to player_number using name_to_number
    # compute random guess for comp_number using random.randrange()
    # compute difference of player_number and comp_number modulo five
    player_choice = objects.__getitem__(player())
    comp_choice = objects.__getitem__(computer())
    result = (name_to_number(player_choice) - name_to_number(comp_choice)) % 5
    # Announce the opponents to each other
    print 'Player chooses ' + player_choice
    print 'Computer chooses ' + comp_choice

    # Setup the game's rules
    win = result == 1 or result == 2
    lose = result == 3 or result == 4
    if win:
        print 'Player wins!\n'
        return True
    elif lose:
        print 'Computer wins!\n'
        return False
    else:
        print 'Player and computer tie!\n'
        game()


# Main Program --
print "Testing Player Assert"
assert player() in ['R', 'P', 'S', 'L', 'V']
print "Testing Computer Assert"
assert computer() in ['R', 'P', 'S', 'L', 'V']
print "Testing game bool "
assert type(game()) is bool
game()
