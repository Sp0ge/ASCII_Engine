import getpass
class Player:
    def __init__(self, pos=(6,12), speed=1, name="player",fov = 20):
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