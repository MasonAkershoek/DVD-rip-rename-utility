# Author: Mason Akershoek
# App Name: Rename Utility

import os
import subprocess

def main():
    quit = 0
    ep = 1
    files = []
    
    print("Welcome to the rename utility")
    print("By. Mason Akershoek\n")

    dir = getDir()
    season = getSeason()
    op = input("Do you need to start at a different value than one? (y or n) ")
    if op == "y":
        ep = getEpNum()

    op = input("would you like to see the order of the rename?(y or n) ")
    if op == "y":
        showPreview(dir)
        
    execute(season, ep, dir)



def getDir():
    dir = input("enter your dir: ")
    print("Current working directory: " + dir + "\n")
    return dir

def getSeason():
    season = input("Enter the season of the videos: ")
    return season

def getEpNum():
    num = input("Enter the number to start at: ")
    ep = int(num)
    return ep

def showPreview(dir):
    entries = os.listdir(dir)
    entries.sort()
    for entry in entries:
            print(entry)
    op = input("Would you still like to continue?(y or n): ")
    if op == "n":
        exit()


def execute(season, ep, dir):
    entries = os.listdir(dir)
    entries.sort()
    for entry in entries:
            x = str("/" + entry)
            os.rename(dir + x, dir + "/" + "S" +
                      season + "E" + str(ep) + ".mp4")
            ep = ep + 1
            quit = 1


        
print("\nOperation Compleate!!")

if __name__=="__main__":
    main()
