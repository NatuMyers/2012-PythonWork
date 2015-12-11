"""
Assignment: Assignment 6, Linked Lists

Description:
Complete the functions count,
addBefore, reverse, and bubbleSort.

Class: CISC 121, October 5th, 2012
Author: Natu Myers
Student Number: 10068437
"""

def count(linkedList, target):
    """
    Returns the number of times the target occurs in the list.
    If the target is not in the list at all, returns zero.
    """
    counter = 0

    #Current node starts as the value of the
    #1st element's dictionary (which is just a pointer to the next node/element)   
    currentNode = linkedList
    
    while currentNode != None:
        if currentNode['data'] == target:
            counter += 1
        currentNode = currentNode['next']
        
    return counter

def addBefore(linkedList, value, newValue):
    """
    Finds a value in the list and adds a new value directly
    before it.  Returns a pointer to the beginning of the
    modified list.  If the first value doesn't occur in the list,
    writes an error message and returns a pointer to the beginning
    of the unchanged list.  If value occurs more than once in
    the list, insert newValue before the first occurrence.

    For full marks, you may not implement this function by finding the
    value in the list, noting its position, and calling insertValue.
    If the value is in a long list, that would involve travelling through
    a lot of nodes once to find value and again to insert the new value.
    For better efficiency, you should be walking down the chain of nodes
    before the value only once.
    """

    #referenceNode is the node with the value
    #newNode is before reference node
    #beforereferencenode is supposed to be before newNode
    legalValue = False
    referenceNode = linkedList

    while referenceNode != None:#while not at the end of list
        if referenceNode['data'] == value:
            legalValue = True
            break
        referenceNode = referenceNode['next']#move it forward

    if legalValue == False:#error check
        print "error in addBefore:",value,"is not an element of the list"
        return linkedList

    newNode = {}#all new elements are dicts.
    newNode["data"] = newValue

    beforeNewNode = linkedList
    #Assign beforeNewNode to the first element in the list...
    #...then move it along the list in the while loop

    
    while beforeNewNode != None:
        #if beforeNewNode points to referenceNode
        if beforeNewNode['next'] == referenceNode:
            beforeNewNode['next'] = newNode#make it point to newNode instead
            newNode['next'] = referenceNode#Make it point to reference node
            break
        beforeNewNode = beforeNewNode['next']#increment

    if beforeNewNode == None:
        #If the code got this far, there is a legal value,
        #but beforeNewNode can't be represented by anything in the list...
        #...because beforeNewNode['next'] skips over reference node
        #In this case reference node is the first element

        newNode['next']=referenceNode
        linkedList=newNode #newNode is the first element

    return linkedList

def reverse(linkedList):
    finderNode = linkedList
    listSize = getSize(linkedList)
    
    #Elements will be moved from linked list to revPList in reverse order
    revPList = []
    tmpNode = {}
    
    n=1
    while n <= listSize:
        finderNode = linkedList
        
        for i in range(listSize-n):
            finderNode = finderNode['next']
            #Add values backwards to a python list
        revPList.append(finderNode["data"])

        n+=1               
        #THE FIRST ITERATION THOUGH THE FOR LOOP WORKS
        #BUT THE SECOND STOPS AT 2

    revList=createList(revPList)

    return revList

def bubbleSort(linkedList):
    #Shouldn't return anything but should modify the list itself
    #Move values of the nodes. not the nodes
    """
    Sorts linkedList using a bubble sort.  
    """
    listSize = getSize(linkedList)

    firstCompared = {}
    secondCompared = {}

    #temp variables used for swapping
    tmp_firstData = 0
    tmp_secondData = 0

    swapped = False
    for i in range(0,listSize-1):
        firstCompared = linkedList
        secondCompared = linkedList['next']

        #We cut off the already sorted part of list each iteration
        for j in range(0,listSize-i-1):
            if firstCompared['data'] > secondCompared['data']:
                #if it's not in order...
                
                #make temp variables
                tmp_firstData= firstCompared['data']
                tmp_secondData= secondCompared['data']
                #then use them to swap data values
                firstCompared['data'] = tmp_secondData
                secondCompared['data'] = tmp_firstData
                swapped = True
            #increment the pointers afterwards
            secondCompared = secondCompared['next']
            firstCompared = firstCompared['next']

        if not swapped:#Leave Early if already sorted
            break

