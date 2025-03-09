from bin import Bin
# from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException

class Node:
    def __init__(self):
        self.value =0
        self.left = None
        self.right = None
        self.height = 1
        self.id=0 
        # this id is bin_id for 1st and ||  object class for avl tree in the Bin || and bin_id for 3rd   


        # bin class
        self.capacity=0

        # object class
        self.size=0
        self.color=-1
        # if self.capacity!=0:
        self.bin=Bin(self.value,self.capacity)
        # if self.color!=-1:
        self.obj=Object(self.value,self.size,self.color)


        pass