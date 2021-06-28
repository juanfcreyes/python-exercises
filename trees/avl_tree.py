import copy

class Node:
    
    def __init__(self, data, height = None, parent = None):
        self.left: Node = None
        self.right: Node = None
        self.parent: Node = parent
        self.height = height
        self.data = data


class AVLTree:
    
    def __init__(self, data = None):
        if data is not None:
            self.root = Node(data)   
        else:
            self.root = None
        self.actual_node = self.root


    def get_root(self, node = None):
        root = node
        if node is None:
            root = self.root
        return root


    def is_empty(self, node = None):
        return node is None


    def is_menber(self, data, node = None):
        if self.is_empty(node):
            return False
        root = self.get_root(node)
        if root.data == data:
            return True
        if root.data > data:
            return self.is_menber(data, root.left)
        else:
            return self.is_menber(data, root.right)


    def is_root(self, data):
        if self.is_empty(self.root):
            return False
        return self.root.data == data
    

    def is_leaf(self, data, node = None):
        root = self.get_root(node)
        return not self.is_empty(root) and root.left is None and root.right is None


    def show_tree(self, node = None):
        root = self.get_root(node)
        if root.left is not None:
            self.show_tree(root.left)
        print(root.data)
        if root.right is not None:
            self.show_tree(root.right)
            

    def show_tree_postorder(self, node = None):
        root = self.get_root(node)
        if root.left is not None:
            self.show_tree_postorder(root.left)
        if root.right is not None:
            self.show_tree_postorder(root.right)
        print(root.data)
        

    def show_tree_preorder(self, node = None):
        root = self.get_root(node)
        print(root.data, root.parent.data if root.parent is not None else -1, root.height, self.calc_balance(root))
        if root.left is not None:
            self.show_tree_preorder(root.left)
        if root.right is not None:
            self.show_tree_preorder(root.right)


    def search_node(self, data, node = None):
        if self.is_empty(node):
            return None
        
        if node.data == data:
            return node
        
        if node.data > data:
            return self.search_node(data, node.left)
        else:
            return self.search_node(data, node.right)


    def add_leaf(self, data, node: Node = None, parent: Node = None):
        if self.is_empty(self.root):
            self.root = Node(data, 0)
            self.actual_node = self.root
            return

        if parent is None:
            self.actual_node = self.root
        else:
            self.actual_node = node

        if self.actual_node is not None:
            if self.actual_node.data > data:
                self.add_leaf(data, self.actual_node.left, self.actual_node)
            elif self.actual_node.data < data: 
                self.add_leaf(data, self.actual_node.right, self.actual_node)
            else:
                return
        else:
            new_node = self.link_node(data, parent)
            self.balance_tree(parent)


    def has_children(self, node):
        return node.left is not None or node.right is not None
    

    def has_both_children(self, node):
        return node.left is not None and node.right is not None


    def get_oldest_child(self, node):
        return node.right if node.right is not None else node.left


    def search_youngest_successor(self, root = None):
        finded = root
        if root.left is not None: 
            return self.search_youngest_successor(root.left)
        return finded


    def remove_node(self, data, root = None):
        node = self.search_node(data, self.get_root(root))
        if node is None:
            return
        
        pivot = self.get_oldest_child(node)
        if not self.has_both_children(node):
            if node.parent.left is node:
                node.parent.left = pivot
            else:
                node.parent.right = pivot
            node.left = None
            node.right = None
        else:
            pivot = self.search_youngest_successor(node.right)
            self.remove_node(pivot.data, pivot)
            node.data = pivot.data
            return

        if pivot is not None:
            pivot.parent = node.parent

        self.re_calc_height(self.root, 0)
        self.balance_tree(node)
        node.parent = None
        
        
    def balance_tree(self, node):
        if node is None:
            return 

        ancestor = node.parent
        balance = 0

        if ancestor is not None:
            balance = self.calc_balance(ancestor)
            
        node_balance = 0
        """Rotation algorithms base on
            https://en.wikipedia.org/wiki/Tree_rotation#/media/File:Tree_Rebalancing.gif"""
        if  balance <= -2:
            node_balance = self.calc_balance(node)          
            if node_balance <= 0:
                self.left_rotation(ancestor)
            else:
                self.doble_left_rotation(ancestor.left)
        if balance >= 2:
            node_balance = self.calc_balance(node)
            if node_balance >= 0:
                self.right_rotation(ancestor)
            else:
                self.doble_right_rotation(ancestor.right)
        self.balance_tree(ancestor)
            

    def re_calc_height(self, node, height):
        if node is not None:
            node.height = height
            self.re_calc_height(node.left, height + 1)
            self.re_calc_height(node.right, height + 1)


    def link_node(self, data, parent):
        new_node = Node(data, parent.height + 1, parent)
        if parent.data > data:
            parent.left = new_node
        else:
            parent.right = new_node
        return new_node
    

    def rotate_root_right(self, root: Node):
        pivot = root.right        
        root.right = pivot.left

        if pivot.left is not None:
            pivot.left.parent = root
        
        pivot.left = root
        pivot.parent = root.parent
        root.parent = pivot
        return pivot


    def rotate_root_left(self, root: Node):
        pivot = root.left
        root.left = pivot.right

        if pivot.right is not None:
            pivot.right.parent = root
        
        pivot.right = root
        pivot.parent = root.parent
        root.parent = pivot    
        return pivot
    

    def determinate_root_or_child(self, root, pivot):
        if self.root is root: 
            self.root = pivot
        else:
            if root is pivot.parent.left:
                pivot.parent.left = pivot
            else:
                pivot.parent.right = pivot
                

    def left_rotation(self, root: Node):
        pivot = self.rotate_root_left(root)
        self.determinate_root_or_child(root, pivot)
        self.re_calc_height(self.root, 0)


    def right_rotation(self, root: Node):
        pivot = self.rotate_root_right(root)
        self.determinate_root_or_child(root, pivot)
        self.re_calc_height(self.root, 0)

    
    def doble_left_rotation(self, root: Node):
        pivot = self.rotate_root_right(root)
        self.determinate_root_or_child(root, pivot)
        self.left_rotation(pivot.parent)


    def doble_right_rotation(self, root: Node):
        pivot = self.rotate_root_left(root)
        self.determinate_root_or_child(root, pivot)
        self.right_rotation(pivot.parent)
           

    def calc_balance(self, node):
        height_left = self.calc_tree_height(node.left, 0)
        height_right = self.calc_tree_height(node.right, 0)
        return height_right - height_left
    

    def calc_tree_height(self, node, height):
        if self.is_empty(node):
            return -1
        left = self.calc_tree_height(node.left, height + 1)
        right = self.calc_tree_height(node.right, height + 1)  
        return max(height, max(left, right))
    

