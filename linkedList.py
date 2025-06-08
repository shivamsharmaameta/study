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
            
    def search(self, val):
        cur = self.head
        pos = 1
        while(cur):
            if cur.val == val:
                print(f"Found at {pos}")
                return
            cur = cur.next
            pos += 1
        print("Not Found!")

def merge(l1, l2):
    h1 = l1.head
    h2 = l2.head
    
    while(h1.next):
        h1 = h1.next
    h1.next = h2

def detectLoop(l):
    # First create a loop using following line of code in main and remove printAll() method.
    # l1.head.next.next.next = l1.head.next

    cur = l.head

    # Using Hashset
    s = set()
    while(cur):
        if cur in s:
            print("Loop Detected! using Hashset.")
            return
        s.add(cur)
        cur = cur.next
    
    # Floyd's Cycle-Finding Algorithm.    
    slow = fast = cur
    while(slow and fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print("Loop Detected! using Floyd's Cycle-Finding Algorithm.")
            return
        cur = cur.next
        
if __name__ == "__main__":
    l1 = LL("A", "B", "C", "D")
    