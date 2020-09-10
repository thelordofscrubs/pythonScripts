import math

def calcDist(loc1,loc2):
    return math.sqrt((loc2.x-loc1.x)**2+(loc2.y-loc1.y)**2)

locations = []

class Location:
    locamt = 0 #total amout of locations, used to increment locid so there are no duplicates
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.location = [x,y]
        self.locid = self.locamt
        self.locamt += 1
        self.connections = []
    def connect(self, newLoc):
        self.connections.append(Connection(self, newLoc))

class Connection:
    conamt = 0 #total amount of connections, used to increment conid so there are no duplicates
    def __init__(self, loc1, loc2):
        self.conid = self.conamt
        self.conamt += 1
        self.loc1 = loc1
        self.loc2 = 0
        self.dist = calcDist(locations[loc1],locations[loc2])

class Request:
    reqamt = 0
    def __init__(self,fro,to,within,pay,weight,space):
        self.fromPlace = fro
        self.toPlace = to
        self.timeLimit = within
        self.pay = pay
        self.loadWeight = weight
        self.loadVolume = space

mapLocations = [Location(0,0),Location(2,5),Location(-2,3),Location(-5,5),Location(1,3),Location(3,-4),Location(0,-2),Location(-2,-3)]
mapLocations[0].connect(mapLocations[2])
mapLocations[0].connect(mapLocations[2])
mapLocations[0].connect(mapLocations[2])
mapLocations[0].connect(mapLocations[2])
mapLocations[0].connect(mapLocations[2])
mapLocations[0].connect(mapLocations[2])