from player import Player
from prop import Prop
from server import Server
import json
import os
import threading
import random

class Engine(Server):
    def __init__(self, size=[200,100], spawn_rate=20, name="Justachankin", server=False):
        self.server = bool(server)
        self.remote_ip = ""
        if not self.server:
            self.remote_ip=str(input("Ip to Connect>>"))
        self.host_player_name = str(name)
        self.running = True
        self.size_x=int(size[0])
        self.size_y=int(size[1])
        self.max_objects = int(((size[0]*size[1])//500) * int(spawn_rate))
        self.entities = list() 
        self.delay = 0.03
        self.players = Player.add_player(list(), name, id=0)
        self.objects = list()
        self.map = list()
        self.display = list()
        Server.__init__(self)
        if self.server:
            self.map_gen()
            self.start_hosting()
        else:
            self.connect_to_server(self.ip)
            #threading.Thread(target=self.connect_to_server, args=([self.remote_ip]), daemon=True).start()
        quit()
            
    def map_gen(self):
        map = list()
        for line in range(self.size_y):
            l = list()
            for char in range(self.size_x):
                entity = random.randint(0,100)
                if char == 0 or char == self.size_x-1 or line == 0 or line == self.size_y-1:
                    if line == 0 or line == self.size_y-1:
                        if (char%2)==0: 
                            l.append("@")
                        else:
                            l.append(" ")
                    else:
                        l.append("@")
                else:
                    if len(self.objects) < self.max_objects and entity == 2:
                        prop = Prop(pos=[char,line],name="prop",id=int(len(self.objects)+1),skin="#")
                        if random.randint(2,50) == 3:
                            prop.change_to("ammo")
                        self.objects.append(prop)    
                    l.append(" ")
            map.append(l)
        self.map = map
        
    def spawn_props(self):
        for obj in self.objects:
            if obj.not_exist:
                self.objects.pop(self.objects.index(obj))
            else:
                pos = obj.get_pos()
                self.display[pos[1]][pos[0]] = str(obj.skin)
        for entity in self.entities:
            
            if entity.not_exist:
                self.entities.pop(self.entities.index(entity))
            else:
                entity.action(self.players[0],"move")
                pos = entity.get_pos()
                self.display[pos[1]][pos[0]] = str(entity.skin)
                
    def map_update(self):
        if self.server:
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
        self.players[0].show_stats(self.ip)
        return display
    
    def entities_collision(self):
        threads = []
        for entitiy in self.entities:
            thread=threading.Thread(target=entitiy.check_collision, args=([self.objects]), daemon=True)
            thread.start()
            thread.join()
    
    def display_show(self):
        # print(self.server_info())
        os.system("cls||clear")
        camera = self.set_camera()
        mu = threading.Thread(target=self.players[0].check_collision, args=([self.objects]), daemon=True)
        mu.start()
        mu.join()
        self.entities_collision()
        display = self.display_gen()
        for line in range(camera[0][0],camera[0][1]):
            string = str()
            for char in range(camera[1][0],camera[1][1]):
                try:
                    string += str(display[line][char])    
                except IndexError:
                    string += str(' ')      
            print(string)
            #print(self.server_info())

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
                
    def export_server_info(self):
        info = str('{"players":{')
        for player in self.players:
            info = info + player.get_player_info()
        info = info[:-1]   
        
        map = str()
        for line in self.map:
            map = map + ''.join(line)
        info = info + '},"map":{"size_x":"' + str(self.size_x) + '","size_y":"' + str(self.size_x) + '","data":"' + "asda" + '"},'
        if len(self.entities) > 0:
            info = info + '"entities":{'
            for prop in self.entities:
                info = info + str(f'"{prop.id}":{"parent":"{prop.parent}"", "pos_x":"{prop.pos[0]}", "pos_y":"{prop.pos[1]}", "direction":"{prop.direction}"},')
            info = info[:-1] + "}"      
        else:
            info = info[:-1]
            
        info = info + "}"
        
        return info
    
    def import_server_info(self, info):
        pass
        # if data[0] != "conn_info":
        #     pre_map = list(data[1].split("|"))
        #     for part in pre_map:
        #         self.map.append(list(part.split("")))
        #     for player_update in data[0].split("|"):
        #         for player in self.players:
        #             if str(player.id) ==  str(player_update[0]):
        #                 player.update(player_update)
        #     for prop in data[2].split("|"):
        #         if prop.parent != str(self.players[0].id):
        #             self.entities.append(Prop(parent=prop.parent, pos=(prop.pos[0], prop.pos[1]), direction=prop.directions)) 
        