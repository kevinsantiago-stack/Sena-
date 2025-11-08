class BSTNode:
    def __init__(self,val): self.val=val; self.left=None; self.right=None
    def insert(self,x):
        if x<=self.val:
            if self.left: self.left.insert(x)
            else: self.left=BSTNode(x)
        else:
            if self.right: self.right.insert(x)
            else: self.right=BSTNode(x)

if __name__=='__main__':
    root=BSTNode(10); root.insert(5); root.insert(15); print(root.left.val, root.right.val)
