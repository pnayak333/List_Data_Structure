class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#--------------------------------------------------------------------------------------

class Linked_List:
    def __init__(self):
        self.head = None

    def Inser_List(self,data):
        New_Node = Node(data)
        if self.head is None:
            self.head = New_Node
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = New_Node
#--------------------------------------------------------------------------------------
    def Display(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
#-------------------------------------------------------------------------------------------
    def Partition_List(self,my_list,x):
        curr = self.head
        left_Node = Node(0)
        left = left_Node
        right_Node = Node(0)
        right = right_Node

        while (curr != None):
            if curr.data <= x:
                left.next = curr
                left = left.next
            else:
                right.next = curr
                right = right.next
            curr = curr.next
        right.next = None
        left.next = right_Node.next
        return left.next

my_list = Linked_List()

#n = int(input("Enter The length of Linked List"))
#for i in range(0,n):
    #x = int(input("Enter The value:"))
    #my_list.Inser_List(x)
my_list.Inser_List(1)
my_list.Inser_List(8)
my_list.Inser_List(3)
my_list.Inser_List(5)
my_list.Inser_List(4)
my_list.Inser_List(11)
my_list.Inser_List(7)


my_list.Display()
my_list.Partition_List(my_list,4)
#print(my_list.partition(my_list,4))
print('----------------------------------------------')
my_list.Display()