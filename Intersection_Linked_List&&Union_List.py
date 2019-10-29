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
    def InterSection_List(self,my_List2):
        if self.head is None or my_List2.head is None:
            return None
        p1 = self.head
        p2 = my_List2.head
        len_p1 = 0
        len_p2 =0
        while p1:
            len_p1 += 1
            print("Inside P1:",p1.data)
            p1 = p1.next

        while p2:
            len_p2 +=1
            print("Inside P2:",p2.data)
            p2 = p2.next

        print("Len P1:",len_p1,"Len : P2",len_p2)

        p1 = self.head
        p2 = my_List2.head

        if len_p1 > len_p2:
            for i in range(len_p1-len_p2):
                print("Inside Loop P1",p1.data)
                p1 = p1.next

        elif len_p2 > len_p1:
            for i in range(len_p2 - len_p1):
                print("Inside Loop P2 ", p2.data)
                p2 = p2.next

        while p2 != p1:
            p1 = p1.next
            p2 = p2.next
        return True



my_List1 = Linked_List()
my_List2 = Linked_List()
obj = Linked_List()

my_List1.List_Apped('A')
my_List1.List_Apped('B')
my_List1.List_Apped('C')
my_List1.List_Apped('D')
my_List1.List_Apped('E')
my_List1.List_Apped('F')
my_List1.List_Apped('G')

my_List2.List_Apped('I')
my_List2.List_Apped('J')
my_List2.List_Apped('K')
my_List2.List_Apped('E')
my_List2.List_Apped('F')

print("Node A:")
my_List1.Display_Node()
print("Node B:")
my_List2.Display_Node()

#size1 = int(input("Enter the size of the Linked list1:"))
#for i in range(size1):
#    node = Node(i)
#    my_List1.List_Apped(node)
#size2 = int(input("Enter the size of the Linked list2:"))
#for i in range(size2):
#    node = Node(i)
#    my_List2.List_Apped(node)

print(my_List1.InterSection_List(my_List2))
#print(intersection)