'''
Python Code to implement a heap with general comparison function
'''

class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        
        # Write your code here
        self.arr=[0]+init_array
        self.cfnc=comparison_function
        # if len(init_array)==0:
        #     self.arr=[0]
        self.cursize=len(init_array)
        for i in range(self.cursize // 2, 0, -1): 
            self.percDown(i)
        self.current_time=0

        pass
        
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        self.arr.append(value)
        self.cursize=self.cursize+1
        self.percup(self.cursize)
        
        # Write your code here
        pass
    def percup(self,i):
        while i // 2 > 0:
            if self.cfnc(self.arr[i],self.arr[i // 2]):
                tmp = self.arr[i // 2]
                self.arr[i // 2] = self.arr[i]
                self.arr[i] = tmp
            i = i // 2
    def percDown(self,i):
         while (i * 2) <= self.cursize:
            mc = self.mint(i)
            if self.cfnc(self.arr[mc],self.arr[i]):
                tmp = self.arr[i]
                self.arr[i] = self.arr[mc]
                self.arr[mc] = tmp
            i = mc
      
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        retval = self.arr[1]
        self.arr[1] = self.arr[self.cursize]
        self.arr.pop()
        self.cursize=self.cursize-1
        self.percDown(1)
        return retval
        # Write your code here
        pass
    def mint(self,i):
        if i*2+1>self.cursize:
            return i*2
        else:
            if self.cfnc(self.arr[i*2],self.arr[i*2+1]):
                return i*2
            else:
                return i*2+1
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        return self.arr[1]
        
        # Write your code here
        pass
    def getal(self):
        return (self.arr)
    
    def parent(self, i): 
        return (i-1)/2
    # You can add more functions if you want to

    def comp(self,a,b):
        proa=(self.current_time-a.arrival_time)-(a.size-a.processed)
        prob=(self.current_time-b.arrival_time)-(b.size-b.processed)
        if proa<prob:
            return False
        elif proa>prob:
            return True
        else:
            # print("proa",proa,"prob",prob,a.id,b.id,a.id<b.id)
            if a.id<b.id:
                return True
            else :
                return False

        pass

    def insert1(self, value):
        self.arr.append(value)
        self.cursize=self.cursize+1
        self.percup1(self.cursize)
        
        # Write your code here
        pass
    def percup1(self,i):
        while i // 2 > 0:
            if self.comp(self.arr[i],self.arr[i // 2]):
                tmp = self.arr[i // 2]
                self.arr[i // 2] = self.arr[i]
                self.arr[i] = tmp
            i = i // 2
    def percDown1(self,i):
         while (i * 2) <= self.cursize:
            mc = self.mint1(i)
            if self.comp(self.arr[mc],self.arr[i]):
                tmp = self.arr[i]
                self.arr[i] = self.arr[mc]
                self.arr[mc] = tmp
            i = mc
      
    def extract1(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        retval = self.arr[1]
        self.arr[1] = self.arr[self.cursize]
        self.arr.pop()
        self.cursize=self.cursize-1
        self.percDown1(1)
        return retval
        # Write your code here
        pass
    def mint1(self,i):
        if i*2+1>self.cursize:
            return i*2
        else:
            if self.comp(self.arr[i*2],self.arr[i*2+1]):
                return i*2
            else:
                return i*2+1