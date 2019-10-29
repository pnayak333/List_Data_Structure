class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.prev = None
class Doubly_Linked_list:
    def __init__(self):
        self.head = node()
    def append(self,data):
        if self.head is None:
            New_Node = node(data)
            New_Node.prev = None
            self.head = New_Node
        else:
            New_Node = node(data)
            Curr_node = self.head
            while Curr_node.next:
                Curr_node = Curr_node.next
            New_Node.prev = Curr_node
            New_Node.next = None
    def Display(self):
        result = []
        Curr = self.head
        while Curr.next != None:
            #print(Curr.data)
            Curr = Curr.next
            result.append(Curr.data)
            #return result
        print(result)

my_dobly = Doubly_Linked_list()

my_dobly.append(1)
my_dobly.append(11)
my_dobly.append(12)
my_dobly.append(13)

my_dobly.Display()