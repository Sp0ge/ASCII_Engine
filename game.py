from engine import Engine
from prop import Prop
import time
import os
import keyboard

class Game(Engine):
    def __init__(self, size, name, server=False):
        Engine.__init__(self, size=size, name=name, server=server)
    
    def game_run(self, ip=None, port=25097):
        while self.running:
            self.check_events()
            self.display_show()
            time.sleep(self.delay)
        
    
    def check_events(self):
        if len(self.map) > 2:
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
                
            if keyboard.is_pressed("e"):
                self.players[0].action=True
            else:
                self.players[0].action=False
            
            if self.players[0].bullets > 0:
                if keyboard.is_pressed("left arrow"):
                    self.entities.append(self.players[0].shooting(0, self.objects))    

                elif keyboard.is_pressed("right arrow"):
                    self.entities.append(self.players[0].shooting(1, self.objects))    
                
                elif keyboard.is_pressed("up arrow"):
                    self.entities.append(self.players[0].shooting(2, self.objects))       
                
                elif keyboard.is_pressed("down arrow"):
                    self.entities.append(self.players[0].shooting(3, self.objects))    
            
            if keyboard.is_pressed('esc'):
                os.system("cls||clear")
                quit()
            
            self.players[0].set_pos(pos)
            self.map_update()