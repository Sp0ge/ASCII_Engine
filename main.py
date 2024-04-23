from display import Display
from player import Player
import menu
import time

class Game(Display, Player):
    def __init__(self):
        self.game_speed=10
        self.running = True
        
        Display.__init__(self)
        
        self.local_players = [Player(self.screen_size)]
        
    def run(self):
        main_menu = menu.Main()
        
        match main_menu.show():
            case 0:
                self.game()
            case 1:
                self.local_players.append(Player(self.screen_size, controls=1))
                self.game()
            case 2:
                print('load')
                
    def game(self):
        while True:
            for player in self.local_players:
                player.update(self.display)
            self.display_show()
            time.sleep((1/self.DisplayFrequency)*self.game_speed)

            