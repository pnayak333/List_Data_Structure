class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def Insert(self,data):
        New_node = node(data)
        if self.head is None:
            self.head = New_node
            return

        Curr_Node = self.head
        while Curr_Node.next != None:
            Curr_Node = Curr_Node.next
        Curr_Node.next = New_node

    def Display_Node(self):
        Curr_node = self.head
        while Curr_node.next != None:
            #print(Curr_node.data)
            Curr_node = Curr_node.next
            print(Curr_node.data,"\n||")
            #result.append(Curr_node.data)
        #print(result)

    def Prepend(self,data):
        Curr_Node = self.head
        New_head = node(data)

        New_head.next = Curr_Node
        Curr_Node = New_head
        #my_list.Display_Node()
        #return self.head
    def Remove_Duplicate(self):
        curr = self.head
        prev = None

        #creating Dictionary
        dup_values = dict()

        while curr.next !=None:
            if curr.data in dup_values:
                prev.next = curr.next
                curr = None
            else:
                dup_values[curr.data] = 1
                print("Dict:",dup_values[curr.data],dup_values)
                prev = curr
            curr = prev.next

    def RemoveDuplicates_Without_Dict(self):
        current = self.head
        while current:
            runner = current
            while runner.next != None:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
    def length_List(self):
        curr = self.head
        length = 0
        while curr.next!=None:
            curr = curr.next
            length +=1
        return length

    def Nth_To_end(self,n):
        p = self.head
        f = self.head
        count = 0
        while count < n-1:
            f = f.next
            count +=1
        while f.next != None:
            f = f.next
            p = p.next
        print(p.data)
    def Delete_Middle_Node(self):
        def delete_mid(mid):
            curr =self.head
            index = 0
            while curr:
                #last = curr
                curr = curr.next
                if index == mid:
                    print(index,mid,"Deleted:",curr.data)
                    temp = curr.next
                    curr.data = temp.data
                    curr.next = temp.next
                    print(temp.data)
                index += 1
        length = 0
        c = self.head
        while c.next != None:
            length += 1
            c = c.next

        mid = length // 2
        print(mid,length)
        count = 0

        delete_mid(mid)













#result = []
my_list = Linked_List()

my_list.Insert(5)
my_list.Insert(15)
my_list.Insert(18)
my_list.Insert(19)
my_list.Insert(14)
my_list.Insert(16)
my_list.Insert(17)
my_list.Insert(12)

#print(my_list.length_List())
#print(my_list.Nth_To_end(5))
my_list.Delete_Middle_Node()
print(" ")
#my_list.Display_Node()

#my_list.Remove_Duplicate()
#my_list.RemoveDuplicates_Without_Dict()
#my_list.RemoveDuplicates_Without_Dict()
my_list.Display_Node()
print(" ")
#my_list.Prepend(1)
#my_list.Display_Node()
