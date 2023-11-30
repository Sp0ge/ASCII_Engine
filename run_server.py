from game import Game

if __name__ == "__main__":
    name = "TEST"
    Game(size=[400,200], name=str(name.strip()), server=True).game_run()