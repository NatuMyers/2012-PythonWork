"""
Assignment: Assignment 3, Poker Program

Description:
Program is to have one function called poker that takes one
parameter -- a string describing a poker hand -- and will
return one of the following strings to describe the hand:

"straight flush"
"four of a kind"
"full house"
"flush"
"straight"
"three of a kind"
"two pair"
"one pair"
"nothing"

Class: CISC 121, October 5th, 2012
Author: Natu Myers
Student Number: 10068437)
"""

def poker(cards):
    """
    This is the main func. wherein
    helper functions are called and an element
    of returnList is returned (to know kind of
    hand!)
    """
    #Breaks up card string by assigning
    #cards 1-5 based on position, commas, etc
    c1 = cards[0]+cards[1]
    c2 = cards[3]+cards[4]
    c3 = cards[6]+cards[7]
    c4 = cards[9]+cards[10]
    c5 = cards[12]+cards[13]

    #The ranks and suits we're working along
    #with the kinds of hands possible! 
    deckRanks = ["A","2","3","4","5","6","7",\
                 "8","9","0","J","Q","K"]
    
    deckSuits = ["S","H","D","C"]
    
    resultList = ["straight flush","four of a kind",\
                  "full house","flush","straight",\
                  "three of a kind","two pair",\
                  "one pair","nothing"]
    result = ""

    #Assigning lists. They start empty!
    myDeck = [None]*52 
    myHand = [None]*5

    """
    MyHand will be filled up by assigning
    to it the return value of makeDeck.
    Passing the deck, ranks,suit, hand list
    and cards are needed to properly generate
    correct cards to analyse.
    """

    myHand = makeDeck\
             (myDeck,deckRanks,deckSuits,\
              myHand,c1,c2,c3,c4,c5)

    #Result is a string that's assigned based on the hand type!
    result = checkHand\
             (myHand,c1,c2,c3,c4,c5,\
              deckRanks,deckSuits,resultList)

    #The type of hand will be returned to the module!
    return result

            
def makeDeck(deck,ranks,suits,hand,crd1,crd2,crd3,crd4,crd5):
    """
    This function makes a deck, and puts
    selected cards from deck to hand.
    This will return the hand array.
    """

    #Cards to be assigned a value from the deck
    card1 = [[],[]]
    card2 = [[],[]]
    card3 = [[],[]]
    card4 = [[],[]]
    card5 = [[],[]]
    #Variables in various loops
    i = 0
    j = 0
    k = 0
    m = 0
    n = 0
    
    #GENERATE DECK
    while i < len(ranks):#13 times
        while j < len(suits):#4 times
            deck[k]= (ranks[i] + suits[j]) #Rank followed by suit
                
            j+=1
            k += 1 #K will get to 52
        j = 0 #J WILL KEEP RESETING
        i += 1
        
    #ASSIGN 5 CARDS FROM DECK TO HAND
    while m < len(deck):
        if deck[m] == crd1:
            card1 = [deck[m][0],deck[m][1]]
        if deck[m] == crd2:
            card2 = [deck[m][0],deck[m][1]]
        if deck[m] == crd3:
            card3 = [deck[m][0],deck[m][1]]
        if deck[m] == crd4:
            card4 = [deck[m][0],deck[m][1]]
        if deck[m] == crd5:
            card5 = [deck[m][0],deck[m][1]]
        m+=1
   
    Hand = [card1,card2,card3,card4,card5]

    #The following While loop changes strings to intergers
    #in the first element in each card hand (the ranks)
    #This is so that we can compare ranks easily
    while j < len(Hand):
        
        #For straights IF there's a king, "A" will be assigned
        # to 14 so that j,k,a will appear incr. by 1
        if Hand[j][0] == "A":
            Hand[j][0] = 1
            while n < len(Hand):
                if Hand[n][0] == 13 or Hand[n][0] == "K":
                    Hand[j][0] = 14
                n+=1
            
        if Hand[j][0] == "2":
            Hand[j][0] = 2
        if Hand[j][0] == "3":
            Hand[j][0] = 3
        if Hand[j][0] == "4":
            Hand[j][0] = 4
        if Hand[j][0] == "5":
            Hand[j][0] = 5
        if Hand[j][0] == "6":
            Hand[j][0] = 6
        if Hand[j][0] == "7":
            Hand[j][0] = 7
        if Hand[j][0] == "8":
            Hand[j][0] = 8
        if Hand[j][0] == "9":
            Hand[j][0] = 9
        if Hand[j][0] == "0":#0 represented 10
            Hand[j][0] = 10   
        if Hand[j][0] == "J":
            Hand[j][0] = 11
        if Hand[j][0] == "Q":
            Hand[j][0] = 12
        if Hand[j][0] == "K":
            Hand[j][0] = 13
        j +=1

    return Hand
   