tree3 = AVLTree()
tree3.add_leaf(9)
tree3.add_leaf(10)
tree3.add_leaf(5)
tree3.add_leaf(2)
tree3.add_leaf(7)
tree3.add_leaf(6)
tree3.add_leaf(8)
tree3.add_leaf(1)
tree3.add_leaf(0)
tree3.add_leaf(13)
tree3.add_leaf(11)
tree3.add_leaf(3)
tree3.add_leaf(12)
tree3.add_leaf(17)
tree3.add_leaf(4)
tree3.add_leaf(14)
tree3.add_leaf(15)
tree3.add_leaf(16)
tree3.add_leaf(20)
tree3.add_leaf(21)
tree3.add_leaf(18)
tree3.add_leaf(19)
tree3.add_leaf(23)
tree3.add_leaf(22)
tree3.add_leaf(26)
tree3.add_leaf(35)
tree3.add_leaf(28)
tree3.add_leaf(30)
tree3.add_leaf(32)
tree3.add_leaf(27)
tree3.add_leaf(24)
tree3.add_leaf(25)
tree3.add_leaf(27)
tree3.add_leaf(31)
tree3.add_leaf(32)
tree3.add_leaf(33)
tree3.add_leaf(34)
tree3.add_leaf(36)
tree3.add_leaf(40)
tree3.add_leaf(37)
tree3.add_leaf(39)
tree3.add_leaf(38)
tree3.remove_node(22)
tree3.remove_node(17)
tree3.remove_node(15)
tree3.remove_node(4)
tree3.remove_node(40)
tree3.remove_node(35)
tree3.show_tree_preorder()

print("Node root ")
tree = AVLTree()
tree.add_leaf(10)
tree.add_leaf(15)
tree.add_leaf(6)
tree.add_leaf(8)
tree.add_leaf(5)
tree.add_leaf(13)
tree.add_leaf(16)
tree.add_leaf(9)
tree.add_leaf(4)
tree.add_leaf(7)
tree.add_leaf(3)
tree.add_leaf(2)
tree.add_leaf(18)
tree.add_leaf(20)
tree.add_leaf(22)
tree.remove_node(10)
tree.remove_node(6)
tree.remove_node(18)
tree.remove_node(4)
tree.remove_node(13)
print("-------------")
tree.show_tree_preorder()
