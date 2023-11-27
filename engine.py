from player import Player
from prop import Prop
import os
import threading
import random

class Engine():
    def __init__(self, size=[200,100], spawn_rate=20, name="Justachankin"):
        self.running = True
        self.size_x=int(size[0])
        self.size_y=int(size[1])
        self.max_objects = int(((size[0]*size[1])//500) * int(spawn_rate))
        self.delay = 0.001
        
        self.players = Player.add_player(list(), name)
        self.objects = list()
        
        self.map = list()
        self.map_gen()
        self.display = list()
    
    def map_gen(self):
        map = list()
        for line in range(self.size_y):
            l = list()
            for char in range(self.size_x):
                entity = random.randint(0,100)
                if char == 0 or char == self.size_x-1 or line == 0 or line == self.size_y-1:
                    if line == 0 or line == self.size_y-1:
                        if (char%2)==0: 
                            l.append("▦")
                        else:
                            l.append(" ")
                    else:
                        l.append("▦")
                else:
                    if len(self.objects) != self.max_objects and entity == 2:
                        self.objects.append(Prop(pos=[char,line],name="prop",id=int(len(self.objects)+1),skin="#", have_collision=True, move=False))    
                    l.append(" ")
                        

            map.append(l)
        
        self.map = map
        
    def spawn_props(self):
        for obj in self.objects:
            pos = obj.get_pos()
            self.display[pos[1]][pos[0]] = str(obj.skin)
        self.display   
       
    # Проверка столкновений не работает.
       
    def check_player_collision(self):
        pass
    
        # for prop in self.objects:
        #     for player in self.players:
        #         collision = [None,None,None,None]
        #         if prop.get_pos()[1] == player.get_pos()[0]+1 and prop.get_pos()[0] == player.get_pos()[1]:
        #             collision[0] = "up"
        #         if prop.get_pos()[1] == player.get_pos()[0]-1 and prop.get_pos()[0] == player.get_pos()[1]:
        #             collision[1] = 'bottom'
        #         if prop.get_pos()[1] == player.get_pos()[0] and prop.get_pos()[0] == player.get_pos()[1]+1:
        #             collision[2] = 'left'
        #         if prop.get_pos()[1] == player.get_pos()[0] and prop.get_pos()[0] == player.get_pos()[1]-1:
        #             collision[3] = 'right'
        #         player.set_collision(collision)
                
    def map_update(self):
        mu = threading.Thread(target=self.map_gen, args=(), daemon=True)
        mu.start()
        mu.join()
    
    def display_gen(self):
        self.display = list()
        self.display = self.map
        mu = threading.Thread(target=self.spawn_props, args=(), daemon=True)
        mu.start()
        mu.join()
        display = Player.show_players(self.display, self.players)
        return display
    
    def display_show(self):
        os.system("cls||clear")
        camera = self.set_camera()
        self.check_player_collision()
        display = self.display_gen()
        for line in range(camera[0][0],camera[0][1]):
            string = str()
            for char in range(camera[1][0],camera[1][1]):
                try:
                    string += str(display[line][char])    
                except IndexError:
                    string += str(' ')      
            print(string)


    def set_camera(self):
        pos_x, pos_y = self.players[0].get_pos()[0], self.players[0].get_pos()[1]
        fov_x = self.players[0].fov
        fov_y = self.players[0].fov * 4
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
          
                   
        return camera 
                

