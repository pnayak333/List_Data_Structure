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
    def Sum_List(self,my_list2):
        p = self.head
        q = my_list2.head
        sum_Lst = []
        carry = 0
        while p and q:
            if not p:
                i=0
            else:
                i = p.data
            if not q:
                j=0
            else:
                j = q.data
            sum  = i+ j + carry
            if sum  >= 10:
                carry = 1
                remainder = sum % 10
                sum_Lst.append(remainder)
            else:
                carry = 0
                sum_Lst.append(sum)
            #if p:
            p = p.next
            #if q:
            q = q.next

        print(sum_Lst)





my_list1 = Linked_List()
my_list2 = Linked_List()


my_list1.Inser_List(1)
my_list1.Inser_List(2)
my_list1.Inser_List(4)

#Linked_List1 = Node(1, Node(2, Node(3, Node(4))))

#ssert not Detect_Cycle(Linked_List1)
my_list2.Inser_List(15)
my_list2.Inser_List(15)
my_list2.Inser_List(15)
my_list1.Display()
my_list1.Sum_List(my_list2)
my_list1.Display()



