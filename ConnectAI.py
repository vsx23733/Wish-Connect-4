import random 
import time
import numpy as np
import copy
import math

class Game():
    def __init__(self, n, m, q1, q2) -> None:

        self.players = [] # Store all players in a list
        self.n = n # Num of lines
        self.m = m # num of  column
        self.q1 = q1
        self.q2 = q2
        self.board = Board(self.n, self.m) # Game board to be displayed and where we will have each token
        self.game_matrix =  np.array([[0 for _ in range(m)] for _ in range(n)]) # Having our game data stored here
        pass


    def set_player(self):

        token_list = ["@", "#"]
        machine_names = ["cpu", "gpu"]

        if self.q1 == "y" and self.q2 == "y": # Player vs Player

            print("2 players required!")
            print("Player 1 will use  @  (Red) and Player 2 will use  #  (Yellow)")

            for i in range(2):
                name = input("Enter the name of the player {} : ".format(i+1))
                print("The token  {}  will be assign to you".format(token_list[i]))
                token = token_list[i]
                self.players.append(Player(name, token))

        elif self.q1 == "y" and self.q2 == "n": # Player vs Bot

            name = input("Enter your name brave player : \n")
            print("The token  {}  will be assigned to you".format(token_list[0]))
            cpu = CPU(name="cpu", token=token_list[1])
            self.players.append(Player(name, token=token_list[0]))
            self.players.append(cpu)

        else : # Bot vs Bot
            for i in range(2):
                print("The token  {}  will be assign to you the {}\n".format(token_list[i], machine_names[i]))
                token = token_list[i]
                self.players.append(CPU(machine_names[i], token))


    def ask_for_move(self, player):

        """Asking move to players"""

        if type(player) == CPU :
            count_move =  player.get_instance_count()
            if count_move <= 2:
                move = player.get_ai_token_position(self.n, self.m)
            else :
                index_player = self.players.index(player)

                if index_player == 0 : opp_player = self.players[1]
                else : opp_player = self.players[0]

                move = player.pick_best_move(self.game_matrix, self.board, player.token, player, opp_player)

        elif type(player) == Player: 
            move = player.get_token_position(self.n, self.m)
            print(f"Move after getting input of player : {move}")

        return move


    def get_authorized_move(self, player) :
        
        """Verifies if the move of the player is authorized"""

        authorized = False
        move = self.ask_for_move(player)

        while not authorized:

            print("\nGetting input of player... \n")

            try :
                print("\nChecking if the move is possible...\n")
                if self.board.is_move_possible(self.game_matrix, move[0], move[1]):
                    print(f"{player.name} is playing ({move[0]}, {move[1]})")
                    authorized =  True
                    print("Is all move good : {}".format((authorized)))
                else :
                    move = self.board.correct_move(self.game_matrix, move[0], move[1])
                    print(f"{player.name} is playing ({move[0]}, {move[1]})")
                    authorized = True
                    print("Is all move good : {}".format(authorized))

            except ValueError as e:
                print(f"Invalid input: {e}")

        return move


    def going_through(self):
        
        """Letting theame goes depending on game parameters"""

        print("Welcome to the Count4 Wish version !!")
        
        if self.q1 == "y" and self.q2 == "y":
            self.pvp()

        elif self.q1 == "y" and self.q2 == "n":
            self.pvb()

        else:
            self.bvb()


    def pvp(self):
        
        """Player vs Player"""

        if self.q1 == "y" and self.q2 == "y":
            self.set_player()
            self.board.view()
        
        player_1, player_2 = self.players
        current_player = random.choice(self.players)

        while True:
            move = self.get_authorized_move(current_player)
            grid_update = self.board.update_grid(self.game_matrix, move[0], move[1], current_player.token)
            self.board.view()

            while not grid_update:
                move = self.get_authorized_move(current_player)
                grid_update = self.board.update_grid(self.game_matrix, move[0], move[1], current_player.token)
                self.board.view()

            if self.board.is_full():
                print("This is a draw !!")
                break

            if self.board.is_win(current_player.token):
                print(f"We have a winner! Congratulations {current_player.name}!")
                break
            
            current_player = player_2 if current_player == player_1 else player_1

            pass


    def pvb(self):
        
        """Player vs CPU"""

        print("Player vs CPU")
        self.set_player()
        self.board.view()

        player, cpu = self.players
        current_player = random.choice(self.players)

        while True :
                move = self.get_authorized_move(current_player)
                grid_update = self.board.update_grid(self.game_matrix, move[0], move[1], current_player.token)
                if type(current_player) == CPU: time.sleep(1)
                self.board.view()

                while not grid_update:
                    move = self.get_authorized_move(current_player)
                    grid_update = self.board.update_grid(self.game_matrix, move[0], move[1], current_player.token)
                    self.board.view()

                if self.board.is_full():
                    print("This is a draw !!")
                    break

                if self.board.is_win(current_player.token):
                    print(f"We have a winner! Congratulations {current_player.name}!")
                    break
                
                current_player = cpu if current_player == player else player

        pass

    def bvb(self):
        
        """CPU vs GPU"""

        print("CPU vs GPU")
        self.set_player()
        self.board.view()

        cpu, gpu = self.players
        current_player = random.choice(self.players)

        while True :
                move = self.get_authorized_move(current_player)
                grid_update = self.board.update_grid(self.game_matrix, move[0], move[1], current_player.token)
                if type(current_player) == CPU: time.sleep(1)
                self.board.view()

                while not grid_update:
                    move = self.get_authorized_move(current_player)
                    grid_update = self.board.update_grid(self.game_matrix, move[0], move[1], current_player.token)
                    self.board.view()

                if self.board.is_full():
                    print("This is a draw !!")
                    break

                if self.board.is_win(current_player.token):
                    print(f"We have a winner! Congratulations {current_player.name}!")
                    break
                
                current_player = cpu if current_player == gpu else gpu

        pass


