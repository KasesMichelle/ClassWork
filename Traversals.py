class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.value)
        if self.right:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        print(self.value)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.value)

    def find(self, key):
        if key < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(key)
        elif key > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(key)
        else:
            return True


if __name__ == '__main__':
    trav = TreeNode('M')
    trav.insert('C')
    trav.insert('R')
    trav.insert('A')
    trav.insert('D')

    print("Inorder:")
    trav.in_order_traversal()

    print("Preorder:")
    trav.pre_order_traversal()

    print("Postorder:")
    trav.post_order_traversal()

    print("Find D:", trav.find('D'))  # True
    print("Find Z:", trav.find('Z'))  # False

             