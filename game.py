from engine import Engine
import time
import keyboard

class Game(Engine):
    def __init__(self, size=[75,25]):
        Engine.__init__(self, size=size)
    
    def run(self):
        while self.running:
            self.check_events()
            self.display_show()
            time.sleep(self.delay)
    
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
            if new_pos[0] < len(self.map)-1: 
                pos[0]= new_pos[0]
            
        if keyboard.is_pressed("d"):
            new_pos[1] = pos[1] + speed
            if new_pos[1] < len(self.map[0])-1:
                pos[1]= new_pos[1]
                
        # if keyboard.is_pressed("e"):
        #     new_pos[1] = pos[1] + speed
        #     if new_pos[1] < len(self.map[0])-1:
        #         pos[1]= new_pos[1]
                
        self.players[0].set_pos(pos)
        self.map_update()