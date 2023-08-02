from colorama import Fore


def main():
    def find_indices(list_to_check, item_to_find):
        indices = []
        for idx, value in enumerate(list_to_check):
            if value == item_to_find:
                indices.append(idx)
        return indices


    # declare colors
    # color of the cells
    cellscolor = Fore.LIGHTBLACK_EX
    xcolor = Fore.LIGHTMAGENTA_EX
    ocolor = Fore.LIGHTBLUE_EX


    def printboard(boardlist):
        # updation the tick tac toe board
        line = "║ "
        print(cellscolor + f"╔═══╦═══╦═══╗")
        for i in range(0, 9):
            if (boardlist[i][1] != 1):
                boardlist[i] = (str(i), None)
                # boardlist[i] = (" ",None)

            # rebuild the line based on color of the cell and X or O
            if boardlist[i][1] == 1 and boardlist[i][0] == 'X':
                line += xcolor + boardlist[i][0] + cellscolor + " ║ "
            elif boardlist[i][1] == 1 and boardlist[i][0] == 'O':
                line += ocolor + boardlist[i][0] + cellscolor + " ║ "
            else:
                line += boardlist[i][0] + " ║ "

            if ((i+1) % 3 == 0):
                print(line)
                if (i+1) != 9:
                    print(cellscolor + f"╠═══╬═══╬═══╣")
                else:
                    print(cellscolor + f"╚═══╩═══╩═══╝")
                line = "║ "

    # checking for win | draw
    def checkwin(boardlist):

        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        playerX_indices = find_indices(boardlist, ('X', 1))
        playerO_indices = find_indices(boardlist, ('O', 1))

        # check if any of wins item is a subset of playerX_indices or playerO_indices [check win for X or O]
        if any(set(win).issubset(playerX_indices) for win in wins):
            printboard(boardlist)
            print(Fore.LIGHTYELLOW_EX, "X Won the match")
            return True
        elif any(set(win).issubset(playerO_indices) for win in wins):
            printboard(boardlist)
            print(Fore.LIGHTYELLOW_EX, "O Won the match")
            return True
        else:
            # check if all cells are filled and no one has won [draw]
            if all(boardlist[i][1] == 1 for i in range(9)):
                printboard(boardlist)
                print(Fore.LIGHTYELLOW_EX, "Match Draw")
                return True

        return False


    # prompt from players
    if __name__ == "__main__":

        boardlist = [("player", str(x)) for x in range(9)]

        players = ["O", "X"]
        colors = [ocolor, xcolor]
        turn = True  # 1 for X and 0 for O

        print(Fore.LIGHTYELLOW_EX + "Welcome to Tic Tac Toe")
        while (True):
            printboard(boardlist)

            print(colors[turn] + f"{players[turn]}'s Chance")

            value = int(input(colors[turn] + "Please enter a value: "))
            # check if the value is already taken
            if (boardlist[value][1] == None):
                boardlist[value] = (players[turn], 1)
            else:
                print(Fore.LIGHTMAGENTA_EX, "Value already taken")
                continue

            if (checkwin(boardlist)):
                print("Match over")
                answer = str(input('Want to play again? (y/n): '))
                if answer == 'n':
                    print("Goodbye")
                    break
                elif answer == 'y':
                    # restart_program!!!
                    main()
                else:
                    print ("Invalid input.")

            turn = not turn
main()