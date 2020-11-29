class Square:
    def __init__(self,index,value,suspectlist=None):
        # member list: index, value, suspect list
        self.index = index # [a,b]
        self.value = value 
        self.suspectlist = suspectlist

    def __str__(self):
        return str(self.value)