class Game:
    def __init__(self, board, player_one, player_two):
        self._player_one = player_one
        self._player_two = player_two
        self.board = board

class Board:
    def __init__(self):
        self.state = [['?', '?', '?'], 
        ['?', '?', '?'], 
        ['?', '?', '?']]

    def render_board(self):
        print(self.state)

class Player:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


bob = Player('bob')    
fred = Player('fred')    
board = Board()

game = Game(board, bob, fred)



