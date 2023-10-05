class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def insert_value(self, key):
        self.root = self.insert(self.root, key)

    def delete(self, root, key):
        if not root:
            return root
        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            root.val = self.min_value(root.right)
            root.right = self.delete(root.right, root.val)
        return root

    def delete_value(self, key):
        self.root = self.delete(self.root, key)

    def search(self, root, key):
        if not root or root.val == key:
            return root
        if key < root.val:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def find_min(self, root):
        current = root
        while current.left:
            current = current.left
        return current.val

    def find_max(self, root):
        current = root
        while current.right:
            current = current.right
        return current.val

    def find_successor(self, root):
        if root.right:
            return self.find_min(root.right)
        successor = None
        current = self.root
        while current:
            if root.val < current.val:
                successor = current
                current = current.left
            elif root.val > current.val:
                current = current.right
            else:
                break
        return successor.val if successor else None

    def find_predecessor(self, root, key):
        if not root:
            return None
        if key < root.val:
            return self.find_predecessor(root.left, key)
        elif key > root.val:
            return root.val if self.find_predecessor(root.right, key) is None else self.find_predecessor(root.right, key)
        else:
            if root.left:
                return self.find_max(root.left)
            else:
                return None

    def find_min_value(self):
        return self.find_min(self.root)

    def find_max_value(self):
        return self.find_max(self.root)

    def find_successor_of_root(self):
        if not self.root:
            return None
        return self.find_successor(self.root)

    def find_predecessor_of_node(self, key):
        node = self.search(self.root, key)
        if not node:
            return None
        return self.find_predecessor(self.root, key)


# Example usage:
bst = BST()
bst.insert_value(50)
bst.insert_value(30)
bst.insert_value(70)
bst.insert_value(20)
bst.insert_value(40)
bst.insert_value(60)
bst.insert_value(80)

print("Minimum value in the BST:", bst.find_min_value())  # Output: 20
print("Maximum value in the BST:", bst.find_max_value())  # Output: 80
print("Successor of root:", bst.find_successor_of_root())  # Output: 60
print("Predecessor of node with value 40:", bst.find_predecessor_of_node(40))  # Output: 30

bst.delete_value(30)
print("Deleted node with value 30.")
print("Predecessor of node with value 40:", bst.find_predecessor_of_node(40))  # Output: 20
