from game import Game

if __name__ == "__main__":
    name = str(input("Enter your nickname >> "))
    if name == " ":
        Game(size=[400,200]).game_run()
    else:
        Game(size=[400,200], name=str(name.strip())).game_run()