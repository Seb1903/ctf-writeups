#
# Text based snake and ladder game
# Author - https://www.pythoncircle.com
#

import time
import random
import sys

# just of effects. add a delay of 1 second before performing any action
SLEEP_BETWEEN_ACTIONS = 1
MAX_VAL = 100
DICE_FACE = 6

# snake takes you down from 'key' to 'value'
snakes = {
    96:61,
    95:86,
    88:55,
    92:51,
    77:39,
    60:15,
    27:7,
    32:11,
    21:17,
    54:1
}

# ladder takes you up from 'key' to 'value'
ladders = {
    4:26,
    8:30,
    24:38,
    28:47,
    31:49,
    57:66,
    58:62,
    53:72,
    76:97,
    80:99
}

player_turn_text = [
    "Your turn.",
    "Go.",
    "Please proceed.",
    "Lets win this.",
    "Are you ready?",
    "",
]

snake_bite = [
    "boohoo",
    "bummer",
    "snake bite",
    "oh no",
    "dang"
]

ladder_jump = [
    "woohoo",
    "woww",
    "nailed it",
    "oh my God...",
    "yaayyy"
]


def welcome_msg():
    msg = """
    Welcome to Snake and Ladder Game.
    Version: 1.0.0
    Developed by: https://www.pythoncircle.com
    
    Rules:
      1. Initally both the players are at starting position i.e. 0. 
         Take it in turns to roll the dice. 
         Move forward the number of spaces shown on the dice.
      2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
      3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
      4. The first player to get to the FINAL position is the winner.
      5. Hit enter to roll the dice.
    
    """
    print(msg)


def get_player_names():
    player1_name = None
    while not player1_name:
        player1_name = input("Please enter a valid name for first player: ").strip()

    player2_name = None
    while not player2_name:
        player2_name = input("Please enter a valid name for second player: ").strip()

    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
    return player1_name, player2_name


def get_dice_value():
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    dice_value = random.randint(1, DICE_FACE)
    print("Its a " + str(dice_value))
    return dice_value


def got_snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
    print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))


def got_ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump).upper() + " ########")
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


def snake_ladder(player_name, current_value, dice_value):
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value


def check_win(player_name, position):
    if MAX_VAL == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing the game. Please visit https://www.pythoncircle.com\n\n")
        sys.exit(1)


def start():
    welcome_msg()

    player1_name, player2_name = get_player_names()


    player1_current_position = 0
    player2_current_position = 0
    i = 0
    movelist = [5, 1, 6, 6, 3, 1, 6, 5, 1, 1, 2, 2, 4, 2, 5, 5, 6, 1, 6, 4, 1, 2, 3, 4, 1, 3, 3, 3, 6, 2, 6, 1, 1, 4, 6, 1, 2, 6, 6, 5, 5, 3, 5, 2, 2, 1, 6, 1, 3, 6, 5, 4, 3, 6, 4, 4, 4, 1, 5, 1, 6, 6, 3, 1, 6, 5, 1, 1, 2, 2, 4, 2, 5, 5, 6, 1, 6, 4, 1, 2, 3, 4, 1, 3, 3, 3, 6, 2, 6, 1, 1, 4, 6, 1, 2, 6, 6, 5, 5, 3]
    moves_done = []
    while True:
        
        #input_1 = input("\n" + player1_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        dice_value = movelist[i]
        i+=1 
        player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)

        check_win(player1_name, player1_current_position)
        moves_done.append(player1_current_position)
        #input_2 = input("\n" + player2_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        dice_value = movelist[i]
        i+=1
        player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)
        moves_done.append(player2_current_position)
        check_win(player2_name, player2_current_position)
        

        print(moves_done)



if __name__ == "__main__":
    start()