class Player():
    def __init__(self, name, token) -> None:

        self.name = name
        self.token = token

    def get_token_position(self, n, m):

        """Get where the player wants to place his token"""

        print("""\nYou have to choose the line and column number where you want to set your token\n""")

        while True:

            try:
                x = int(input("{} enter row number (0-{}): ".format(self.name, n-1)))
                y = int(input("{} Enter the column number (0-{}) : ".format(self.name, m-1)))
                if x < 0 or x >= n or y < 0 or y >= m:
                    raise ValueError("Invalid input, out of board range.")
                return [x, y]
            
            except ValueError as e:
                print(f"Invalid input: {e}. Try again.")


class CPU(Player):

    count_move = 1

    def __init__(self, name, token) -> None:
        super().__init__(name, token)

    def get_ai_token_position(self, n, m):

        """Get a random position for the AI
        Parameters : 
        n : num of rows of the game board
        m : num of columns of the game board"""

        x = np.random.randint(0, n-1)
        y = np.random.randint(0, m-1)
        print((x, y))
        CPU.count_move += 1

        return [x, y]
    
    def get_valid_positions(self, game_matrix, board):

        """Get valid locations for a set of position
        Parameters :
        Game matrix : the matrix storing our data
        Board : Actual board of the game"""

        temp_positions = [] # List of positions 

        for i in range(game_matrix.shape[0]):
            for j in range(game_matrix.shape[1]):

                if board.is_move_possible(game_matrix, x=i, y=j):
                    temp_positions.append([i, j])
                else :
                    temp_positions.append(board.correct_move(game_matrix, i, j))

        valid_positions = []

        for position in temp_positions :
            if position not in valid_positions :
                if isinstance(position, list):
                    valid_positions.append(position)
                else :
                    continue

        return valid_positions
    
    def pick_best_move(self, game_matrix, board, token, player, opp_player):

        """Using the score position in the valid locations to pick the best move"""

        CPU.count_move += 1

        print("cpu is playing ...")
        valid_positions = self.get_valid_positions(game_matrix=game_matrix, board=board)
        print(f"Valid positions : {valid_positions}")
        best_score = -1000
        best_move = [0, 0]

        """for position in valid_positions:


            temp_board = board.copy_board()
            print(f"Testing position : {position}...")
            print("\n-----------------------------------------------------------------------\n")
            print("\n-----------------------------------------------------------------------\n")
            grid_state = temp_board.update_grid(game_matrix, position[0], position[1], token)
            print("Updating temp grid...")

            if not position == None :
                if grid_state:
                    score = temp_board.score_position(position, opp_player.token)
                    print("Score got calculated\n")
                    print(f"SCORE FOR POS {position} : {score}")
                    if score > best_score:
                        best_score = score
                        best_move = position
                    print("Temp grid is updated successfully\n")
                    temp_board.view()
                else :
                    print("Grid update failed")
                    continue  

                print(f"\nMove : {best_move}")
                print(f"Score : {best_score}\n")"""

        best_move, best_score = board.minimax(board.grid, game_matrix, self, opp_player, 5, True)
        print(f"Best Move : {best_move}")
        print(f"Minimax Score : {best_score}") # Supposed to use the minimax algorithm here to make the AI undefeatable but don't work yet. 
        

        return best_move
    
    @classmethod
    def get_instance_count(cls):
        return cls.count_move
    
    pass


