class Square:
    # square instances only get suspectlist if they have unsolved 
    # val - hence optional param
    def __init__(self,index,value,suspectlist=None):
        # member list: index, value, suspect list
        self.index = index # [a,b]
        self.value = value 
        self.suspectlist = suspectlist
        self.t_zone = []

    def __str__(self):
        return str(self.value)

    def setTzone(self,t_zone):
        self.t_zone.append(t_zone) 
        print(t_zone)