def checkHand(Hand,card1,card2,card3,card4,card5,rank,suits,result):
    """
    This function calls the helper functions
    isOnePair,idTwoPair,isThreeofaKind,
    isFourofaKind,and isStraightorFlush

    Using these functions, the appropriate
    result will be returned as a string to
    the function poker
    """
    
    rank = ["1","2","3","4","5","6","7","8","9","0","J","Q","K"]   
    i = 0
    j = 0
    n=0
    onePair = False
    twoPair = False
    threeofaKind = False
    straight = False
    flush = False
    fullHouse = False
    fourofaKind = False
    straightFlush = False

    Hand.sort()#Needed for the straight func. to prevent many loops
 
    n = isStraightorFlush(Hand)
    if n == 3:
        straightFlush = True
    if n == 2:
        flush = True
    if n == 1:
        straight = True

    #To save a bit of time...don't ALWAYS go through all this
    if straightFlush == False and straight == False and flush == False: 
        onePair = isOnePair(Hand,rank)
        twoPair = isTwoPair(Hand,rank)
                
        threeofaKind = isThreeofAKind(Hand,rank)
        fourofaKind = isFourofAKind(Hand,rank)
        fullHouse = isFullHouse(Hand)

    #Final step, return a string if true
    if onePair == True:
        return result[7]
    if twoPair ==True:
        return result[6]
    if threeofaKind == True:
        return result[5]
    if straight == True:
        return result[4]
    if flush == True:
        return result[3]
    if fullHouse == True:
        return result[2]
    if fourofaKind == True:
        return result[1]
    if straightFlush == True:
        return result[0]
    else:
        return result[8]#Nothing
                             
def isOnePair(Hand,rank):
    """
    Checks if hand is a one pair. Compares all cards in hand with each
    and every other card to see if 2 have the same of one
    rank. Returns true if so.
    """ 
    for a in range(len(Hand)):
        for b in range(len(Hand)):
            for c in range(len(Hand)):
                for d in range(len(Hand)):
                    for e in range(len(Hand)):
                        for f in range(12):
                            if  a != b and b != c\
                               and c != d and d != e\
                               and e != f:
                                if Hand[a][0] == f\
                                   and Hand[b][0] == f:
                                    if Hand[c][0] != f\
                                       and Hand[d][0] != f\
                                       and Hand[e][0] != f:
                                        if Hand[c][0] != Hand[d][0]\
                                           and Hand[d][0] != Hand[e][0]\
                                           and Hand[e][0] != Hand[c][0]:
                                            return True
                                            print "hi"
                                
    
def isTwoPair(Hand,rank):
    """
    Checks if hand is a two pair. Compares all cards in hand with each
    and every other card to see if 2 have the same of one
    rank and 2 other have the same of another rank. Returns true if so.
    """ 
    for a in range(len(Hand)):
        for b in range(len(Hand)):
            for c in range(len(Hand)):
                for d in range(len(Hand)):
                    for e in range(len(Hand)):
                        for f in range(12):
                            for g in range(12):
                                if  a != b\
                                   and b != c\
                                   and c != d\
                                   and d != e\
                                   and e != f\
                                   and f != g:
                                    if Hand[a][0] == f\
                                       and Hand[b][0] == f\
                                       and Hand[c][0] == g\
                                       and Hand[d][0] == g\
                                       and Hand[e][0] != f\
                                       and Hand[e][0] != g:
                                        return True
                                        
                                    
                                    
