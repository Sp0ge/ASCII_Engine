from player import Player
import os
from colors import Color

class Engine():
    def __init__(self, size=[30,20]):
        self.running = True
        self.size_x=int(size[0])
        self.size_y=int(size[1])
        self.delay = 0.025
        
        self.players = Player.add_player(list())
        
        self.map = self.map_gen()
        self.display = list()
    
    def map_gen(self):
        map = list()
        for line in range(self.size_y):
            l = list()
            for char in range(self.size_x):
                if char == 0 or char == self.size_x-1 or line == 0 or line == self.size_y-1:
                    if line == 0 or line == self.size_y-1:
                        if (char%2)==0: 
                            l.append(Color.random("▦"))
                        else:
                            l.append(" ")
                    else:
                        l.append(Color.random("▦"))
                else:
                    l.append(" ")
            map.append(l)
        return map
    
    def map_update(self):
        self.map = self.map_gen()
    
    def display_gen(self):
        self.display.clear()
        display = self.map
        display = Player.show_players(display, self.players)
        return display
    
    def display_show(self):
        os.system("cls||clear")
        camera = self.set_camera()
        display = self.display_gen()
        lines = 0

        for line in range(camera[0][0],camera[0][1]):
            string = str()
            for char in range(camera[1][0],camera[1][1]):
                string += str(display[line][char])      
            print(string)
            lines += 1
       
    def set_camera(self):
        pos_x, pos_y = self.players[0].get_pos()[0], self.players[0].get_pos()[1]
        fov_x = self.players[0].fov
        fov_y = self.players[0].fov * 2
        camera = list([[pos_x-fov_x,pos_x+fov_x],[pos_y-fov_y,pos_y+fov_y]])      
        display_len = [self.size_x,self.size_y]  
        
        #up wall
        if camera[0][0] < 0:
            camera[0][0] = 0
            camera[0][1] = pos_x + fov_x
            
        #left wall
        if camera[1][0] < 0:
            camera[1][0] = 0
            camera[1][1] = pos_y + fov_y
        
        #bottom wall
        if camera[0][1] > display_len[1]:
            camera[0][1] = display_len[1]
            camera[0][0] = pos_x - fov_x
            
        #right wall
        if camera[1][1] > display_len[0]:
            camera[1][1] = display_len[0]
            camera[1][0] = pos_y - fov_y
            
        print(camera)     
                   
        return camera 
                

