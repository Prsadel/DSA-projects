from node import Node
from object import Color
def comp_1(node_1, node_2):
    pass

class AVLTree:
    def __init__(self, compare_function=comp_1):
        self.root = None
        self.size = 0
        self.comparator = compare_function

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def insert(self, root, value,id):
        if not root:
            n=Node()
            n.value=value
            n.id=AVLTree()
            n.id.insert_valuex(id)
            return n
        elif value==root.value:

            root.id.insert_valuex(id)
            return root
        elif value < root.value:
            root.left = self.insert(root.left, value,id)
        
        else:
            root.right = self.insert(root.right, value,id)

        

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    def insert2(self, root, value,lis):
        if not root:
            n=Node()
            n.value=value
            n.id=lis[0]
            n.size=lis[1]
            n.color=lis[2]
            n.obj.object_id=value
            n.obj.size=lis[1]
            n.obj.color=lis[2]
            return n
        elif value < root.value:
            root.left = self.insert2(root.left, value,lis)
        else:
            root.right = self.insert2(root.right, value,lis)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    
    def insert1(self, root,value,capacity):
        if not root:
            n=Node()
            n.value=value
            n.capacity=capacity
            n.bin.rem_capacity=capacity
            n.bin.binid=value
            
            return n
        elif value < root.value:
            root.left = self.insert1(root.left, value,capacity)
        else:
            root.right = self.insert1(root.right, value,capacity)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    def insertx(self, root,value):
        if not root:
            n=Node()
            n.value=value
            return n
        elif value < root.value:
            root.left = self.insertx(root.left, value)
        else:
            root.right = self.insertx(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    def insert4(self, root,value,object):
        if not root:
            n=Node()
            n.value=value
            n.id=object
            
            return n
        elif value < root.value:
            root.left = self.insert4(root.left, value,object)
        else:
            root.right = self.insert4(root.right, value,object)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    


    def delete(self, root, value,binid):
        if not root:
            return root

        if value < root.value:
            root.left = self.delete(root.left, value,binid)
        elif value > root.value:
            root.right = self.delete(root.right, value,binid)

        elif value==root.value and binid!=root.id:
            root.right=self.delete(root.right,value,binid)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value,binid)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    
    def delete1(self, root, value):
        if not root:
            return root
        if value < root.value:
            root.left = self.delete1(root.left, value)
        elif value > root.value:
            root.right = self.delete1(root.right, value)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.id = temp.id
            root.bin=temp.bin
            root.obj=temp.obj
            
            root.right = self.delete1(root.right, temp.value)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y
    def min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current
    def minse_value_node(self):
        current =self.root
        while current.left:
            current = current.left
        return current
    def maxse_value_node(self):
        current=self.root
        while current.right:
            current=current.right
        return current

    def search(self, root, value):
        if not root or root.value == value:
            return root
        if root.value < value:
            return self.search(root.right, value)
        return self.search(root.left, value)
    
    def search_green(self,size):
        best_node=None
        root=self.root

        while root:
            if root.value>=size:
                if best_node==None:
                    best_node=root
            
                if root.value>=best_node.value:
                    best_node=root
                    
            root=root.right

        return best_node
    def search_red(self,size):
        # print("red")
        best_node=None
        root=self.root

        while root:
            if root.value>=size:
                if best_node==None:
                    best_node=root
            
                if best_node.value<=root.value:
                    best_node=root
            root=root.right

        return best_node
    def search_yellow(self,size):
        best_node=None
        root=self.root
        while root:
            if root.value==size:
                return root

            elif root.value>size:
                if best_node==None:
                    best_node=root
            
                if best_node.value>=root.value:
                    best_node=root
                
                root=root.left
            
            else:
                root=root.right
        return best_node
    
    def search_blue(self,size):
        best_node=None
        root=self.root
        while root:
            if root.value==size:
                return root

            elif root.value>size:
                if best_node==None:
                    best_node=root
            
                if best_node.value>=root.value:
                    best_node=root
                
                root=root.left
            
            else:
                root=root.right
        return best_node
    
    

    def insert_value(self, value,id):
        self.root = self.insert(self.root, value,id)
    
    def insert_value1(self,id,capacity):
        self.root = self.insert1(self.root,id,capacity)

    def insert_value2(self,id,lis):
        self.root=self.insert2(self.root,id,lis)
    
    def insert_valuex(self,id):
        self.root=self.insertx(self.root,id)

    def insert_value4(self, value,id):
        self.root = self.insert4(self.root, value,id)
    
    def delete12(self, root, value):
        if not root:
            return root

        if value < root.value:
            root.left = self.delete12(root.left, value)
        elif value > root.value:
            root.right = self.delete12(root.right, value)
        else:
            # Node to be deleted found
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

        # Get the in-order successor (smallest in the right subtree)
            temp = self.min_value_node(root.right)

        # Copy the value and id AVL tree from successor to root
            root.value = temp.value
            root.id = temp.id  # Update root's id AVL tree with successor's id AVL tree

        # Delete the in-order successor
            root.right = self.delete12(root.right, temp.value)

        # Update height of the current node
        root.height = 1 + max(self.height(root.left), self.height(root.right))

        # Balance the tree
        balance = self.balance(root)

        # Left-Left Case
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left-Right Case
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Right Case
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # Right-Left Case
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    

    def deletebin(self, value,binid):
        # self.root = self.delete(self.root, value,binid)
        a=self.search_value(value)
        # print(a.id.root.height)
        if a.id.root.height<=1:
            # a.id.root=None
            self.delete_value12(value)
        else:
            b=a.id
            b.delete_value12(binid)
            a.id=b

    def delete_value12(self, value):
        self.root = self.delete12(self.root, value)
        
    def delete_value1(self, value):
        self.root = self.delete1(self.root, value)

    def search_value(self, value):
        return self.search(self.root, value)
    
    def search_bin_idco(self,size,color):
        print(color)
        # if color==Color.RED:
        #     return self.search_blue(size)
        # elif color==2:
        #     return self.search_yellow(size)
        # elif color==3:
        #     return self.search_red(size)
        # elif color==4:
        #     return self.search_green(size)
    
    def inorder_trav(self,node):
        if not node:
            return []
        lefty=self.inorder_trav(node.left)
        righty=self.inorder_trav(node.right)
        # node.id.inorder_trav(node.id.root)
        return (lefty+[[node.value,node.id]]+righty)

    
    

    
