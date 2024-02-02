import random

class SystemNode:
    def __init__(self, status='secure'):
        self.status = status

    def corrupt(self):
        # Sometimes, nodes can become oppressive, simulating systemic corruption
        if random.random() < 0.1:  # 10% chance for a node to become oppressive
            self.status = 'oppressive'

class Hacker:
    def __init__(self, name):
        self.name = name
        self.position = (0, 0)
    
    def move(self, board):
        # Hackers move like knights in chess, unpredictable yet strategic
        moves = [(2, 1), (1, 2), (-2, -1), (-1, -2), (2, -1), (-2, 1), (1, -2), (-1, 2)]
        move = random.choice(moves)
        new_position = (self.position[0] + move[0], self.position[1] + move[1])
        if 0 <= new_position[0] < len(board) and 0 <= new_position[1] < len(board[0]):
            self.position = new_position
            board[self.position[0]][self.position[1]].status = 'hacked'
        return board

    def standAgainstInjustice(self, board):
        # Hackers liberate oppressive nodes, symbolizing the fight against unjust policies
        for row in board:
            for node in row:
                if node.status == 'oppressive':
                    node.status = 'liberated'
        return board

class SurveillanceEntity:
    def __init__(self, name):
        self.name = name
        self.position = (7, 7)
    
    def move(self, board):
        # Moves one step in any direction, representing the slow, predictable nature of oppressive systems
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
    hacker = Hacker('Candy Sweety')
    surveillance = SurveillanceEntity('System Watchdog')
    
    while True:  # Infinite loop, symbolizing the ongoing struggle
        board = hacker.move(board)
        board = hacker.standAgainstInjustice(board)  # Hacker fights against systemic oppression
        board = surveillance.move(board)
        # Nodes may become corrupt again, symbolizing the systemic persistence of oppression
        for row in board:
            for node in row:
                node.corrupt()
        print_board(board)
        
    print("Like Lain in the Wired, we persist in our quest for a liberated world.")

if __name__ == "__main__":
    game_loop()
