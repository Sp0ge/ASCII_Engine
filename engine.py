from player import Player
from reprint import output

class Engine():
    def __init__(self, size=[30,20]):
        self.running = True
        self.size_x=int(size[0])
        self.size_y=int(size[1])
        self.delay = 0.01
        
        self.players = []
        self.add_player()
        
        self.map = self.map_gen()
        
        with output(initial_len=self.size_y, interval=0) as out_lines:
            self.display = out_lines
    
    def add_player(self):
        self.players.append(Player(name=f"player_{len(self.players)+1}"))
    
    def show_players(self, input_display):
        for player in self.players:
            input_display[player.get_pos()[0]][player.get_pos()[1]]=player.get_skin()
        return input_display
    
    def map_gen(self):
        map = list()
        for line in range(self.size_y):
            l = list()
            for char in range(self.size_x):
                if char == 0 or char == self.size_x-1 or line == 0 or line == self.size_y-1:
                    if line == 0 or line == self.size_y-1:
                        if (char%2)==0: 
                            l.append("▦")
                        else:
                            l.append(" ")
                    else:
                        l.append("▦")
                else:
                    l.append(" ")
            map.append(l)
        return map
    
    def map_update(self):
        self.map = self.map_gen()
    
    def display_gen(self):
        display = self.map
        display = self.show_players(display)
        return display
    
    def display_show(self):
        display = self.display_gen()
        lines = 0
        camera = self.set_camera(display)
        for line in range(camera[0][0],camera[0][1]):
            string = str()
            for char in range(camera[1][0],camera[1][1]):
                try:
                    string += str(display[line][char])
                except:
                    string += str(" ")      
                self.display[lines] = string
        
            lines += 1
            
    def set_camera(self, display):
        x_stop,y_stop = 0,0
        
        pos_x, pos_y = self.players[0].get_pos()[0], self.players[0].get_pos()[1]
        display_size = [len(display[len(display)//2]), len(display)]
        fov = self.players[0].fov
        camera = list([[pos_x-10,pos_x+10],[pos_y-10,pos_y+10]])
        
        if display_size[0] < camera[0][1]:
            x_stop = camera[0][1] - display_size[0]
            
        if display_size[1] < camera[1][1]:
            y_stop = camera[1][1] - display_size[1]
            
        # if display_size[0] > camera[0][1]:
        #     x_stop =  camera[0][1]-display_size[0]
            
        # if display_size[1] > camera[1][1]:
        #     y_stop =  camera[1][1]-display_size[1]
             
        camera = list([[pos_x-fov-x_stop,pos_x+fov+x_stop],[pos_y-fov-y_stop,pos_y+fov+y_stop]])       
        return camera 
                

