class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
    def List_Apped(self,data):
        New_Node = Node(data)
        if self.head is None:
            self.head  = New_Node
            return
        #New_Node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = New_Node
    def Display_Node(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next

    def Prepend(self, data):
        New_Node = Node(data)
        #Curr_Node = self.head
        New_Node.next = self.head
        self.head = New_Node


    def Planindrome_Linked_List(self,Node) -> bool:
        runner = self.head
        current = self.head

        while(runner != None and runner.next != None):
            my_list.append(current.data)
            print(my_list)
            current = current.next
            runner = runner.next.next
        if runner != None: current = current.next
        while current != None:
            if (my_list.pop() != current.data):
                return False
                print(my_list.pop())
            current = current.next
        return True
    def Reverse_Linked_List(self):
        curr = self.head
        prev = None

        while curr:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
            #rev.append(prev.data)
            print(prev.data)



my_list = []
rev = []
my_obj = Linked_List()
my_obj.List_Apped("A")
my_obj.List_Apped("B")
my_obj.List_Apped("C")
my_obj.List_Apped("D")
my_obj.List_Apped("E")
#my_obj.Prepend("X")
#my_obj.Display_Node()
my_obj.Reverse_Linked_List()
#my_obj.Display_Node()
#print(my_obj.Planindrome_Linked_List(my_obj))
#my_obj.Method_1_Palindrome()