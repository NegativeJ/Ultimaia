from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def showInstructions():    
    #print opening and commands
    print("Ultimaia Testing build")
    print("######################")
    print("Commands:")
    print("'go [direction]'")
    print("'get [item]'")

def showStatus():
    #print status
    print("---------------------------")
    print("You are in the " + rooms[currentRoom]["name"])
    #print inventory
    print("Inventory : " + str(inventory))
    #print item s in room
    if "item" in rooms[currentRoom]:
        print("You see a " + rooms[currentRoom]["item"])
    print("---------------------------")

#Inventory V1
inventory = []

#Rooms
rooms = {

            1 : {  "name"  : "Testing Room 1" ,
                   "north" : 5,
                   "east"  : 2,
                   "south" : 3 }  ,
 
            2 : {  "name"  : "Testing Room 2" ,
                   "west"  : 1,
                   "south" : 4,
                   "item"  : "key_1" }  ,            

            3 : {  "name"  : "Testing room 3" ,
                   "north": 1 }  ,

            4 : {  "name"  : "Testing room 4" ,
                   "north" : 2 } ,
            
            5 : {  "name"  : "Dungeon1" ,
                   "north" : 6,
                   "south" : 1 } ,
            
            6 : {  "name"  : "Dungeon2" ,
                   "north" : 7,
                   "south" : 5 } ,
            
            7 : {  "name"  : "Dungeon3" ,
                   "north" : 8,
                   "south" : 6 } ,
            
            8 : {  "name"  : "Dungeon4" ,
                   "north" : 9,
                   "south" : 7 } ,
            
            9 : {  "name"  : "Dungeon5" ,
                   "north" : 10,
                   "south" : 8 } ,
            
            10 : {  "name"  : "Dungeon6" ,
                    "south" : 9}

         }

currentRoom = 1

showInstructions()


#loop infinitely
while True:

    showStatus()
    
    #['go','east']
    move = input("@: ").lower().split()
    
    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You can't go that way!")

    if move[0] == "get" :
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
            inventory += [move[1]]
            print(move[1] + " got!")
            del rooms[currentRoom]["item"]
        else:
            print("Can't get " + move[1] + "!")
            