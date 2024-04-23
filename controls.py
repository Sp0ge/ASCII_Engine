import keyboard

class Controls():
    def keys(self, display):      
            if keyboard.is_pressed('s'):
                display[self.pos[0]][self.pos[1]] = self.background
                self.pos[0] += self.speed
                self.background = display[self.pos[0]][self.pos[1]]
            
            if keyboard.is_pressed('w'):
                display[self.pos[0]][self.pos[1]] = self.background
                self.pos[0] -= self.speed
                self.background = display[self.pos[0]][self.pos[1]]
                
            if keyboard.is_pressed('a'):
                display[self.pos[0]][self.pos[1]] = self.background
                self.pos[1] -= self.speed
                self.background = display[self.pos[0]][self.pos[1]]
            
            if keyboard.is_pressed('d'):
                display[self.pos[0]][self.pos[1]] = self.background
                self.pos[1] += self.speed
                self.background = display[self.pos[0]][self.pos[1]]
                
    def arrows(self, display):
        if keyboard.is_pressed('down'):
                display[self.pos[0]][self.pos[1]] = self.background
                self.pos[0] += self.speed
                self.background = display[self.pos[0]][self.pos[1]]
            
        if keyboard.is_pressed('up'):
            display[self.pos[0]][self.pos[1]] = self.background
            self.pos[0] -= self.speed
            self.background = display[self.pos[0]][self.pos[1]]
            
        if keyboard.is_pressed('left'):
            display[self.pos[0]][self.pos[1]] = self.background
            self.pos[1] -= self.speed
            self.background = display[self.pos[0]][self.pos[1]]
        
        if keyboard.is_pressed('right'):
            display[self.pos[0]][self.pos[1]] = self.background
            self.pos[1] += self.speed
            self.background = display[self.pos[0]][self.pos[1]]