from display import Display
from player import Player
import menu

class Game(Display, Player):
    def __init__(self):
        self.running = True
        
        Display.__init__(self)
        
    def run(self):
        main_menu = menu.Main()
        main_menu.show()