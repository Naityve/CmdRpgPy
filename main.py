from naityveUtils import NaityveUtils
import msvcrt
import random

# map size
height = 15
width = 25

# player spawn location
player_row = 1
player_col = 1

def print_map():
    NaityveUtils.clear_console()
    for i in range(height):
        for j in range(width):
            if i == player_row and j == player_col:
                print('@', end='')
            else:
                print(gameMap[i][j], end='')
        print()

# loot spawner
def spawn_question_marks():
    for _ in range(2):
        while True:
            x = random.randint(1, width - 2)
            y = random.randint(1, height - 2)
            if gameMap[y][x] == '/' and (x != player_col or y != player_row):
                gameMap[y][x] = '?'
                break

# Create the game map
gameMap = [['#' if i == 0 or i == height - 1 or j == 0 or j == width - 1 else '/' for j in range(width)] for i in range(height)]

# Initial map display
spawn_question_marks()
print_map()

# Game loop
while True:
    # Check if a key is pressed (non-blocking)
    message = ""
    if msvcrt.kbhit():
        move = msvcrt.getch().decode('utf-8')  # Get the pressed key
        
        if move == 'w':
            if gameMap[player_row - 1][player_col] == "?" :
                gameMap[player_row][player_col] = '/'
                player_row -= 1
                gameMap[player_row][player_col] = '@'
                message = "You picked up a small key."
            elif player_row > 1 and gameMap[player_row - 1][player_col] != '#':
                gameMap[player_row][player_col] = '/'
                player_row -= 1
                gameMap[player_row][player_col] = '@'
                message = "You move one unit north."
            else:
                message = "Cannot move up. There's a wall." # need to fix gets cleared
        elif move == 's':
            if gameMap[player_row + 1][player_col] == "?" :
                gameMap[player_row][player_col] = '/'
                player_row += 1
                gameMap[player_row][player_col] = '@'
                message = "You picked up a small key."
            elif player_row < height - 2 and gameMap[player_row + 1][player_col] != '#':
                gameMap[player_row][player_col] = '/'
                player_row += 1
                gameMap[player_row][player_col] = '@'
                message = "You move one unit south."
            else:
                message = "Cannot move down. There's a wall." # need to fix gets cleared
        elif move == 'a':
            if gameMap[player_row][player_col - 1] == "?" :
                gameMap[player_row][player_col] = '/'
                player_col -= 1
                gameMap[player_row][player_col] = '@'
                message = "You picked up a small key."
            elif player_col > 1 and gameMap[player_row][player_col - 1] != '#':
                gameMap[player_row][player_col] = '/'
                player_col -= 1
                gameMap[player_row][player_col] = '@'
                message = "You move one unit west."
            else:
                message = "Cannot move left. There's a wall." # need to fix gets cleared
        elif move == 'd':
            if gameMap[player_row][player_col + 1] == "?" :
                gameMap[player_row][player_col] = '/'
                player_col += 1
                gameMap[player_row][player_col] = '@'
                message = "You picked up a small key."
            elif player_col < width - 2 and gameMap[player_row][player_col + 1] != '#':
                gameMap[player_row][player_col] = '/'
                player_col += 1
                gameMap[player_row][player_col] = '@'
                message = "You move one unit east."
            else:
                message = "Cannot move right. There's a wall." # need to fix gets cleared
        elif move == 'q':
            NaityveUtils.clear_console()
            break

        # update map
        print_map()
        print(message)
