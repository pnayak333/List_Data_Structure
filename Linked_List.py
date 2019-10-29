#Creating a Wrapper - Node

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Creating Linked List

class Linked_List:
    def __init__(self):
        self.head = None

    #Creating Append MEthod
    def append(self,data):
        New_Node = node(data)
        if self.head is None:
            self.head = New_Node
            return
        #New_Node = node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = New_Node

    #Find the Length of the list
    def leng_List(self):
        count = 0
        curr = self.head
        while curr.next != None:
            count += 1
            curr = curr.next
        return count

    #Display the Content of the list
    def Display(self):
        result = []
        curr_node = self.head
        while curr_node != None:
            print(curr_node.data)
            curr_node = curr_node.next

            #result.append(curr_node.data)
        #print(result)
    #Display the Value based on the Index
    def get(self,index):
        if index > self.leng_List():
            print("The size of the List more than the Length of the List")
        if index < 0:
            print("Ooooops! Wrong Input")
        curr_index = 0
        curr_node = self.head
        while curr_node:
            curr_node = curr_node.next
            if curr_index == index: return curr_node.data
            curr_index += 1
    #Find the Value and Display the Index of the List
    def get_val(self,val):
        if val < 0:
            print("Ooooops! Wrong Input")
        curr_node = self.head
        #curr_node = curr_node.next
        while True:
            curr_node = curr_node.next
            if curr_node.data == val:
                return curr_node.data

    def remove(self,val):
        curr_index = 0
        curr_node = self.head
        if curr_node.data == val:
            self.head = curr_node.next
            curr_node = None
            return


        while curr_node.next != None:
            lst_node = curr_node
            curr_node = curr_node.next
            if curr_node.data == val:
                lst_node.next = curr_node.next
                return curr_node.data
            #curr_index+=1



my_list = Linked_List()

my_list.Display()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
my_list.append(1)
print(my_list.leng_List())
my_list.Display()
print("The 2nd Index of the List is:", my_list.get(2))
print("Get_Value of Number:",my_list.get_val(50))
print("The 2nd Index of the List is Removed:", my_list.remove(10))
my_list.Display()

