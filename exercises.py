class Game:
    def __init__(self):
        self.turn = 'X' 
        self.tie = False 
        self.winner = None 
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None
        }

    def print_board(self):
        b = self.board
        print(f"""
A B C
1) {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
----------
2) {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
----------
3) {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
""")

    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input("Enter a valid move (example: A1): ").lower()
            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn
                break
            else:
                print("Invalid move! That space is either taken or doesn't exist.")

    def check_for_winner(self):
        for row in ['1', '2', '3']:
            if (self.board[f'a{row}'] and 
                self.board[f'a{row}'] == self.board[f'b{row}'] == self.board[f'c{row}']):
                self.winner = self.board[f'a{row}']
                return

        for col in ['a', 'b', 'c']:
            if (self.board[f'{col}1'] and 
                self.board[f'{col}1'] == self.board[f'{col}2'] == self.board[f'{col}3']):
                self.winner = self.board[f'{col}1']
                return

        if (self.board['a1'] and 
            self.board['a1'] == self.board['b2'] == self.board['c3']):
            self.winner = self.board['a1']
            return

        if (self.board['c1'] and 
            self.board['c1'] == self.board['b2'] == self.board['a3']):
            self.winner = self.board['c1']
            return
        
    def check_for_tie(self):
        if not self.winner and all(value is not None for value in self.board.values()):
            self.tie = True

    def switch_turn(self):
        turn_dict = {'X': 'O', 'O': 'X'}
        self.turn = turn_dict[self.turn]

    def play_game(self):
        print("\nShall we play a game?")
        
        while not (self.winner or self.tie):
            self.render()
            self.get_move()
            self.check_for_winner()
            if not self.winner:
                self.check_for_tie()
            if not (self.winner or self.tie):
                self.switch_turn()
        
        self.render()

if __name__ == "__main__":
    game = Game()
    game.play_game()