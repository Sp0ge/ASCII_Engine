from rich.console import Console as RichC

RichC = RichC()

class Main():
    def __init__(self):
        self.menu  = consolemenu.ConsoleMenu(title="My Game", subtitle="In development", clear_screen=True)
        self.gen()
        
    def gen(self):
        
    def show(self):
        self.menu.show()