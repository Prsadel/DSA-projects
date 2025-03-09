'''
    This file contains the class definition for the StrawHat class.
'''

import crewmate
from heap import *
import treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        li=[]
        c=0
        for i in range(0,m):
            li.append([c,[]])
        self.cret=Heap(comp1f,li)
        self.cret.cursize=m
        # Write your code here
        pass
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        # print(self.cret.cursize)
        temp=self.cret.extract()
        b=temp[0]
        temp[1].append(treasure)
        if temp[0]>treasure.arrival_time:
            temp[0]=temp[0]+treasure.size
            self.cret.insert(temp)
        else:
            temp[0]=treasure.arrival_time+treasure.size
            self.cret.insert(temp)
        # print(self.cret.cursize)

        
        # Write your code here
        pass
    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        a=self.cret.getal()
        # print(len(a))
        # for i in a:
        #     print(i[0],"(",len(i[1]),")",end=" ")
        # print()
        x=[]
        tot_tres=0
        for i in a[1:]:
            if i[0]==0:
                continue
            else:
                tot_tres=tot_tres+len(i[1])
                # print(len(i[1]))
                x=x+self.solve(i[1])
        x.sort(key=colist)
        if len(x)!=tot_tres:
            print("aalo")
        return x
        # Write your code here
        pass
    
    # You can add more methods if required
        

    def solve(self,li):
        b=Heap(co,[])
        # for i in li:
        #     print(i.id,end=" ")
        # print()
        b.cursize=0
        li[0].processed=0
        b.insert1(li[0])
        b.current_time=max(li[0].arrival_time,b.current_time)
        y=[]
        alpha=0
        beta=0
        for i in range(1,len(li)):
            a=li[i]
            a.processed=0
            while(b.cursize!=0 and b.current_time!=a.arrival_time):
                temp=b.top()
                if (b.current_time+(temp.size-temp.processed))>=a.arrival_time:
                    temp1=b.extract1()
                    temp1.processed=temp1.processed+a.arrival_time-b.current_time
                    b.current_time=a.arrival_time
                    b.insert1(temp1)
                    b.insert1(a)
                    break
                else :
                    b.current_time=b.current_time+(temp.size-temp.processed)
                    temp1=b.extract1()
                    temp1.completion_time=b.current_time
                    temp1.processed=temp1.size
                    y.append(temp1)
            if b.cursize==0:
                b.current_time=a.arrival_time
                b.insert1(a)
        # print(len(y),b.cursize)
        # if b.cursize>1 and li[0].id==1001:
        #     print(b.comp(li[0],li[1]))
        #     a=li[0]
        #     c=li[1]
        #     print(a.arrival_time,a.size,a.processed,b.current_time)
        #     print(c.arrival_time,c.size,c.processed,b.current_time)
        #     proa=(a.arrival_time-b.current_time)-(a.size-a.processed)
        #     prob=(c.arrival_time-b.current_time)-(c.size-c.processed)
        #     print(proa,prob)




        while(b.cursize!=0):
            temp=b.top()
            b.current_time=b.current_time+(temp.size-temp.processed)
            temp1=b.extract1()
            temp1.completion_time=b.current_time
            temp1.processed=temp1.size
            y.append(temp1)
        # if len(li)==1:
        #     b.current_time=b.current_time+li[0].size
        #     li[0].processed=li[0].size
        #     li[0].completion_time=b.current_time
        #     y.append(li[0])
        # print(len(y))
        return y
        
        pass
def comp1f(a,b):
    if a[0]<b[0]:
        return True
    else:
        return False
def co(a,b):

    pass
def colist(obj:treasure.Treasure):
    return obj.id
        

 
    