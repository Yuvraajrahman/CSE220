#Step1: Creating a Node class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
#step2: creating a LinkedList class:
 
#tast1 (MyList Class)       
class MyList:
    size = 0
    #declaring head  as NONE:
    def __init__(self):
        self.head = None

#task2 (showList)
    def showList(self):
        if self.head is None:
            print("Empty list")
            return

        nN = self.head
        while nN is not None:
            print(nN.data,end= ' ')
            nN = nN.next

#task3 (isEmpty)  
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
#task4  (clear)
    def clear(self):
        while self.head is not None:
            new_node = self.head
            self.head = self.head.next 
            new_node = None

#task5 (insert)
    def insertAtEnd(self, newElement):
        new_node = Node(newElement)                 #creating a node
        self.size+=1
        if self.head is None:                       #if there is no element at fist position of the list then 
            self.head = new_node                    #new node is the new element with referece of self.head
        
        
        #Finding the last element and inserting there: 
        
        else:                                       #if there is already elements in the list
            check = self.head  
            if new_node.data == check.data:         #searching for similar data
                    print("element already exist")
            else:
                while check.next is not None:           #if next reference is the null, then 'check' is at the last element/node
                    check = check.next                  #continuing the loop
                check.next = new_node               #changing the referene of the last Node into new_node's reference 
                                                                    #as it is the last element/node now


#task6 (Insert at index)
    def insert(self,newElement, index):
 
        Node_pos = index +1     
        newNode = Node(newElement) 
        self.size+=1
        
        if( Node_pos == 1):                        #if the index is 0, size = 1(Fist Node)
            newNode.next = self.head
            self.head = newNode                 
            
        elif (Node_pos >1):    
            temp = self.head
            for i in range(1, Node_pos-1):
                if(temp != None):
                    temp = temp.next   
            if(temp != None):
                newNode.next = temp.next
                temp.next = newNode  
        else:
            print("\Invalid Index")
        

#Extra
    def insertAtBeginning(self, newElement):
        new_node = Node(newElement)                                 #adding newElement to new_node
        new_node.next = self.head                                   #the reference of self.head will be added to new_node reference
        self.head = new_node                                        #storing the reference of the new_node in the 
        self.size += 1                                             #self.head as new_node is the new first element of the linked  list
    

#Task7: (Remove Node)
    def remove(self, deletekey):

        if self.head is not None:
            if deletekey == self.head.data:
                self.head = self.head.next
                self.head = None
                return


        new = self.head
        while new is not None:
            if new.data == deletekey:
                print(deletekey)
                break
            tmp2 = new
            new = new.next

        if (self.head == None):
            return
        tmp2.next = new.next





# Advanced task1: Get Even Numbers

    def even(self):
        tmp1=self.head
        test1=MyList()
        if test1 is not None:
            while tmp1 is not None:
                if(tmp1.data %2 == 0):
                    test1.insertAtEnd(tmp1.data)
                tmp1=tmp1.next
            test1.showList()
            return
        

#Advanced task2:
#Check Presence of an element:

    def check(self,c1):
        tmp1 = self.head
        test1 = MyList()
        if test1 is not None:
            while tmp1 is not None:
                if(tmp1.data == c1):
                    print("\nTrue")
                    return True
                tmp1 = tmp1.next
                
            print("\nFalse")



#A Second TesterClass to get desired outputs:
class TesterClass:
    def __init__(self):
        self.head = None
        # self.tail = None
        
    #add at end for other functions
    def addnew(self, data):
        new_node = Node(data)                      # adding data and creating a new Node
        if (self.head == None):                 # both head and tail will point at new_node since 
            self.head = new_node                # it will be the fist node of the list
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node                        # making new_node the new tail of the list as
                                                        # the value stays at last index when we push new node.
    #add at beginning for other functions
    def insertAtBeginning(self, newElement):
        new_node = Node(newElement)                                 #adding newElement to new_node
        new_node.next = self.head                                   #the reference of self.head will be added to new_node reference
        self.head = new_node                                        #storing the reference of the new_node in the 
      
      
#Advanced task3: (Reverse)

    def reverse(self):
            tmp1 = self.head                     
            tmp2 = None
            
            while(tmp1 is not None):
                next = tmp1.next                    #saving next reference to a variable
                tmp1.next = tmp2                    #changing  reference of head node(tmp1) to None(tmp2) 
                tmp2 = tmp1                         #looping with crawl one position ahead
                tmp1 = next                         #after completing the loop, the head reference becomes one as the 
            self.head = tmp2                            #tail value should be Null.
            

#advanced task4: (Sort)
# Sorting the given list:
    def sortList(self):

        tmp1 = self.head                                # tmp1 is the present element, pointing at head
        tmp2 = None                                     # tmp2 is index which will assist while looping through

        if (self.head == None):
            return
        else:
            while (tmp1 != None):

                tmp2 = tmp1.next                        # switching node index from next to current

                while (tmp2 != None):

                    if (tmp1.data > tmp2.data):         # swapping data if new node's data is greater then index's data
                        temp = tmp1.data
                        tmp1.data = tmp2.data
                        tmp2.data = temp
                    tmp2 = tmp2.next
                tmp1 = tmp1.next


#Advanced task5 : (Sum)               

    def sum(self):
        tmp1 = self.head
        sum = 0
        while (tmp1 != None):
            sum = sum + tmp1.data
            tmp1 = tmp1.next

        print("sum:",sum)


# Advanced task6: (Rotate)   
    def rotate(self, k):
    
        tmp1 = self.head
    
    
        while tmp1.next is not None:     #looping until the last node of the list
            tmp1 = tmp1.next
    
        tmp1.next = self.head
        tmp1 = self.head
        
        while range(k - 1):          #The last element of the array will be (k-1) while rotating
            tmp1 = tmp1.next
    
    
        self.head = tmp1.next
        tmp1.next = None
        return self.head



    #print Outputs:

    def showList(self):  
        tmp1 = self.head
        if (self.head == None):
            print("Empty List")
            return
        while (tmp1 != None):
            
            print(tmp1.data, end=" ")
            tmp1 = tmp1.next
        print(" ")









#From MyList Class:                    
list1 = MyList()
#Adding values to data
list1.insertAtBeginning(101)
list1.insertAtEnd(25)
list1.insertAtEnd(91)
list1.insertAtEnd(87)
list1.insertAtEnd(1)
list1.insert(120,1)
list1.showList()
list1.isEmpty()
print("\nremoved given key:")
list1.remove(1) 
list1.showList()
#list1.clear()   
'''Kindly remove the hashtag of "list1.clear()" to see the output,
this function was commented so that it doest remove all the elements
before testing other functions.'''    

#ADVANCED:
#From list1:
print("\nThe even elements:")
list1.even()
print("\nChecking if this element present:")
list1.check(120)



#From TesterList class 
list2 = TesterClass()
# adding values to data:
list2.addnew(8)
list2.addnew(7)
list2.addnew(6)
list2.addnew(1)
list2.addnew(2)
print("Original list2:  ")
list2.showList()
list2.sortList()
print("New Sorted list:  ")
list2.showList()
list2.sum()
#list2.rotate(3)
list2.showList()
list2.reverse()
print("\nReversed: ")
list2.showList()