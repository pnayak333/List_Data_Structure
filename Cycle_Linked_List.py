class Node(object):
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



    def Detect_Cycle(self):
        slow = my_list1.head
        fast = my_list1.head.next

        while fast and fast.next != None:
            print("Slow:",slow.data,"Fast:",fast.data)
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return  False

my_list1 = Linked_List()
my_list2 = Linked_List()


my_list1.Inser_List(1)
my_list1.Inser_List(2)
my_list1.Inser_List(4)
my_list2.Inser_List(5)

my_list1.head.next.next.next = my_list2.head
if my_list1.Detect_Cycle():
    print("Cyle00")
else:
    print("Not")