# Cory Thomas cmthomas@email.wm.edu 954-295-5796
# This program will work to read through data on rushers in the 
# National Football League for the 2010 and 2011 seasons. After it has read 
# through the data and created a list of the information, it will
# calculate the rusher rating for each player using the given formula.
# This formula is the average yards per carry plus the percentage of touchdowns
# per carry plus the percentage of fumbles per carry all divided by (100 * 4.5).
# The program will then print out the name of each rusher followed by his 
# rusher rating. It will then ask the user if he or she wants information about 
# a particular player and then get the information requested and print it out.

# Import the player class
from Player import Player


# -----------------------------------------------------------------------------


def dataReader() :
    """This function will work to read through the data in the file and create 
    the appropriate list of information using that data"""
    
    import string
    
    # Open the data file for reading
    file = open("rushers.csv", 'r')
    
    # Create an empty dictionary to store the information of the payer to
    players = {}
    
    # Read through each line in the file and throw away the column header
    # information
    line = file.readline().strip()
    line = file.readline().strip()
    while line != '' :
        
        # Strip away the extraneous punctuation and split the line at the commas
        newLine = line.strip(string.punctuation)
        newLine = line.split(',')
        
        # Create the players name and create a Player object passing the first 
        # and last names as arguments
        first = newLine[0]
        last = newLine[1]
        
        playerObject = Player(first, last)
        name = playerObject.returnName()
                        
        # Check to see if the player is already in the dictionary and if not add
        # him with his name as the key and the player object as the value
        if name not in players :
            
            players[name] = playerObject
        
        # Call the update function    
        Player.update(players[name], newLine[2], newLine[3], newLine[13], \
        newLine[5], newLine[6], newLine[7], newLine[10])
            

        line = file.readline().strip()
    
    # Close the file
    file.close()
    
    # Create an empty list and append the values to it
    playerList = []
    
    for val in players.values(): 
        playerList.append(val)
        
    playerList.sort()
    
    # Print out the results
    for elem in playerList:
        print(elem)
        
    return players
    

# ----------------------------------------------------------------------------

def lookUpInfo(players) :
    """ This procedure will function to determine if the user is interested in
    information about a particular person, and is he or she is interested to
    gather the relevant information and print it out to the screen"""
    
    # Create a while loop to gather information for the user
    interest = input("\n\nDo you want information about a particular player? ")
    print(interest)
    while interest.lower() == 'y' :
        
        # Ask the user to enter the name he or she is looking and allow for 
        # lower case letters
        name = input("Enter player's name: ")
        print(name)
        
        name = name.lower()
        name = name.title()
        
        # Make sure the name is in the dictionary
        if name not in players :
            print("This player is not in the system.")
        
        else :
            # Allow the user to choose what informtion he or she wants about the 
            # player he or she entered
            choice = input("\nPick one \na) Overall rusher rating" \
            "\nb) Individual years and rating\n \nEnter choice: ")
            print(choice)
        
            if choice.lower() == 'a' :
                print()
                print(players[name])
            
            elif choice.lower() == 'b' :
                print()
                Player.printInfo(players[name])
            
            else :
                print("You've entered an illegal choice")
                
        interest = input("\n\nAre you interested in another player? ")
        print(interest)
        

# ----------------------------------------------------------------------------


#Main program

dataReader()
players = dataReader()
lookUpInfo(players)