from debug import how_it_fast

class Display():
    def __init__(self):
        self.screen_size = (32,32)
        self.display = list()
        
        self.prepare()
            
    def prepare(self):
        self.display_clear()
        self.display_init(self.screen_size)
    
    def display_init(self, screen_size):
        self.display.clear()
        for y in range(0, screen_size[1]):
            row = []
            for x in range(0, screen_size[0]):
                row.append(" ")
            self.display.append(row)
            
        for y in range(0, screen_size[1]):
            if y == 0 or y==screen_size[1]-1:
                for x in range(0, screen_size[0]):
                    self.display[y][x] = "#"
            else:
                self.display[y][0] = "#"
                self.display[y][-1] = "#"
        
    def show(self):
        for row in self.display:
            print(' '.join(map(str, row)))
    
    def display_clear(self):
        print("\033c", end="", flush=True)