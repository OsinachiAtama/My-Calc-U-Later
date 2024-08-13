 # Using Constructors and Classes
'''
class Company: 
    def __init__(self): # Here, the parameters name, age and weight belong to the object not the function. 
        #Look in the blocks below to see how to make the parameters belong to the function so that you can just 
        #call them in as you call the function
        self.name = "n/a"
        self.age = 0
        self.weight = 0.0
    
    def print_company(self): 
        print(f"Name : {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight}lbs.\n")


if __name__ == "__main__": 
    company1 = Company()
    company1.name ='Apple'
    company1.age = 60 
    company1.weight = 500
    company1.print_company()



# ******************************************Definig  a class with parameters
class Company: 
    def __init__(self, name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    def print_company(self): 
        print(f"Name : {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight}lbs.\n")

if __name__ == "__main__" : 
    company1 = Company("Turner", 100,500)
    company1.print_company()
'''

# ****************************************** Linked lists as dictionaries


# print("biscuit")

# head = {
#     "value" : 11, 
#     "next"  :{
#         "value" : 3, 
#         "next"  :{
#             "value" : 23, 
#             "next"  :{
#                 "value" : 7, 
#                 "next"  : None
                
#             }
#         }

#     }


# }

#print(head["next"]["next"]["value"])

#This will work for linked lists: 
#print(my_linked_list.head.next.next.value)

#**********************************************Linked lists 
'''
class Linkedlist : 
    def __init__(self,value): #the word self in the function shows that this is a constructor and not a regular function
        #creates new Node
    def append(self, value): 
        # create new Node 
        #add Node to end
    def prepend(self, value): 
        # create new Node 
        #add Node to the beginning
     def insert(self,index, value): 
        # create new Node 
        # inset node at index
'''
class Node : 
    def __init__(self,value) :
        self.value = value 
        self.next = None

class LinkedList: 
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    #******************************Looking at all the values in a linked list 

    def print_list(self): 
        temp = self.head
        while temp is not None: 
            print(temp.value)
            temp = temp.next

        #****************************Appending an item to the end of a list

    def append (self, value): 
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node 
            self.tail = new_node 
        else : 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop (self): 
        temp = self.head # Container for the head
        pre = self.head
        
        if self.length == 0 : # No value in list scenario
            print('This linked list is empty')
            return None
              
            
        while temp.next is not None: # while there is more than one item on the list
            pre = temp  #pre and temp are the same value
            temp = temp.next # temp is now the next value
        self.tail = pre # while loop has ended which means pre is now on the last value and temp is now on None
        self.tail.next = None 
        self.length -=1
        if self.length == 0 : # this means that after the length of the ll was decreased once, there was nothing left so there is only one value in the list
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value): 
        new_node = Node(value)   # making a node for the new value
        if self.length == 0:  # empty list
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head #  attaching new node to linked list
            self.head = new_node # declaring new node as head
        self.length += 1    
        return True
    
    def pop_first(self): 
        if self.length == 0 : 
            return None

        temp = self.head # container
        
        self.head = self.head.next  # head is now next item on the list
        temp.next = None # temp has been broken off
        self.length -=1

        if self.length == 0 : 
            self.tail = None
        return temp.value
    
    def get(self,index): # Will provide the value at the index
        if (index < 0 or index >= self.length) :
            return None
        temp = self.head
        for _ in range (index): #moves temp the number of times of the index to arrive at the right value
            temp = temp.next
        return temp

    def set_value(self,index,value): # changes value at a given index 
        #new_node = Node(value)
        if (index < 0 or index >= self.length) : #you can use temp = self.get(index,  but I am too tired right now to make sense of that)
            return "impossible, out of range"
        temp = self.head
        for _ in range (index): 
            temp = temp.next 
        temp.value = value
        my_linked_list.print_list()
        return True
    
    # def insert (self, index, value): 
    #     new_node = Node(value)
    #     temp = self.get(index)
    #     if temp is not None: 
    #         temp.next = new_node
    #         if index == self.length - 1: 
    #             new_node = self.tail
    #             self.tail.next = None
    #         return True
    #     return False
    
    def insert (self, index, value): 
        if (index < 0 or index >= self.length) :
            return False
        if index == 0: 
            return self.prepend(value)
        if index == self.length : 
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next 
        temp.next = new_node 
        self.length +=1 
        return True
    def remove (self, index):
        if (index < 0 or index >= self.length) :
            return None
        if index == 0: 
            return self.pop_first()
        if index == self.length : 
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next 
        temp.next = None
        self.length -=1
        return temp
    
    # def reverse(self): 
    #     if self.length == 0 :
    #         return None 
    #     if self.length == 1 :
    #         return self
    #     pre = self.head 
    #     temp = self.tail 
    #     mid = self.head.next
    #     self.head = temp 
    #     self.head.next = pre.next
    #     self.tail = pre 
    #     pre.next = None

    #     while _ in range self.length - 1 : 


    def reverse(self): 
        temp = self.head 
        self.head = self.tail
        self.tail = temp
        after = temp.next 
        before = None 

        for _ in range(self.length) : 
            after = temp.next 
            temp.next = before
            before = temp
            temp = after 
        
        




    

        

            

my_linked_list = LinkedList(1)

my_linked_list.append(2)

#my_linked_list.print_list()

# print(my_linked_list.pop())
# print(my_linked_list.pop())
# print(my_linked_list.pop())

my_linked_list.prepend(8)
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())

#my_linked_list.print_list()

print(my_linked_list.get(2))
my_linked_list.set_value(2,10)
my_linked_list.insert(2,15)

my_linked_list.print_list()
#my_linked_list.remove(2)
my_linked_list.reverse()
my_linked_list.print_list()
