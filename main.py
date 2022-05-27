import random       # RANDOM PICKING OF NUMBERS


# FUNCTION: MAIN MENU
def main_menu():
    print("*********************************************************")
    print("*             ROCK-PAPER-SCISSORS GAME                  *")
    print("*********************************************************")
    print("")

    while True:
        try:
            print("1. SINGLE PLAYER")
            print("2. PASS AND PLAY")
            print("3. EXIT")
            print("---------")
            menuChoice = int(input("Choice: "))


            if menuChoice == 1:
                single_player()
            elif menuChoice == 2:
                pass_play()
            elif menuChoice == 3:
                exit_program()
            else:
                print("\n")
                print("> INVALID INPUT! Choose between 1 - 3 only!")
                print("\n")
        except ValueError:
            print("\n")
            print("> INVALID INPUT! Characters and symbols are not accepted")
            print("\n")





# FUNCTION: SINGLE PLAYER MODE
def single_player():
    print("\n\n\n")
    print("==============================")
    print("     SINGLE PLAYER MODE")
    print("==============================")
    print("")


    p1 = player1_input()                    # Call the function and assign the returned input to 'p1'

    # Player 2 random input
    rpsRandomizer = ['r', 'p', 's', 'R', 'P', 'S']
    player2 = random.choice(rpsRandomizer)
    print("[BOT] Player 2's turn =")
    print("\tR-P-S?:   ", player2)

    who_wins(p1, player2)

    print("Do you want to play again? [y/n]")
    print("---------")
    optionChoice = (input("Choice: "))

    if optionChoice == 'y' or optionChoice == 'Y':
        single_player()
    elif optionChoice == 'n' or optionChoice == 'N':
        main_menu()
    else:
        print("\n")
        print("> INVALID INPUT")
        print("\n")





# FUNCTION: PASS AND PLAY MODE
def pass_play():
    print("\n\n\n")
    print("==============================")
    print("     PASS AND PLAY MODE")
    print("==============================")
    print("")


    p1 = player1_input()                    # Call the function and assign the returned input to 'p1'
    p2 = player2_input()                    # Call the function and assign the returned input to 'p1'
    who_wins(p1, p2)

    print("Do you want to play again? [y/n]")
    print("---------")
    optionChoice = (input("Choice: "))

    if optionChoice == 'y' or optionChoice == 'Y':
        pass_play()
    elif optionChoice == 'n' or optionChoice == 'N':
        main_menu()
    else:
        print("\n")
        print("> INVALID INPUT")
        print("\n")





# FUNCTION: PLAYER 01
def player1_input():
    flag = False

    # Loop until input is either r-p-s
    while not flag:
        # Input
        print("Player 1's turn =")
        player1 = (input("\tR-P-S?:   "))

        player1 = player1.lower()                   # Convert uppercase char into lowercase char

        if player1 == 'r' or player1 == 'p' or player1 == 's':
            flag = True
            return player1





# FUNCTION: PLAYER 02
def player2_input():
    flag = False

    # Loop until input is either r-p-s
    while not flag:
        # Input
        print("Player 2's turn =")
        player2 = (input("\tR-P-S?:   "))

        player2 = player2.lower()                    # Convert uppercase char into lowercase char

        if player2 == 'r' or player2 == 'p' or player2 == 's':
            flag = True
            return player2





# FUNCTION: R-P-S WINNER ALGORITHM
def who_wins(player1, player2):
    print("\n")

    # Determine who wins the match
    if player1 == player2:
        print(">> DRAW!")
    elif player1 == 'r':
        if player2 == 'p':
            print(">> PLAYER 2 WINS!")
        elif player2 == 's':
            print(">>PLAYER 1 WINS!")
    elif player1 == 'p':
        if player2 == 's':
            print(">> PLAYER 2 WINS!")
        elif player2 == 'r':
            print(">> PLAYER 1 WINS!")
    elif player1 == 's':
        if player2 == 'r':
            print(">> PLAYER 2 WINS!")
        elif player2 == 'p':
            print(">> PLAYER 1 WINS!")
    print("\n")





# FUNCTION: EXIT
def exit_program():
    print("PROGRAM EXITED")
    exit()





"""""
    MAIN CODE 
"""""
# Start program
main_menu()
