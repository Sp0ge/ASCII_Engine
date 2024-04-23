from controls import Controls

class Player():
    def __init__(self, display_size=[0,0], id=1, controls=int(0)):
        self.id = int(id)
        if controls == 0:
            self.pos = [display_size[0]//6,display_size[1]//2]
        else:
            self.pos = [display_size[0]//3,display_size[1]//2]
        self.skin = "@"
        self.background = "."
        self.speed = 1
        self.controls = controls
        
    def update(self, display):
        match self.controls:
            case 0:
                Controls.keys(self, display)
            case 1:
                Controls.arrows(self, display)
                
        display[self.pos[0]][self.pos[1]] = str(self.skin)
    
    
    