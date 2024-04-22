from consolemenu import SelectionMenu
from consolemenu.items import *

class Main():
    def __init__(self):
        self.title = "Main menu"
        self.options = ["Start","Load"]
        self.menu = SelectionMenu(self.options,self.title,show_exit_option=True)

    def show(self):
        self.menu.show()
        self.menu.join()
        return self.menu.selected_option