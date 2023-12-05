class Game:

    def __init__(self, player1 = 1, player2 = 2):
        self.player1 = player1
        self.player2 = player2
        self.PlayerTurn = None
        self.list = [[' ',' ',' '],
                    [' ',' ',' '],
                    [' ',' ',' ']]
        self.input = []
        

    def DisplayGrid(self):
        
        for i, row in enumerate(self.list):
            row_letter = ' | '.join(row)
            print(row_letter)
            if i < 2:
                print('-' * 9)




    def gridInput(self, option):
        while True:
            try:
                option = int(option)
                if 1 <= option <= 9:
                    # Convert the option to grid coordinates
                    row = (option - 1) // 3
                    col = (option - 1) % 3

                    # Check if the selected cell is already taken
                    if self.list[row][col] in ("X", "O"):
                        print("Cell already taken. Please choose an empty cell.")
                    else:
                        # Update the grid with the current player's symbol
                        if self.PlayerTurn == self.player1:
                            self.list[row][col] = "X"
                        else:
                            self.list[row][col] = "O"

                        # Append the selected option to the input list
                        self.input.append(option)

                        # Display the updated grid
                        self.DisplayGrid()

                        # Mention whose turn it is
                        

                        # Check for a winner after each move
                        if self.checkBoard():
                            print(f"{self.PlayerTurn} wins!")
                            return
                        break  # Break the loop if everything is successful
                else:
                    print("Invalid option. Please choose a number between 1 and 9.")
                    option = input('Enter a valid number: ')
            except ValueError:
                print("Invalid input. Please enter a valid number.")







    def playerTurn(self):
        if self.PlayerTurn == self.player1:
            self.PlayerTurn = self.player2
        else:
            self.PlayerTurn = self.player1

        if self.checkBoard():
            print(f"Player : {self.PlayerTurn} wins!")

        print(f"It's {self.PlayerTurn}'s turn.")
        return self.PlayerTurn
    




    def playerInput(self):
        self.DisplayGrid()  # Display the grid at the start of the game
        while not self.checkBoard():
            self.playerTurn()
            player_input = input('pick a number on the grid ')
            print(f"{self.PlayerTurn} chose {player_input}")
            self.gridInput(player_input)

        # Display the final state of the board
        print("Game Over!")
        self.DisplayGrid()






    def checkBoard(self):
    # Check for a winner in rows, columns, and diagonals
        for row in self.list:
            if all(cell == "X" for cell in row) or all(cell == "O" for cell in row):
                return True

        for col in range(3):
            if all(self.list[row][col] == "X" for row in range(3)) or all(self.list[row][col] == "O" for row in range(3)):
                return True

        if all(self.list[i][i] == "X" for i in range(3)) or all(self.list[i][2 - i] == "X" for i in range(3)):
            return True
        elif all(self.list[i][i] == "O" for i in range(3)) or all(self.list[i][2 - i] == "O" for i in range(3)):
            return True

        # Check for a draw
        if all(cell == "X" or cell == "O" for row in self.list for cell in row):
            return True

        return False



    
            

GM = Game()

GM.playerInput()