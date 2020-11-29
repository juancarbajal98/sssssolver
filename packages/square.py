class Square:
    # square instances only get suspectlist if they have unsolved 
    # val - hence optional param
    def __init__(self,index,value,suspectlist=None):
        # member list: index, value, suspect list
        self.index = index # [a,b]
        self.value = value 
        self.suspectlist = suspectlist
        # {[rowdata],[columndata],[boxdata]}
        self.t_zone = []

    def __str__(self):
        return str(self.value)

    def setTzone(self,t_zone):
        # enumerate thru param - feed into data field t zone
        for i in range(len(t_zone)):
            self.t_zone.append(t_zone[i]) 

    def trimSuspect(self,val):
        self.suspectlist.remove(val)
        print('self.suspectlist:', self.suspectlist)
        print('coords:',self.index)
        if (len(self.suspectlist) == 1):
            self.value = self.suspectlist[0]
            self.suspectlist = None
            # update t_zone suspects 
    
    def stripTzone(self):
        # intilize a null list 
        unique_list = [] 
      
        # traverse for all elements 
        for x in self.t_zone: 
            # check if exists in unique_list or not 
            if x not in unique_list: 
                unique_list.append(x) 
        return unique_list