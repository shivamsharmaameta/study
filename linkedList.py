class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LL:
    def __init__(self,*args):
        self.head = None
        if args:
            for i in args:
                self.insertAtEnd(i)
    def insertAtEnd(self,val):
        if self.head:
            new = Node(val)
            cur = self.head
            while(cur.next):
                cur = cur.next
            cur.next = new
        else:
            new = Node(val)
            self.head = new
    def insertAtStart(self,val):
        if self.head:
            new = Node(val)
            new.next = self.head
            self.head = new
        else:
            new = Node(val)
            self.head = new
    
    def insertAtPos(self,val, pos):
        if self.head:
            new = Node(val)
            cur = self.head
            for i in range(1,pos-1):
                cur = cur.next
            temp = cur.next
            cur.next = new
            new.next = temp
        else:
            new = Node(val)
            self.head = new
    
    def deleteAtLast(self):
        if self.head:
            cur = self.head
            try:
                while(cur.next.next):
                    cur = cur.next
                cur.next = None
            except:
                self.head = None
        else:
            print("No element to delete.")
            
    def deleteAtStart(self):
        if self.head:
            temp = self.head.next
            self.head = temp
        else:
            print("No element to delete.")
    
    def deleteAtPos(self,pos):
        if pos == 1:
            self.deleteAtStart()
        elif self.head:
            cur = self.head
            try:
                for i in range(1,pos-1):
                    cur = cur.next
                temp = cur.next.next
                cur.next = temp
            except:
                print(f"No element at position {pos}")
        else:
            print("No element to delete.")

    def printAll(self):
        cur = self.head
        ele = []
        while(cur):
            ele.append(str(cur.val))
            cur = cur.next
        if ele:
            print("->".join(ele))
        else:
            print("Empty List")


l = LL("A", "B", "C", "D")

l.printAll()
