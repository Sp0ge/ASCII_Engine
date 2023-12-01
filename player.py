from prop import Prop

class Player_Stats():
    def __init__(self):
        self.health = 100
        self.bullets = 10
        
    def show_stats(self, ip):
        print(str(f"[ HP: {self.health} ] [ Bullets: {self.bullets} ] [IP: {ip} ]"))
      


class Player(Player_Stats):
    def __init__(self, pos=(6,12), speed=1, name="player",fov = 10, id=0):
        self.id = int(id) 
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
    
    def shooting(self, direct,objects):
        obj=Prop(name="bullet",parent=str(self.id), id=len(objects)+1,pos=[self.pos_y,self.pos_x], direction=direct)
        obj.change_to("bullet")
        self.bullets -= 1
        return obj
        
    def set_name(self, name):
        self.name = str(name)
    
    def get_pos(self):
        return [self.pos_x,self.pos_y]
    
    def get_name(self):
        return str(self.name)
    
    def get_health(self):
        return str(self.health)
    
    def add_player(players, name, id=None):
        if id is None:
            players.append(Player(name=name, id=0))
        else:
            players.append(Player(name=name, id=int(id)+1))
        return players
    
    def show_players(input_display, players):
        for player in players:
            y,x = player.get_pos()[0], player.get_pos()[1]
            input_display[y][x]=player.get_skin()
            title = player.get_name() + "|HP" + player.get_health() + "%"
            name_len = len(title)
            for char in range(0,name_len):
                if len(input_display[0]) > (player.get_pos()[1]-(name_len//2)+char):
                    input_display[player.get_pos()[0]-2][player.get_pos()[1]-(name_len//2)+char] = title[char]
        return input_display
    
    def get_player_info(self):
        return '"' + str(self.id) + '":{"pos_x":"' + str(self.pos_x) + '","pos_y":"' + str(self.pos_y) + '","health":"' + str(self.health) + '","bullets":"' + str(self.bullets) + '","name":"' + str(self.name) + '"},'
    
    def update(self, data):
        self.pos_x = int(data[1])
        self.pos_y = int(data[2])
        self.health = int(data[3])
        self.bullets = int(data[4])
        self.name = str(data[5])