def isThreeofAKind(Hand,rank):
    """
    Checks if hand is a three of a kind.
    Compares all cards in hand with each and every other
    card to see if 3 have the same rank. Returns true if so.
    """
    for a in range(len(Hand)):
        for b in range(len(Hand)):
            for c in range(len(Hand)):
                for d in range(len(Hand)):
                    for e in range(len(Hand)):
                        for f in range(12):
                            for g in range(12):
                                if  a != b\
                                   and b != c\
                                   and c != d\
                                   and d != e\
                                   and e != f\
                                   and f != g:
                                    if Hand[a][0] == f\
                                       and Hand[b][0] == f\
                                       and Hand[c][0] == f:
                                        if Hand[d][0] != Hand[a][0]\
                                           and Hand[d][0] != Hand[b][0]\
                                           and Hand[d][0] != Hand[c][0]\
                                           and Hand[d][0] != Hand[e][0]:
                                            if Hand[e][0] != Hand[a][0]\
                                               and Hand[e][0] != Hand[b][0]\
                                               and Hand[e][0] != Hand[c][0]:
                                                return True


def isFourofAKind(Hand,rank):
    """
    Checks if hand is a four of a kind. Compares all cards in hand with each
    and every other card to see if 4 have the same of one
    rank. Returns true if so.
    """ 
#Compares all cards in hand with each and every other card to see if 4 have the same rank
    for a in range(len(Hand)):
        for b in range(len(Hand)):
            for c in range(len(Hand)):
                for d in range(len(Hand)):
                    for e in range(len(Hand)):
                        for f in range(12):
                                if  a != b\
                                   and b != c\
                                   and c != d\
                                   and d != e\
                                   and e != f:
                                    if Hand[a][0] == f\
                                       and Hand[b][0] == f\
                                       and Hand[c][0] == f\
                                       and Hand[d][0] == f\
                                       and Hand[e][0] != f:
                                        return True
                                    

def isFullHouse(Hand):
    """
    Checks if hand is a full house. Compares all cards in hand with each
    and every other card to see if 3 have the same of one
    rank and the other 2 have the same of another rank.
    Returns true if so.
    """
    for a in range(len(Hand)):
        for b in range(len(Hand)):
            for c in range(len(Hand)):
                for d in range(len(Hand)):
                    for e in range(len(Hand)):
                        for f in range(12):
                            for g in range(12):
                                if  a != b\
                                   and b != c\
                                   and c != d\
                                   and d != e\
                                   and e != f\
                                   and f != g:
                                    if Hand[a][0] == f\
                                       and Hand[b][0] == f\
                                       and Hand[c][0] == f\
                                       and Hand[d][0] == g\
                                       and Hand[e][0] == g:
                                        return True
                                    


def isStraightorFlush(Hand):
    """
    Checks for straight flushes, straights and flushes.
    This Function returns 3 if it's a straight flush.
    2 if it's a straight, and 1 if it's a flush.
    n will remain 0 if it's neither.
    Returns true if so.
    """
    
    #Variable Needed for indexes, loops etc
    j = 0
    n = 0
    i = 0
    #Straight checker
    while i <= 10:
        if Hand[0][0] == i\
           and Hand[1][0] == i+1\
           and Hand[2][0] == i+2\
           and Hand[3][0] == i+3\
           and Hand[4][0] == i+4:
            n=1
        i+=1
    #Flush checker
    if Hand[0][1] == Hand[1][1]\
       and Hand[1][1] == Hand[2][1]\
       and Hand[2][1] == Hand[3][1]\
       and Hand[3][1] == Hand[4][1]: 
        n+=2
    return n
        


