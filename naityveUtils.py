import os
import sys

class NaityveUtils():

    # identifies system the program is running on
    def os_check():
        if sys.platform == "win32":
            return "Windows"
        elif sys.platform.startswith("linux"):
            return "Linux"
        elif sys.platform == "darwin":
            return "MacOS"
        else:
            return "Unknown"

    # clears the console
    def clear_console():
        os.system('cls')

    def printMap(width, height):
        gameMap = [['#' if i == 0 or i == height - 1 or j == 0 or j == width - 1 else '/' for j in range(width)] for i in range(height)]
        
        for row in gameMap:
            print(''.join(row))

    def GetMapWidth():
        try:
            return input("Enter desired map width:")
        except ValueError:
            print("Invalid input. Input must be a whole number")
            NaityveUtils.GetMapWidth()

    def GetMapHeigth():
        try:
            return input("Enter desired map height:")
        except ValueError:
            print("Invalid input. Input must be a whole number")
            NaityveUtils.GetMapHeigth()


    