class UnionFind(object):
    def __init__(self,n):
        self.table=[-1]*n
 
    def find(self,x):
        parent=self.table[x]
        if parent<0:
            return x
        else:
            root=self.find(parent)
            self.table[x]=root
        return root
 
    def union(self,a,b):
        root1=self.find(a)
        root2=self.find(b)
        if root1 != root2:
            if self.table[root1] != self.table[root2]:
                if self.table[root1] < self.table[root2]:
                    self.table[root2]=root1
                else:
                    self.table[root1]=root2
        else:
            self.table[root1]+=(-1)
            self.table[root2]=root1
