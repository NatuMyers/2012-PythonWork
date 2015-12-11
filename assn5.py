"""
Assignment: Assignment 5, Olympic Database

Description:
This module contains functions for maintaining and displaying a
database of Olympic medal winners, using two levels of dictionaries.

Class: CISC 121 FW, section 001, October 25th, 2012
Author: Natu Myers
Student Number: (10068437)
"""

def sample():
    """
    Builds and returns a sample database, containing medalists for a few of my
    favorite events from the London Olympics.
    Supplied with the assignment to help you test your functions.
    Feel free to modify it to include your favorite olympic events.
    We will ignore this function when we mark the assignment.
    """
    olympics = {} # empty dictionary
    addMedalist(olympics,"Gabriel Douglas","Women's gymnastics all-around",\
                "gold")
    addMedalist(olympics,"Victoria Komova","Women's gymnastics all-around",\
                "silver")
    addMedalist(olympics,"Aliya Mustafina","Women's gymnastics all-around",\
                "bronze")
    addMedalist(olympics,"Usain Bolt","Men's 100 meter","gold")
    addMedalist(olympics,"Yohan Blake","Men's 100 meter","silver")
    addMedalist(olympics,"Justin Gatlin","Men's 100 meter","bronze")   
    addMedalist(olympics,"Michael Jung","Equestrian eventing","gold")
    addMedalist(olympics,"Gerco Schroder","Equestrian jumping","bronze")
    addMedalist(olympics,"Aliya Mustafina","Women's Uneven Bars","gold")
    
    return olympics


def addMedalist(database, name, event, medal):
    """
    Modifies an Olympic database by adding a medal winner.
    Parameters:
        the database
        the name of the medalist
        the name of the event 
        the kind of medal ("gold","silver" or "bronze")
    No return result.  Changes the database in place.
    If the database already contains an entry for this combination of
    event and medal, prints an error message and doesn't change the
    database.
    """

    if event in database and medal in database[event]:
        print "ERROR: Event/medal combo already in database."
        return None
        



    
    #Without this if, only one medal will be added per event
    if event not in database:#If the event isn't already a key...
        database[event]={}#Make an empty dictionary value.
    
    
    



    #The subdictionary's key will be assigned to the name
    database[event][medal] = name 

    
def lookup(database, event, medal):
    """
    Looks up a medalist in an Olympic database.
    Parameters:
        the database
        the name of the event
        the kind of medal ("gold","silver" or "bronze")
    Return value: the name of the medalist
    If there is no entry for the specified event and medal, returns None.
    Does not print anything.
    """
    
    eventDict = {}

    #Check if events exist in the called database
    if event in database:
        eventDict = database[event]
    if event not in database:
        return None

    #Check if medals exist in the called event
    if medal in eventDict:
        return eventDict[medal]
    if medal not in eventDict:
        return None


def displayMedals(database):
    """
     Displays the medalists in a database, in indented form.
    Parameter: the database
    """
   
    # 1 loop is needed for every level of nesting
    for event in database:#goes through every key in database

        eventisPrinted = False
        for medal in database[event]:#database[event] is a subdictionary
            
            if eventisPrinted == False:#This counter helps display the title only ONCE
                print event+":"
                eventisPrinted = True
            print "\t",medal+":",\
                  database[event][medal]#database[event][medal]returns the value of the subdictionary (a name)

            
def deleteMedalist(database, event, medal):
    """
    Modifies an Olympic database by deleting a medal winner.
    Parameters:
        the database
        the name of the event (a string)
        the kind of medal ("gold","silver" or "bronze")
    No return result.  Changes the database in place.
    If the database doesn't contain the entry described by the
    parameters, writes an error message and doesn't change the
    database.
    """
    #Removes the name accompanied with the value of the subdictionary
    del database[event][medal]

    
def findAthlete(database, name):
    """
    Looks for an athlete in the database.  Lists all the medals won by
    the athlete, or displays a "no medals" message.
    """
    nameisPrinted = False
    
    for event in database:#goes through every key in database
    
        for medal in database[event]:#goes through all subdictionaries
            
            #Medal is the value, and the name is now the key.
            if database[event][medal] == name:
                
                #This counter helps display each event just once 
                if nameisPrinted == False:
                    print name+":"
                
                print "\t"+event+",",medal, "medal"
                nameisPrinted = True
                
    if nameisPrinted == False:
        print name+":\n", "\tno medals"

