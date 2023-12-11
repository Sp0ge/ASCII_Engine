import threading
def lol():
    print("asdasd")
    
if __name__ == "__main__":
    threading.Thread(target=lol).start()
    threading.Thread(target=lol).start()
    