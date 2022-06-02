class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data==self.data:
            return
        
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinaryTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinaryTree(data)

    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()
        
        elements.append(self.data)

        if self.right:
            elements+=self.right.in_order_traversal()

        return elements

    def search(self,val):
        if self.data==val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False 
        
        if val > self.data:
            if self.right:
                return self.right.search(val)

            else:
                return False

def build_tree(elements):
    root=BinaryTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root
if __name__ == '__main__':
    list=[55,66,99,22,44,77,62,34,94,86,456,543218,5476321]
    tree=build_tree(list)
    print(tree.in_order_traversal())
    print(tree.search(66))
