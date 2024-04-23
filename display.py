from debug import how_it_fast
import win32api
import os

class Display():
    def __init__(self):
        self.screen_size = [24,24]
        self.display = list()
        self.DisplayFrequency = getattr(win32api.EnumDisplaySettings(win32api.EnumDisplayDevices().DeviceName, -1),"DisplayFrequency")

        self.prepare()
            
    def prepare(self):
        self.display_clear()
        self.display_init(self.screen_size)
    
    def display_init(self, screen_size):
        self.display.clear()
        for y in range(0, screen_size[1]):
            row = []
            for x in range(0, screen_size[0]):
                row.append(".")
            self.display.append(row)
            
        for y in range(0, screen_size[1]):
            if y == 0 or y==screen_size[1]-1:
                for x in range(0, screen_size[0]):
                    self.display[y][x] = "#"
            else:
                self.display[y][0] = "#"
                self.display[y][-1] = "#"
        
    def display_show(self):
        self.display_clear()
        for row in self.display:
            print(' '.join(map(str, row)))
    
    def display_clear(self):
        os.system("cls||clear")