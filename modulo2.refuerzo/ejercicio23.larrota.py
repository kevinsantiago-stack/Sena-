class LinkedNode:
    def __init__(self,val): self.val=val; self.next=None
class LinkedList:
    def __init__(self): self.head=None
    def append(self,val):
        n=LinkedNode(val)
        if not self.head: self.head=n; return
        cur=self.head
        while cur.next: cur=cur.next
        cur.next=n

if __name__=='__main__':
    ll=LinkedList(); ll.append(1); ll.append(2); print(ll.head.val, ll.head.next.val)
