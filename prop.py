from colors import Color
class Prop():
    def __init__(self, name, id, pos, skin="7" ,have_collision=True):
        self.color = "white"
        self.type = "prop"
        self.hit_box = 1
        self.trigger = None
        self.skin = Color.set(str(skin), self.color)
        self.pos = list(pos)
        self.name = str(name)
        self.id = int(id)
        self.have_collision = bool(have_collision)
    
    def get_pos(self):
        return list(self.pos)
    
    def move(self, direct):
        match direct:
            case 0:
                self.pos[0] -= 1
            case 1:
                self.pos[0] += 1
            case 2:
                self.pos[1] -= 1
            case 3:
                self.pos[1] += 1