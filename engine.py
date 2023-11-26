from player import Player
import time
import keyboard
from reprint import output

class Engine(object):
    def __init__(self, size_x=20, size_y=10):
        self.running = True
        
        self.size_x=int(size_x)
        self.size_y=int(size_y)
        
        self.players = []
        self.add_player()
        
        self.map = self.map_gen()
        
        with output(initial_len=self.size_y, interval=0) as out_lines:
            self.display = out_lines
        
    def run(self):
        while self.running:
            self.check_events()
            self.display_show()
            time.sleep(0.05)
    
    def check_events(self):
        pos = self.players[0].get_pos()
        new_pos = [0,0]
        speed=self.players[0].speed
        
        if keyboard.is_pressed("w"):
            new_pos[0] = pos[0] - speed
            if new_pos[0] > 0: 
                pos[0] = new_pos[0]
                
            
        if keyboard.is_pressed("a"):
            new_pos[1] = pos[1] - speed
            if new_pos[1] > 0: 
                pos[1]= new_pos[1]
            
        if keyboard.is_pressed("s"):
            new_pos[0] = pos[0] + speed
            if new_pos[0] < len(self.map)-2: 
                pos[0]= new_pos[0]
            
        if keyboard.is_pressed("d"):
            new_pos[1] = pos[1] + speed
            if new_pos[1] < len(self.map[0])-1:
                pos[1]= new_pos[1]
                
        self.players[0].set_pos(pos)
        self.map_update()
    
    def add_player(self):
        self.players.append(Player(name=f"player_{len(self.players)+1}"))
    
    def show_players(self, input_display):
        for player in self.players:
            input_display[player.get_pos()[0]][player.get_pos()[1]]=player.skin
        return input_display
    
    def map_gen(self):
        map = list()
        for line in range(self.size_y):
            l = list()
            for char in range(self.size_x):
                l.append("_")
            map.append(l)
        return map
    
    def map_update(self):
        self.map = self.map_gen()
    
    def display_gen(self):
        display = self.map
        display = self.show_players(display)
        return display
    
    def display_show(self):
        display = self.display_gen()
        lines = 0
        for line in range(len(display)-1):
            string = str()
            for char in display[line]:
                string += str(char)
            self.display[lines] = string
            lines += 1
                

