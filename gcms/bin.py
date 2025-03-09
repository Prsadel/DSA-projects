# from avl import AVLTree\
from object import Object
class Bin:
    def __init__(self, bin_id, capacity):
        self.binid=bin_id
        self.rem_capacity=capacity
        from avl import AVLTree
        self.obj_stori=AVLTree()
        pass

    def add_object(self, object):
        # Implement logic to add an object to this bin
        self.obj_stori.insert_value4(object.object_id,object)
        self.rem_capacity=self.rem_capacity-object.size
        pass

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        obj_torem=self.obj_stori.search_value(object_id)
        self.rem_capacity=self.rem_capacity+obj_torem.id.size
        # implement the deletion here 
        self.obj_stori.delete_value1(object_id)
        pass

    def inorder_trav(self,node):
        if not node:
            return []
        lefty=self.inorder_trav(node.left)
        righty=self.inorder_trav(node.right)

        return (lefty+[node.value]+righty)
    
    def list_obj(self):
        return self.inorder_trav(self.obj_stori.root)
    