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