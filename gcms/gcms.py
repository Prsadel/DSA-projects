from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.tree_imp=AVLTree()
        self.binid=AVLTree()
        self.objid=AVLTree()
        # self.tpim=AVLTree()
        pass 

    def add_bin(self, bin_id, capacity):
        self.tree_imp.insert_value(capacity,bin_id)
        self.binid.insert_value1(bin_id,capacity)
        pass

    def add_object(self, object_id, size, color):
        binin=None
        if color==Color.BLUE:
            binin=self.tree_imp.search_blue(size)
        elif color==Color.YELLOW:
            binin=self.tree_imp.search_yellow(size)
        elif color==Color.RED:
            # print("redused")
            binin=self.tree_imp.search_red(size)
        elif color==Color.GREEN:
            binin=self.tree_imp.search_green(size)
        if binin==None:
            # print("aal")
            raise NoBinFoundException
        bininid=0
        if color==Color.BLUE:
            bininid=binin.id.minse_value_node()
        elif color==Color.YELLOW:
            bininid=binin.id.maxse_value_node()
        elif color==Color.RED:
            bininid=binin.id.minse_value_node()
        elif color==Color.GREEN:
            bininid=binin.id.maxse_value_node()
            
        # print("putein",binin.value,bininid.value,object_id,"->",binin.value-size)
        # self.tree_imp.deletebin(binin.value,bininid.value)
        # # if binin.value-size>=0:
        # self.tree_imp.insert_value((binin.value-size),bininid.value)
        a=binin.value
        b=bininid.value
        # print(object_id,b,a,"->",size)
        # self.tpim.insert_value4(object_id,b)
        lis=[bininid.value,size,color]
        self.objid.insert_value2(object_id,lis)
        # print("putein",binin.value,bininid.value,object_id,"->",binin.value-size)
        
        bininmod=self.binid.search_value(bininid.value)
        # print(bininmod.bin.rem_capacity)
        objinmod=self.objid.search_value(object_id)
        bininmod.capacity=bininmod.capacity-size
        bininmod.bin.add_object(objinmod.obj)
        # print(bininmod.bin.rem_capacity,"->",a-size)

        # self.tree_imp.deletebin(binin.value,bininid.value)
        # # if binin.value-size>=0:
        # self.tree_imp.insert_value((bininmod.bin.rem_capacity),bininid.value)
        self.tree_imp.deletebin(a,b)
        # print("be",self.tree_imp.inorder_trav(self.tree_imp.root))
        self.tree_imp.insert_value(a-size,b)
        # print("af",self.tree_imp.inorder_trav(self.tree_imp.root))
    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin\


        objimond=self.objid.search_value(object_id)
        binidn=objimond.id
        binid_sizere=objimond.size
        # print(binid_sizere)
        # self.objid.delete_value1(object_id)

        binimond=self.binid.search_value(binidn)
        # print(self.objid.inorder_trav(self.objid.root))
        # print(binidn,binimond.value)
        binid_sizeit=binimond.bin.rem_capacity
        # print(binimond.capacity,binid_sizeit)
        # print(self.bin_info(binimond.value))
        binimond.bin.remove_object(object_id)
        self.objid.delete_value1(object_id)
        self.tree_imp.deletebin(binimond.capacity,binidn)
        binimond.capacity=binimond.capacity+binid_sizere
        self.tree_imp.insert_value((binid_sizere+binid_sizeit),binidn)
        # print(self.objid.inorder_trav(self.objid.root))

        pass

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        # print("call")
        binimond=self.binid.search_value(bin_id)
        a=binimond.bin.list_obj()
        return (binimond.bin.rem_capacity,a)

        pass

    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        objimond=self.objid.search_value(object_id)
        if objimond==None:
            return 0
        return objimond.id
        pass
    
