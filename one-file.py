import random
import os
import threading
import time
import keyboard

class Prop():
    def __init__(self, name, id, pos, skin="7" ,have_collision=True, move = False):
        self.skin = str(skin)
        self.type = "prop"
        self.pos = list(pos)
        self.name = str(name)
        self.id = int(id)
        self.have_collision = bool(have_collision)
        self.move = bool(move)
        self.collision=[None,None,None,None]
        
    def get_pos(self):
        return list(self.pos)

class Player:
    def __init__(self, pos=(6,12), speed=1, name="player",fov = 11):
        self.skin = "◯"
        self.type="player"
        self.fov = int(fov)
        self.pos_x = int(pos[0])
        self.pos_y = int(pos[1])
        self.name = str(name)
        self.speed = int(speed)
        
        self.collision=[None,None,None,None]
    
    def set_collision(self, collision):
        self.collision = list(collision)
        
    def get_skin(self):
        return self.skin
    
    def set_pos(self,cords):
        if self.pos_x-1 == cords[0] and self.collision[0] is None :
            self.pos_x = int(cords[0])
        if self.pos_x+1 == cords[0] and self.collision[1] is None :
            self.pos_x = int(cords[0])
        if self.pos_y-1 == cords[1] and self.collision[2] is None :
            self.pos_y = int(cords[1])
        if self.pos_y+1 == cords[1] and self.collision[3] is None :
            self.pos_y = int(cords[1])    
    
    def set_name(self, name):
        self.name = str(name)
    
    def get_pos(self):
        return [self.pos_x,self.pos_y]
    
    def get_name(self):
        return str(self.name)
    
    def add_player(players, name):
        players.append(Player(name=f"{name}[{len(players)+1}]"))
        return players
    
    def show_players(input_display, players):
        for player in players:
            input_display[player.get_pos()[0]][player.get_pos()[1]]=player.get_skin()
            name_len = len(player.get_name())
            for char in range(0,name_len):
                if len(input_display[0]) > (player.get_pos()[1]-(name_len//2)+char):
                    input_display[player.get_pos()[0]-1][player.get_pos()[1]-(name_len//2)+char] = player.get_name()[char]
        return input_display

class Color():
    def set(input, color):
        match color:
            case "green":
                return f"\033[92m{input}\033[0m"
            case "red":
                return f"\033[93m{input}\033[0m"
            case "blue":
                return f"\033[94m{input}\033[0m"
            case "white":
                return f"\033[94m{input}\033[0m"
            
    def random(input):
        match random.randint(0,3):
            case 0:
                return f"\033[92m{input}\033[0m"
            case 1:
                return f"\033[93m{input}\033[0m"
            case 2:
                return f"\033[94m{input}\033[0m"
            case 3:
                return f"\033[94m{input}\033[0m"
                   
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
            quit()
            
        # if keyboard.is_pressed("e"):
        #     new_pos[1] = pos[1] + speed
        #     if new_pos[1] < len(self.map[0])-1:
        #         pos[1]= new_pos[1]
                
        self.players[0].set_pos(pos)
        self.map_update()      

if __name__ == "__main__":
    # name = str(input("Enter your nickname >> "))
    # if len(name)==0:
    name = "Sp0ge"
    Game(size=[500,250], name=name).run()