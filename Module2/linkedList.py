class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
        def __init__(self):
            self.head = None

def PrintList(self):
    temp = self.head
    if(temp !=None):
        print("The list contains: ", end = " ")
        while(temp != None):
            print(temp.data, end = " ")
            temp = temp.next
        print()
    else:
        print("The list is empty")

#Create a new node at the start of the list
def PushFront(self, newElement):
    newNode = Node(newElement)
    #self.head is the current head of the list.
    newNode.next = self.head
    self.head = newNode

#Create a new node at the end of the list
def PushBack(self, newElement):
    newNode = Node(newElement)

    #If the list is empty, the new node is the head of the list
    if(self.head == None):
        self.head = newNode
        return

    #Else, traverse the list until we reach the last one
    else:
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        #set the .next of the last element to the new element
        temp.next = newNode

def Insert(self, newElement, position):
    newNode = Node(newElement)
    if (position < 1):
        print("\nposition should be greater than 1.")

    elif(position == 1):
        #make the new node the first element, change .next of current head before changing current head to be the new node
        newNode.next = self.head
        self.head = newNode
    
    else:
        temp = self.head
        #scrolls through the list until it reaches the target position. This temp node is carried on to the next if statement
        for i in range(1, position - 1):
            if(temp != None):
                temp = temp.next
        
        if(temp != None):
            #Sets the new node in front of the target position node.
            newNode.next = temp.next
            temp.next = newNode
        else:
            print("\nThe previous node is null.")

def popFront(self):
    if(self.head != None):
        temp = self.head
        self.head = self.head.next
        temp = None

def popBack(self):
    if(self.head != None):
        if(self.head.next == None):
            self.head = None
            #Special occation when head is not null and next is null, set head to null.
        else:
            temp = self.head
            while(temp.next.next != None):
                temp = temp.next
            lastNode = temp.next
            temp.next = None
            lastNode = None

def pop_at(self, position):
    if(position < 1):
        print("\nPosition should be >= 1.")
    elif (position == 1 and self.head != None):
        nodeToDelete = self.head
        self.head = self.head.next
        nodeToDelete = None
    else:
        temp = self.head
        for i in range(1, position-1):
            if(temp != None):
                temp = temp.next
        
        if(temp != None and temp.next != None):
            nodeToDelete = temp.next
            temp.next = temp.next.next
            nodeToDelete = None
        else:
            print("\nThe node is already null.")

MyList = LinkedList()

first = Node(10)
second = Node(20)
third = Node(30)

MyList.head = first
first.next = second
second.next = third


PushFront(MyList, 202)
PushBack(MyList, 230)
Insert(MyList, 1, 1)
PrintList(MyList)
popFront(MyList)
PrintList(MyList)
popBack(MyList)
PrintList(MyList)
pop_at(MyList, 2)
PrintList(MyList)