def rock (color: str):
    print(f"{color} is  rock!")


rock_dict: dict = {
    'blue': rock
}

inp = input("write the color: ")
rock_dict.get(inp)(inp)