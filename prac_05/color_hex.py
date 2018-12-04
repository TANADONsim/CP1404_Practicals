COLOR_NAMES = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "BEIGE": "#f5f5dc", "BLACK": "#000000",
               "BLANCHEDALMOND": "#ffebcd", "BLUEVIOLET": "#8a2be2", "BURLYWOOD": "#deb887"}
# print(STATE_NAMES)

color = input("Enter color name: ")
color = color.upper()
while color != "":
    if color in COLOR_NAMES:
        print(color, "is", COLOR_NAMES[color])
    elif color == "ALL":
        for color in COLOR_NAMES:
            print("{0:<4} is {1}".format(color, COLOR_NAMES[color]))
    else:
        print("Invalid color name")
    color = input("Enter color name : ")
    color = color.upper()
 