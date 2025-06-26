#A simple console-based Tic Tac Toe game for 2 players, developed using basic programming concepts like variables, datatypes, conditional & looping statements, functions

def place_symbol(grid_map,symb,grid_value):
    """
        Argument (as String): grid map, symbol of player, value of grids

        Input (as Integer): Position to place symbol

        It places given symbol at given position and displays updated grid 

        Returns: Value of grids
    """
    print(grid_map)
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

def win(grid_value,player1, player2):
    """
        Argument (as String): value of grids, names of players

        Input : None

        It compares grid values and grid value to symbol(X/O), if they satisfy winning condition or tie condition then it displays the corresponding result
        
        Winning condition: Same symbol in the following grid position combinations
            - 012, 345, 678 (horizontal)
            - 036, 147, 258 (vertical)
            - 048, 246 (diagonal)
        Tie condition: No " " symbol in grid and no same symbol in above grid position combination

        Returns: True if one of the above condition is satisfied
                 False if NO condition is satisfied
    """
    # 012, 345, 678 (horizontal)
    if grid_value[0] == grid_value[1] == grid_value[2] != " ": #1
        if grid_value[0] == "X":
            print(f"\n\t{player1} is winner!!")
        else:
            print(f"\n\t{player2} is winner!!")
        return True

    elif grid_value[3] == grid_value[4] == grid_value[5] != " ": #2
        if grid_value[3] == "X":
            print(f"\n{player1} is winner!!")
        else:
            print(f"\n{player2} is winner!!")
        return True

    elif grid_value[6] == grid_value[7] == grid_value[8] != " ": #3
        if grid_value[6] == "X":
            print(f"\n{player1} is winner!!")
        else:
            print(f"\n{player2} is winner!!")
        return True
    
    # 036, 147, 258 (vertical)
    if grid_value[0] == grid_value[3] == grid_value[6] != " ": #1
        if grid_value[0] == "X":
            print(f"\n{player1} is winner!!")
        else:
            print(f"\n{player2} is winner!!")
        return True

    elif grid_value[1] == grid_value[4] == grid_value[7] != " ": #2
        if grid_value[1] == "X":
            print(f"\n{player1} is winner!!")
        else:
            print(f"\n{player2} is winner!!")
        return True

    elif grid_value[2] == grid_value[5] == grid_value[8] != " ": #3
        if grid_value[2] == "X":
            print(f"\n{player1} is winner!!")
        else:
            print(f"\n{player2} is winner!!")
        return True

    # 048, 246 (diagonal)
    if grid_value[0] == grid_value[4] == grid_value[8] != " ": #1
        if grid_value[0] == "X":
            print(f"\n{player1} is winner!!")
        else:
            print(f"\n{player2} is winner!!")
        return True

    elif grid_value[2] == grid_value[4] == grid_value[6] != " ": #2
        if grid_value[2] == "X":
            print(f"\n{player1} is winner!!")
        else:
            print(f"\n{player2} is winner!!")
        return True
    
    #TIE
    if " " not in grid_value and state_win_tie == False:
        print("\nIt's a Tie!")
        return True

    return False #if no winner

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

grid_value = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

state_win_tie = False

player1 = input("Enter player 1 name: ")
player2 = input("Enter player 2 name: ")

while not state_win_tie:
    for name,symbol in zip([player1,player2], ["X","O"]):
        print(f"\n\n{name}'s turn: (Symbol: {symbol})")
        place_symbol(grid_map,symbol,grid_value)
        state_win_tie = win(grid_value, player1, player2)
        
        if state_win_tie == True:
            break
