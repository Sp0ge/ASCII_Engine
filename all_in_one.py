import random
import threading
import keyboard
import os
import time

class Color():
    def set(input, color):
        match color:
            case "green":
                return f"\033[92m{input}\033[0m"
            case "red":
                return f"\033[93m{input}\033[0m"
            case "blue":
                return f"\033[94m{input}\033[0m"
            case _:
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

class Prop():
    def __init__(self, name, id, pos, skin="#" ,parent="engine", have_collision=True, direction=None, speed=2):
        self.color = "white"
        self.type = "prop"
        
        self.speed = int(speed)
        self.not_exist = False
        self.hit_box = 1
        self.trigger = None
        self.skin = Color.set(str(skin), self.color)
        self.pos = list(pos)
        self.direction = direction
        self.name = str(name)
        self.parent = str(parent)
        self.id = int(id)
        self.have_collision = bool(have_collision)
        self.collision_found = bool()
    
    def change_to(self, type):
        match type:
            case "ammo":
                self.skin =  "◘"
                self.color = "red"
            case "prop":
                self.skin =  "#"
                self.color = "white"
            case "bullet":
                self.skin =  "*"
                self.color = "blue"   
                 
        self.type = type
    
    def get_pos(self):
        return list(self.pos)
    
    def check_collision(self, objects):
        if not self.collision_found:
            self.collision=[None,None,None,None]
            
        pos = self.get_pos()
        self.collision_found = False
        surround = [[pos[0],pos[1]-self.hit_box],[pos[0],pos[1]+self.hit_box],[pos[0]-self.hit_box,pos[1]],[pos[0]+self.hit_box,pos[1]]]
        for prop in objects:
            prop_pos = prop.get_pos()
            prop_pos[0],prop_pos[1] = prop_pos[1],prop_pos[0]
            if prop_pos in surround and prop.have_collision:
                prop.action(self, "collision")
                self.collision_found = True
                self.collision[surround.index(prop_pos)] = True
                match self.type:
                    case "bullet":
                        self.not_exist = True
                        
    def move(self, direct, speed=1):
        match direct:
            case 0:
                self.pos[0] -= 1 * speed
            case 1:
                self.pos[0] += 1 * speed
            case 2:
                self.pos[1] -= 1 * speed
            case 3:
                self.pos[1] += 1 * speed
                
    def action(self, player, type):
        match type:
            case "collision":
                if self.type == "ammo" and player.action:
                    player.bullets += 5000
                    self.not_exist = True
                if self.type == "bullet":
                    player.health -= 5
            case "move":
                if self.type == "bullet":
                    self.move(self.direction)
                    
            
                
                
                    
   
class Player_Stats():
    def __init__(self):
        self.health = 100
        self.bullets = 10
        
    def show_stats(self):
        print(str(f"[ HP: {self.health} ] [ Bullets: {self.bullets} ]"))
      
class Player(Player_Stats):
    def __init__(self, pos=(6,12), speed=1, name="player",fov = 10):
        self.skin = "O"
        self.type="player"
        self.hit_box = 1
        self.fov = int(fov)
        self.action=False
        self.pos_x = int(pos[0])
        self.pos_y = int(pos[1])
        self.name = str(name)
        self.speed = int(speed)
        self.moving=[None,None,None,None]
        self.collision=[None,None,None,None]
        self.collision_found = bool()
        
        Player_Stats.__init__(self)
          
    def get_skin(self):
        return self.skin
    
    def check_collision(self, objects):
        if not self.collision_found:
            self.collision=[None,None,None,None]
            
        pos = self.get_pos()
        self.collision_found = False
        surround = [[pos[0],pos[1]-self.hit_box],[pos[0],pos[1]+self.hit_box],[pos[0]-self.hit_box,pos[1]],[pos[0]+self.hit_box,pos[1]]]
        for prop in objects:
            prop_pos = prop.get_pos()
            prop_pos[0],prop_pos[1] = prop_pos[1],prop_pos[0]
            if prop_pos in surround and prop.have_collision:
                prop.action(self, "collision")
                self.collision_found = True
                self.collision[surround.index(prop_pos)] = True
                
    def set_pos(self,cords):
        if self.pos_x-1 == cords[0] and self.collision[2] is None :
            self.moving=[None,None,None,None]
            self.pos_x = int(cords[0])
            self.moving[2] = True
            
        if self.pos_x+1 == cords[0] and self.collision[3] is None :
            self.moving=[None,None,None,None]
            self.pos_x = int(cords[0])
            self.moving[3] = True
            
        if self.pos_y-1 == cords[1] and self.collision[0] is None :
            self.moving=[None,None,None,None]
            self.pos_y = int(cords[1])
            self.moving[0] = True 
            
        if self.pos_y+1 == cords[1] and self.collision[1] is None :
            self.moving=[None,None,None,None]
            self.pos_y = int(cords[1])
            self.moving[1] = True
            
        
    def set_name(self, name):
        self.name = str(name)
    
    def get_pos(self):
        return [self.pos_x,self.pos_y]
    
    def get_name(self):
        return str(self.name)
    
    def get_health(self):
        return str(self.health)
    
    def add_player(players, name):
        players.append(Player(name=f"{name}[{len(players)+1}]"))
        return players
    
    def show_players(input_display, players):
        for player in players:
            input_display[player.get_pos()[0]][player.get_pos()[1]]=player.get_skin()
            title = player.get_name() + "|HP" + player.get_health() + "%"
            name_len = len(title)
            for char in range(0,name_len):
                if len(input_display[0]) > (player.get_pos()[1]-(name_len//2)+char):
                    input_display[player.get_pos()[0]-2][player.get_pos()[1]-(name_len//2)+char] = title[char]
        return input_display        

class Engine():
    def __init__(self, size=[200,100], spawn_rate=20, name="Justachankin"):
        self.running = True
        self.size_x=int(size[0])
        self.size_y=int(size[1])
        self.max_objects = int(((size[0]*size[1])//500) * int(spawn_rate))
        self.entities = list() 
        self.delay = 0.03
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
        self.players[0].show_stats()
        return display
    
    def entities_collision(self):
        threads = []
        for entitiy in self.entities:
            thread=threading.Thread(target=entitiy.check_collision, args=([self.objects]), daemon=True)
            thread.start()
            thread.join()
    
    def display_show(self):
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
        
if __name__ == "__main__":
    # name = str(input("Enter your nickname >> "))
    # if len(name)==0:
    name = "Sp0ge"
    Game(size=[400,200], name=name).run()