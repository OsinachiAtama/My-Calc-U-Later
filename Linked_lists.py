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
        self. length = 1

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

my_linked_list = LinkedList(1)

my_linked_list.append(2)

my_linked_list.print_list()