# DO NOT CHANGE OR ADD ANYTHING BELOW THIS COMMENT!  Leave the
# functions developed in class as they are.

def insertValue(linkedList, index, value):
    """
    Adds a new element to a list.
    Parameters:
        value: the value for the new element
        index: the index for the new list element
    The new value does not replace the current element at
    position index; it is inserted before that element and
    the size of the list grows by 1.
    
    The return value is the head of the modified list.
    (That's usually the same as the lis parameter, unless
    we've added a new first element.)
    
    If the index is out of bounds, prints an error message and
    returns the list unchanged.
    """

    # create a new node to hold the value
    newNode = {'data': value}
    
    # special case: inserting at the beginning
    if index == 0:
        # This node is now the first node.  The first node of
        # the original list comes right after it.
        newNode['next'] = linkedList
        return newNode

    else:
        # find the node right before the insertion point    
        before = nthNode(linkedList, index-1)
        if before == None:
            print "Error: illegal index to insertValue"
            return linkedList
        else:
            after = before['next'] # the node after the insertion point
            before['next'] = newNode
            newNode['next'] = after
            return linkedList # same first node

        
def listString(linkedList):
    """
    Returns a string describing the list, suitable for printing.
    """
    description = "["
    isFirst = True
    node = linkedList
    while node != None:
        if isFirst:
            isFirst = False
        else:
            description += ","
        description += str(node['data'])
        node = node['next']
    description += "]"
    return description


def printList(linkedList):
    """
    Prints a representation of a list
    """
    print listString(linkedList)
    

def createList(plist):
    """
    Creates and returns a linked list containing all of the elements
    of the Python-style list parameter.  A useful shortcut for testing.
    """
    linkedList = None
    for index in range(len(plist)-1, -1, -1):
        linkedList = insertValue(linkedList,0, plist[index])
    return linkedList
        

def nthNode(linkedList, n):
    """
    Helper method: returns a reference to node n in a list
    (counting from zero).
    Parameters: the list and an index n
    If there is no node n, returns None.
    """
    if n < 0 or linkedList == None:
        return None
    
    count = 0
    node = linkedList
    while count < n:
        node = node['next']
        if node == None:
            return None
        count += 1
    return node


def get(linkedList, index):
    """
    Returns the value of a list element
    Parameters: the list and the index of the element
    If the index is not the index of an existing list element,
        prints an error message and returns None
    """
    node = nthNode(linkedList, index)
    if node == None:
        print "Error: illegal index to get function"
        return None
    else:
        return node['data']


def set(linkedList, index, value):
    """
    Changes the value of a list element
    Parameters: the index of the element and the new value
    No return value (always None).
    If the index is not the index of an existing list element,
        writes an error and returns the list unchanged
    """
    node = nthNode(linkedList, index)
    if node == None:
        print "Error: illegal index to set function"
        return
    node['data'] = value



def delete(linkedList, index):
    """
    Deletes an element from a linked list.
    Parameter: list and index of the element to delete
    
    The return value is the head of the modified list.
    (That's usually the same as the linkedList parameter, unless
    we've deleted the first element.)
    
    If the index is out of bounds, writes an error message and
    returns the list unchanged.
    """

    # special case: deleting first element
    if index == 0 and linkedList != None:
        return linkedList['next']

    else:
        # the node before the one we're going to delete
        before = nthNode(linkedList, index-1)
        if before == None:
            print "Error: illegal index to delete function"
            return linkedList
        nodeToDelete = before['next']
        if nodeToDelete == None:
            print "Error: illegal index to delete function"
            return linkedList
        before['next'] = nodeToDelete['next']
        return linkedList


def getSize(linkedList):
    """
    Returns the size of a list
    """
    count = 0
    node = linkedList
    while node != None:
        count += 1
        node = node['next']
    return count






