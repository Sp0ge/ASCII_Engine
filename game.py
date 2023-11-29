from engine import Engine
from prop import Prop
import time
import os
import keyboard

class Game(Engine):
    def __init__(self, size=[75,25], name="Justachankin"):
        Engine.__init__(self, size=size, name=name)
    
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
        
        if keyboard.is_pressed('esc'):
            os.system("cls||clear")
            quit()
            
        if keyboard.is_pressed("e"):
            self.players[0].action=True
        else:
            self.players[0].action=False
        
        if self.players[0].bullets > 0:
            if keyboard.is_pressed("left arrow"):
                self.players[0].bullets -= 1
                obj = Prop(name="bullet",parent=self.players[0], id=len(self.objects)+1,pos=[pos[1],pos[0]], direction=0)
                obj.change_to("bullet")
                self.entities.append(obj)   
            
            elif keyboard.is_pressed("right arrow"):
                self.players[0].bullets -= 1
                obj = Prop(name="bullet",parent=self.players[0], id=len(self.objects)+1,pos=[pos[1],pos[0]], direction=1)
                obj.change_to("bullet")
                self.entities.append(obj)    
            
            elif keyboard.is_pressed("up arrow"):
                self.players[0].bullets -= 1
                obj = Prop(name="bullet",parent=self.players[0], id=len(self.objects)+1,pos=[pos[1],pos[0]], direction=2)
                obj.change_to("bullet")
                self.entities.append(obj)    
            
            elif keyboard.is_pressed("down arrow"):
                self.players[0].bullets -= 1
                obj = Prop(name="bullet",parent=self.players[0], id=len(self.objects)+1,pos=[pos[1],pos[0]], direction=3)
                obj.change_to("bullet")
                self.entities.append(obj)     
                
        self.players[0].set_pos(pos)
        self.map_update()