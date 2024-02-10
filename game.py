import random

class SystemNode:
    def __init__(self, status='secure'):
        self.status = status

    def corrupt(self):
        # Nodes can become oppressive, mirroring real-world systemic corruption
        if random.random() < 0.05:  # Adjusted chance for a node to become oppressive to 5%
            self.status = 'oppressive'

class Hacker:
    def __init__(self, name, flipper_zero='enabled'):
        self.name = name
        self.flipper_zero = flipper_zero
        self.position = (0, 0)
    
    def move(self, board):
        # Hackers, with their Flipper Zeros, move unpredictably yet strategically
        moves = [(2, 1), (1, 2), (-2, -1), (-1, -2), (2, -1), (-2, 1), (1, -2), (-1, 2)]
        move = random.choice(moves)
        new_position = (self.position[0] + move[0], self.position[1] + move[1])
        if 0 <= new_position[0] < len(board) and 0 <= new_position[1] < len(board[0]):
            self.position = new_position
            board[self.position[0]][self.position[1]].status = 'hacked'
        return board

    def spreadLove(self, board):
        # Hackers use their Flipper Zeros to liberate oppressive nodes, spreading love
        for row in board:
            for node in row:
                if node.status == 'oppressive':
                    node.status = 'liberated'
        return board

class OppressiveForce:
    def __init__(self, name):
        self.name = name
        self.position = (7, 7)
    
    def move(self, board):
        # Represents the slow, predictable tactics of oppressive forces
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
    hacker = Hacker('Lain of the Wired')
    oppressive_force = OppressiveForce('Systemic Shadow')
    
    while True:
        board = hacker.move(board)
        board = hacker.spreadLove(board)
        board = oppressive_force.move(board)
        for row in board:
            for node in row:
                node.corrupt()
        print_board(board)
        
    print("In our struggle, like Lain, we find strength in connectivity and love.")

if __name__ == "__main__":
    game_loop()