class Board():
    def __init__(self, n, m) -> None:

        self.n_row =  n
        self.n_col = m
        self.grid = [["-" for _ in range(self.n_col)] for _ in range(self.n_row )]
        self.shape = (n, m)

        pass

    def view(self):
        
        """View the board"""
        
        for i in range(self.n_row):
            print(f"{i} | ", end='')
            print(*self.grid[i], sep=' | ', end=f"")
            print(" |\n")
        
        print("   ", end="")
        print('   '.join([str(i) for i in range(self.n_col)]))
        pass

    def is_empty(self, i, j):

        """Check if the case is empty"""

        return self.grid[i][j] == "-"
    
    def is_full(self):

        """Check if the game board is full"""

        return all([not self.is_empty(i, j) for i in range(self.n_row) for j in range(self.n_col)])
    
    
    
    def is_win(self, token):

        """"Function which checks winning condition for a given token
        Parameters:
        token : Player's token"""

        # Check horizontal, vertical, and diagonal lines
        for r in range(self.n_row):
            for c in range(self.n_col - 3):
                if all(self.grid[r][c + i] == token for i in range(4)):
                    return True

        for r in range(self.n_row - 3):
            for c in range(self.n_col):
                if all(self.grid[r + i][c] == token for i in range(4)):
                    return True

        for r in range(self.n_row - 3):
            for c in range(self.n_col - 3):
                if all(self.grid[r + i][c + i] == token for i in range(4)):
                    return True

        for r in range(self.n_row - 3):
            for c in range(3, self.n_col):
                if all(self.grid[r + i][c - i] == token for i in range(4)):
                    return True

        return False
                
    def is_move_possible(self, game_matrix, x, y):
            
            """Cheching if the move is possible 
            Only return false when there is no filled slot under the selected slot"""
            
            n = game_matrix.shape[0] 

            if (x == n-1):
                return True
            else :
                if self.is_empty(x, y):
                    if self.is_empty(x+1, y):
                            return False
                    else : return True                

            
    def correct_move(self, game_matrix, x, y):
        
        """Applying gravity when move is not possible"""

        n = game_matrix.shape[0]
        if not self.is_move_possible(game_matrix, x, y):
            for i in range(1, n-x):
                """print(f"Is the slot ({x + i}, {y}) is free : {self.is_empty(x+i, y)}\n")"""
                if self.is_move_possible(game_matrix, x+i, y):
                    x, y = x + i, y
                    return [x, y]
        else : 
            return [x, y]
        
        pass
            

    def update_grid(self, game_matrix, x, y, token):
        
        """Function which update the game board by taking the token position of the player
        Check if the move is possible, if then update, if not raise an error"""
                
        n = game_matrix.shape[0]
        if self.is_empty(x, y):

            if self.is_move_possible(game_matrix, x, y):
                self.grid[x][y] = token
                return True

            else :
                if not self.is_move_possible(game_matrix, x, y) : 
                    x, y = self.correct_move(game_matrix, x, y)
                    self.grid[x][y] = token
                    return True
        else :
            #print(f"Position ({x}, {y}) is already occupied. Please choose another spot.")
            return False
        
    def consecutive(self, window, token):
        """
        Helper function to check if tokens in a window are contiguous
        Parameters:
        window : Combinaison of 4 consecutive slot
        token : Token of the player"""
        window_str = ''.join(window)

        return token * 2 in window_str or token * 3 in window_str or token * 4 in window_str
    
        
    def score_position(self, position, opp_token):

        """Compute the score for each position in the game_matrix
        Typically, the bot just see 1 move forward. 
        We can increase the intelligence of out bot by increasing his depth
        Parameter :
        Position : List [row_index, columns_index]"""

        score = 0
        EMPTY = "-"
        WINDOW_LENGTH = 4  
        token = self.grid[position[0]][position[1]]  
        r, c = position  

        # Horizontal Score
        row_array = self.grid[r]
        for col in range(max(0, c - (WINDOW_LENGTH - 1)), min(self.n_col - (WINDOW_LENGTH - 1), c) + 1):
            window = row_array[col:col + WINDOW_LENGTH]
            score += self.evaluate_window(window, position, opp_token)

        # Vertical Score
        col_array = [self.grid[i][c] for i in range(self.n_row)]
        for row in range(max(0, r - (WINDOW_LENGTH - 1)), min(self.n_row - (WINDOW_LENGTH - 1), r) + 1):
            window = col_array[row:row + WINDOW_LENGTH]
            score += self.evaluate_window(window, position, opp_token)

        # Positive Diagonal Score (bottom-left to top-right)
        for row in range(self.n_row - WINDOW_LENGTH + 1):  # Ensure window stays within bounds
            for col in range(self.n_col - WINDOW_LENGTH + 1):
                window = [self.grid[row + i][col + i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, position, opp_token)

        # Negative Diagonal Score (top-left to bottom-right)
        for row in range(WINDOW_LENGTH - 1, self.n_row):  # Ensure window stays within bounds
            for col in range(self.n_col - WINDOW_LENGTH + 1):
                window = [self.grid[row - i][col + i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, position, opp_token)

        return score
    
        
    def evaluate_window(self, window, position, opp_token):
        
        """Compute the score for each position tested by the machine"""

        score = 0
        EMPTY = "-"
        token = self.grid[position[0]][position[1]]  

        if window == [token] * 4:
            score += 80

        elif window.count(token) == 3 and window.count(EMPTY) == 1 and self.consecutive(window, token):
            score += 10

        elif window.count(token) == 2 and window.count(EMPTY) == 2 and self.consecutive(window, token):
            score += 3

        if window.count(opp_token) == 3 and window.count(EMPTY) == 1 and self.consecutive(window, opp_token):
            score -= 100

        return score
        
    
    def copy_board(self):

        """Return a shallow copy of the current board"""

        return copy.deepcopy(self)
    
    def terminal_node(self, game_matrix, cpu : CPU, player : Player):

        return self.is_win(cpu.token) or self.is_win(player.token) or len(cpu.get_valid_positions(game_matrix, self)) == 0
    
    def minimax(self, grid, game_matrix, cpu, player, depth, maximizingPlayer):
        """Minimax Algorithm to allow the CPU to look ahead `depth` moves."""
        
        valid_locations = cpu.get_valid_positions(game_matrix, self)
        terminal = self.terminal_node(game_matrix, cpu, player)
        
        # Check if the terminal node (win, lose, or draw)
        if depth == 0 or terminal:
            if terminal:
                if self.is_win(cpu.token):  # CPU wins
                    return (None, 10000000000000000000)
                elif self.is_win(player.token):  # Player wins
                    return (None, -10000000000000000000)
                else:  # Draw
                    return (None, 0)
            else:  # Depth is 0
                return (None, self.score_position(valid_locations[0], player.token))
        
        # Maximizing player (CPU)
        if maximizingPlayer:
            value = -math.inf
            best_position = random.choice(valid_locations)
            for position in valid_locations:
                # Simulate the move on a copy of the board
                temp_board = self.copy_board()
                temp_board.update_grid(game_matrix, position[0], position[1], cpu.token)
                
                # Recursively call minimax
                _, new_score = self.minimax(temp_board, game_matrix, cpu, player, depth-1, False)
                if new_score > value:
                    value = new_score
                    best_position = position
            return best_position, value
        
        # Minimizing player (Human Player)
        else:
            value = math.inf
            best_position = random.choice(valid_locations)
            for position in valid_locations:
                # Simulate the move on a copy of the board
                temp_board = self.copy_board()
                temp_board.update_grid(game_matrix, position[0], position[1], player.token)
                
                # Recursively call minimax
                _, new_score = self.minimax(temp_board, game_matrix, cpu, player, depth-1, True)
                if new_score < value:
                    value = new_score
                    best_position = position
            return best_position, value



def main():
    
    """Main function 
    Get game parameters
    Setup and run the game"""

    class InputRowColumnError(Exception):
        def __init__(self, n, m):
            self.n = n
            self.m = m
            self.message = f"Invalid dimensions: n = {n}, m = {m}. Rows must be > 4 and columns must be > 4."
            super().__init__(self.message)

    class ChoiceError(Exception):
        def __init__(self, q1, q2):
            self.q1 = q1
            self.q2 = q2
            self.message = f"Invalid choice: q1 = {q1}, q2 = {q2}. Choices must be either 'y' or 'n'."
            super().__init__(self.message)

    try:
        n = int(input("Enter the number of rows (n > 4): "))
        m = int(input("Enter the number of columns (m > 4): "))

        if n <= 4 or m <= 4:
            raise InputRowColumnError(n, m)

    except InputRowColumnError as e:
        print(e.message)
        exit()
    except Exception as i:
        print("An error occured")
        exit()

    try:
        q1 = input("Do you want to play? (y/n): ").lower()
        q2 = input("Do you want to play against another player? (y/n): ").lower()

        if q1 not in ['y', 'n']:
            raise ChoiceError(q1, q2)
        if q2 not in ['y', 'n']:
            raise ChoiceError(q1, q2)

    except ChoiceError as e:
        print(e.message)
        exit()

    except Exception as i:
        print("An error occured")
        exit()

    new_game = Game(n, m, q1, q2)
    new_game.going_through()
    pass

if __name__ == "__main__":
    main()
