#Made for Windows (as it uses Windows-specific commands such as 'cls'
# and Windows-specific color codes instead of ANSI escape codes
import os
import time

grid_value = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def place_symbol(grid_map,symb,grid_value):
    """
        Argument (as String): grid map, symbol of player, value of grids

        Input (as Integer): Position to place symbol

        It places given symbol at given position and displays updated grid 

        Returns: Value of grids
    """
    print(grid_map)

    print(f'''
         {grid_value[0]}  |  {grid_value[1]}  |  {grid_value[2]}
       _____ _____ _____
         {grid_value[3]}  |  {grid_value[4]}  |  {grid_value[5]}
       _____ _____ _____
         {grid_value[6]}  |  {grid_value[7]}  |  {grid_value[8]}
    ''')

    user_in = input("Enter position (1-9): ")
    if user_in == "1" and grid_value[0] == " ":
        grid_value[0] = symb
    elif user_in == "2" and grid_value[1] == " ":
        grid_value[1] = symb
    elif user_in == "3" and grid_value[2] == " ":
        grid_value[2] = symb
    elif user_in == "4" and grid_value[3] == " ":
        grid_value[3] = symb
    elif user_in == "5" and grid_value[4] == " ":
        grid_value[4] = symb
    elif user_in == "6" and grid_value[5] == " ":
        grid_value[5] = symb
    elif user_in == "7" and grid_value[6] == " ":
        grid_value[6] = symb
    elif user_in == "8" and grid_value[7] == " ":
        grid_value[7] = symb
    elif user_in == "9" and grid_value[8] == " ":
        grid_value[8] = symb
    else:
        print("Invalid position!")

    print(f'''
         {grid_value[0]}  |  {grid_value[1]}  |  {grid_value[2]}
       _____ _____ _____
         {grid_value[3]}  |  {grid_value[4]}  |  {grid_value[5]}
       _____ _____ _____
         {grid_value[6]}  |  {grid_value[7]}  |  {grid_value[8]}
    ''')

    return grid_value

def win(grid_value):
    """
        Argument (as String): value of grids

        Input : None

        It compares grid values and grid value to symbol(X/O), if they satisfy winning condition or tie condition then it returns the corresponding result
        
        Winning condition: Same symbol in the following grid position combinations
            - 012, 345, 678 (horizontal)
            - 036, 147, 258 (vertical)
            - 048, 246 (diagonal)
        Tie condition: No " " symbol in grid and no same symbol in above grid position combination

        Returns: "X" if above condition is satisfied & symbol is "X"
                 "O" if above condition is satisfied & symbol is not "X", i.e. "O"
                 "True" if Tie condition is satisfied
                 False if NO condition is satisfied
    """
    # 012, 345, 678 (horizontal)
    if grid_value[0] == grid_value[1] == grid_value[2] != " ": #1
        if grid_value[0] == "X":
            return "X"
        else:
            return "O"

    elif grid_value[3] == grid_value[4] == grid_value[5] != " ": #2
        if grid_value[3] == "X":
            return "X"
        else:
            return "O"

    elif grid_value[6] == grid_value[7] == grid_value[8] != " ": #3
        if grid_value[6] == "X":
            return "X"
        else:
            return "O"
    
    # 036, 147, 258 (vertical)
    if grid_value[0] == grid_value[3] == grid_value[6] != " ": #1
        if grid_value[0] == "X":
            return "X"
        else:
            return "O"

    elif grid_value[1] == grid_value[4] == grid_value[7] != " ": #2
        if grid_value[1] == "X":
            return "X"
        else:
            return "O"

    elif grid_value[2] == grid_value[5] == grid_value[8] != " ": #3
        if grid_value[2] == "X":
            return "X"
        else:
            return "O"

    # 048, 246 (diagonal)
    if grid_value[0] == grid_value[4] == grid_value[8] != " ": #1
        if grid_value[0] == "X":
            return "X"
        else:
            return "O"

    elif grid_value[2] == grid_value[4] == grid_value[6] != " ": #2
        if grid_value[2] == "X":
            return "X"
        else:
            return "O"
    
    #TIE
    if " " not in grid_value and state_win_tie == False:
        return "True"

    return False #if no winner

def execute_game(state_win_tie):
    while not state_win_tie:
        for name,symbol in zip([player1,player2], ["X","O"]):
            if symbol == "X":
                os.system("color 01") #Player X -> blue
            else:
                os.system("color 02") #Player O -> green

            print(f"\n\n{name}'s turn: (Symbol: {symbol})")
            place_symbol(grid_map,symbol,grid_value)

            time.sleep(1)
            os.system("cls") 
            
            state_win_tie = win(grid_value)
            
            if state_win_tie == "X": 
                game_end = f"\n\t\t*** {player1} is winner!! ***"
            elif state_win_tie == "O":
                game_end = f"\n\t\t*** {player2} is winner!! ***"
            elif state_win_tie == "True":
                game_end = f"\n\t\t*** It is a Tie!! ***"

            if state_win_tie or state_win_tie == "True": #if state is X/O(True) or "True"(Tie)
                for color in color_list:
                    os.system(f"color {color}")
                    print(f'''
                          {grid_value[0]}  |  {grid_value[1]}  |  {grid_value[2]}
                        _____ _____ _____
                          {grid_value[3]}  |  {grid_value[4]}  |  {grid_value[5]}
                        _____ _____ _____
                          {grid_value[6]}  |  {grid_value[7]}  |  {grid_value[8]}
                    ''')
                    print(game_end)

                    time.sleep(1)
                    os.system("cls")
                break

welcome_mssg = '''
    ____ WELCOME TO TIC-TAC-TOE ____\n
Symbol for Player 1 is 'X'
Symbol for Player 2 is 'O'\n
To play the game ENTER NUMBER POSITION 
as shown in the MAP to place your symbol
'''

grid_map = '''
   ** MAP **
  1  |  2  |  3
_____ _____ _____
  4  |  5  |  6 
_____ _____ _____
  7  |  8  |  9 
'''

print(welcome_mssg)

color_list = ["01","02","03","04","05","06"] #blue, green, cyan/aqua, red, magenta/purple, yellow

player1 = input("Enter player 1 name: ").title()
player2 = input("Enter player 2 name: ").title()

while True:
    try:
        play = input("\nPlay? Yes(Y) / No(N): ").upper()
        if play == "Y":
            grid_value = [" "] * 9
            state_win_tie = False
            execute_game(state_win_tie)
        elif play == "N":
            print("Thanks!")
            break
        else:
            raise Exception("Please enter a valid choice")
    except Exception as e:
        print(f"Error: {e}")
