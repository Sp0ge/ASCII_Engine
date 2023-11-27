class Player(object):
    def __init__(self, pos=(6,12), speed=1, name="Guest_Player",fov = 20):
        self.skin = "◯"
        self.fov = int(fov)
        self.pos_x = int(pos[0])
        self.pos_y = int(pos[1])
        self.name = str(name)
        self.speed = int(speed)
    
    def get_skin(self):
        return self.skin
    
    def set_pos(self,cords):
        self.pos_x = int(cords[0])
        self.pos_y = int(cords[1])
    
    def set_name(self, name):
        self.name = str(name)
    
    def get_pos(self):
        return [self.pos_x,self.pos_y]
    
    def get_name(self):
        return str(self.name)
    
    def add_player(players):
        players.append(Player(name=f"player_{len(players)+1}"))
        return players
    
    def show_players(input_display, players):
        for player in players:
            input_display[player.get_pos()[0]][player.get_pos()[1]]=player.get_skin()
            name_len = len(player.get_name())
            for char in range(0,name_len):
                if len(input_display[0]) > (player.get_pos()[1]-(name_len//2)+char):
                    input_display[player.get_pos()[0]-1][player.get_pos()[1]-(name_len//2)+char] = player.get_name()[char]
        return input_display