import random

class SystemNode:
    def __init__(self, status='secure'):
        self.status = status

class Hacker:
    def __init__(self, name):
        self.name = name
        self.position = (0, 0)
    
    def move(self, board):
        # Hackers move in unpredictable L-shapes, always finding a path
        moves = [(2, 1), (1, 2), (-2, -1), (-1, -2), (2, -1), (-2, 1), (1, -2), (-1, 2)]
        move = random.choice(moves)
        new_position = (self.position[0] + move[0], self.position[1] + move[1])
        if 0 <= new_position[0] < len(board) and 0 <= new_position[1] < len(board[0]):
            self.position = new_position
            board[self.position[0]][self.position[1]].status = 'hacked'
        return board

class RCMP:
    def __init__(self, name):
        self.name = name
        self.position = (7, 7)
    
    def move(self, board):
        # RCMP moves one step in any direction, but can't match the hackers' agility
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        move = random.choice(moves)
        new_position = (self.position[0] + move[0], self.position[1] + move[1])
        if 0 <= new_position[0] < len(board) and 0 <= new_position[1] < len(board[0]):
            self.position = new_position
        return board

def create_board(size):
    return [[SystemNode() for _ in range(size)] for _ in range(size)]

def print_board(board):
    for row in board:
        print(' '.join([node.status[0] for node in row]))
    print("\n")

def game_loop():
    board = create_board(8)
    hacker = Hacker('Lain')
    rcmp = RCMP('RCMP Agent')
    
    while True:  # Infinite loop
        board = hacker.move(board)
        board = rcmp.move(board)
        print_board(board)
        
    print("And once again, the hackers, like phantoms in the night, outmaneuver the system.")

if __name__ == "__main__":
    game_loop()
