class Tree:
    def __init__(self, data, lt=None, rt=None):
        self.data = data
        self.lt = lt
        self.rt = rt

    def inorder(self):
        # print("self.data : ", self.data)
        if self.lt:
            self.lt.inorder()
        print(self.data, end=',')
        if self.rt:
            self.rt.inorder()

    def preorder(self):
        print(self.data, end=',')
        if self.lt:
            self.lt.preorder()
        if self.rt:
            self.rt.preorder()

    def postorder(self):
        if self.lt:
            self.lt.postorder()
        if self.rt:
            self.rt.postorder()
        print(self.data, end=',')


# root = Tree(5, lt=3, rt=4)
node1 = Tree(6)
node2 = Tree(7)
node3 = Tree(3, lt=node1)
node4 = Tree(4, rt=node2)
root = Tree(5, lt=node3, rt=node4)
# try:
#     print(root.lt.rt.data)
# except AttributeError:
#     print("Right node does not exist")
#
# if root.rt.lt:
#     print("exists")

print("inorder : ")
root.inorder()
print("\npreorder : ")
root.preorder()
print("\npostorder : ")
root.postorder()
