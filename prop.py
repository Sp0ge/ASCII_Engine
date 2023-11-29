from colors import Color
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
                    
            
                
                
                    