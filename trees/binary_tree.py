class node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class tree:
    
    def __init__(self, data):        
        self.root = node(data)
        

    def get_root(self, node):
        root = node
        if root is None:
            root = self.root
        return root
    

    def has_two_children(self, node):
        return node.left is not None and node.right is not None


    def has_children(self, node):
        return node.left is not None or node.right is not None
    
        
    def add_node(self, data, parent = None):
        root = self.get_root(parent)
        if root.data == data:
            return
        if root.data > data:
            if root.left is None:
                root.left = node(data)
            else:
                self.add_node(data, root.left)
        else:
            if root.right is None:
                root.right = node(data)
            else:
                self.add_node(data, root.right)
                

    def search_oldest_son(self, node):
        if node.left is not None and node.right is not None:
            return node.right
        elif node.left is None and node.right is not None:
            return node.right
        else:
            return node.left
        

    def delete_node(self, data, leaf = None,  parent = None):
        root = self.get_root(leaf)
        if root.data == data:
            if self.has_two_children(root):
               self.delete_node_two_children(root)
            else:
                finded = self.search_oldest_son(root)
                if parent.left is root:
                    parent.left = finded
                else:
                    parent.right = finded
            return 

        if root.data > data and root.left is not None:
            finded = self.delete_node(data, root.left, root)
        elif root.right is not None:
            finded = self.delete_node(data, root.right, root)

    def delete_node_two_children(self, root):
        finded = self.search_youngest_successor(root.right)
        self.delete_node(finded.data)
        root.data = finded.data
            
    
    def show_tree(self, node = None):
        root = self.get_root(node)
        print(root.data)
        if root.left is not None: 
            self.show_tree(root.left)
        if root.right is not None:
            self.show_tree(root.right)
            

    def show_tree_inorder(self, node = None):
        root = self.get_root(node)
        if root.left is not None: 
            self.show_tree_inorder(root.left)
        print(root.data)
        if root.right is not None:
            self.show_tree_inorder(root.right)
 

    def search_element(self, data, node = None):
        finded = None
        root = self.get_root(node)   
        if root.data == data:
            return root
        if root.data >= data and root.left is not None: 
            finded = self.search_element(data, root.left)
        elif root.right is not None:
            finded = self.search_element(data, root.right)
        return finded


    def search_youngest_successor(self, root = None):
        finded = root
        if root.left is not None: 
            return self.search_youngest_successor(root.left)
        return finded
        


binary_tree = tree(10)
binary_tree.add_node(36)
binary_tree.add_node(30)
binary_tree.add_node(4)
binary_tree.add_node(3)
binary_tree.add_node(1)
binary_tree.add_node(6)
binary_tree.add_node(37)
binary_tree.add_node(35)
binary_tree.add_node(10)
binary_tree.add_node(2)
binary_tree.add_node(5)
binary_tree.add_node(34)
binary_tree.add_node(8)
binary_tree.add_node(7)
binary_tree.add_node(1)
binary_tree.show_tree()
binary_tree.delete_node(36)
binary_tree.delete_node(6)
binary_tree.delete_node(30)
#print(binary_tree.delete_node_2(30))
#print(binary_tree.delete_node(10))
print('after delete nodes')
#binary_tree.show_tree()


tree = tree(10)
tree.add_node(15)
tree.add_node(6)
tree.add_node(8)
tree.add_node(5)
tree.add_node(13)
tree.add_node(16)
tree.add_node(9)
tree.add_node(4)
tree.add_node(7)
tree.add_node(3)
tree.add_node(2)
tree.add_node(18)
tree.add_node(20)
tree.add_node(22)
tree.add_node(12)
tree.add_node(11)
tree.delete_node(10)
tree.delete_node(15)
tree.delete_node(8)
tree.delete_node(4)
tree.delete_node(2)
tree.delete_node(18)
tree.delete_node(11)
tree.delete_node(16)
tree.show_tree()
print('in order')
print('-------------')
tree.show_tree_inorder()
