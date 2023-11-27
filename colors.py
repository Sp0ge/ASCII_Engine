import random

class Color():
    def set(input, color):
        match color:
            case "green":
                return f"\033[92m{input}\033[0m"
            case "red":
                return f"\033[93m{input}\033[0m"
            case "blue":
                return f"\033[94m{input}\033[0m"
            case "white":
                return f"\033[94m{input}\033[0m"
            
    def random(input):
        match random.randint(0,3):
            case 0:
                return f"\033[92m{input}\033[0m"
            case 1:
                return f"\033[93m{input}\033[0m"
            case 2:
                return f"\033[94m{input}\033[0m"
            case 3:
                return f"\033[94m{input}\033[0m"