class Player(object):
    def __init__(self, pos=(0,0), speed=1, name="player"):
        self.skin = "#"
        self.pos_x = int(pos[0])
        self.pos_y = int(pos[1])
        self.name = str(name)
        self.speed = int(speed)
    
    def set_pos(self,cords):
        self.pos_x = int(cords[0])
        self.pos_y = int(cords[1])
    
    def set_name(self, name):
        self.name = str(name)
    
    def get_pos(self):
        return [self.pos_x,self.pos_y]
    
    def get_name(self):
        return str(self.name)
        