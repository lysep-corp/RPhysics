import math
class const:
    pi=3.14159265358979323846
    G = 6.67e-11

class Position2D:
    def __init__(self,x=0,y=0,tuple_=None):
        self.x = x
        self.y = y
        if(tuple_):
            self.x=tuple_[0]
            self.y=tuple_[1]
    def Set(self,x=None,y=None):
        if(x is not None ):self.x=x
        if(y is not None ):self.y=y
        return self
    def Subtract(self,Position):
        self.x-=Position.x
        self.y-=Position.y
        return self
    def Subtract_(self,Position):
        x = self.x
        y = self.y
        x+= Position.x
        y+= Position.y
        return Position2D(x,y)
    def Add(self,Position):
        self.x-=Position.x
        self.y-=Position.y
        return self
    def Add_(self,Position):
        x = self.x
        y = self.y
        x+= Position.x
        y+= Position.y
        return Position2D(x,y)
    def Multiple(self,x=0,y=0):
        if(x):
            self.x*=x
        if(y):
            self.y*=y
        return self
    def Divide(self,x=0,y=0):
        if(x):
            self.x/=x
        if(y):
            self.y/=y
        return self
    def GetTuple(self):
        return (int(self.x),int(self.y))
    def GetDistanceSquare(self,TargetPosition):
        return ((TargetPosition.x-self.x)**2 + (TargetPosition.y-self.y)**2)
    def GetDistance(self,TargetPosition):
        return ((TargetPosition.x-self.x)**2 + (TargetPosition.y-self.y)**2)**0.5
    def GetTargetAngle(self,TargetPosition):
        return math.atan2(
            TargetPosition.y-self.y,
            TargetPosition.x-self.x
            )
class Vector2D:
    def __init__(self,angle=0,value=0):
        self.Angle = angle
        self.Value = value
        self.x = value*math.cos(self.Angle)
        self.y = value*math.sin(self.Angle)
    def GetAngle(self):
        self.Angle = math.atan2(self.y,self.x)
        return self.Angle
    def GetTuple(self):
        return (int(self.x),int(self.y))
    def SetValue(self,value):
        self.Value = value
        self.x = self.Value*math.cos(self.Angle)
        self.y = self.Value*math.sin(self.Angle)
    def SetAngle(self,angle):
        self.Angle = angle
        self.x = self.Value*math.cos(self.Angle)
        self.y = self.Value*math.sin(self.Angle)
    def CalculateVA(self):
        self.Value = math.hypot(self.x,self.y)
        self.Angle = math.atan2(self.y,self.x)
    def SplitVectorSet(self,value,angle):
        self.x= value*math.cos(angle)
        self.y= value*math.sin(angle)
        self.CalculateVA()
    def SplitVectorAdd(self,value,angle):
        self.x+= value*math.cos(angle)
        self.y+= value*math.sin(angle)
        self.CalculateVA()
    def SplitVectorSub(self,value,angle):
        self.x-= value*math.cos(angle)
        self.y-= value*math.sin(angle)
        self.CalculateVA()
    def Add_(self,x=0,y=0):
        self.x+=x
        self.y+=y
        self.CalculateVA()
        return self
    def Add(self,vector):
        self.x+=vector.x
        self.y+=vector.y
        self.CalculateVA()
        return self
    def Substract(self,vector):
        self.x-=vector.x
        self.y-=vector.y
        self.CalculateVA()
        return self
    def Substract_(self,x=0,y=0):
        self.x-=x
        self.y-=y
        self.CalculateVA()
        return self
    def Multiply_(self,x=0,y=0):
        self.x*=x
        self.y*=y
        self.CalculateVA()
        return self
    def Multiply(self,vector):
        self.x*=vector.x
        self.y*=vector.y
        self.CalculateVA()
        return self
    def Divide_(self,x=0,y=0):
        self.x/=x
        self.y/=y
        self.CalculateVA()
        return self
    def Divide(self,vector):
        self.x/=vector.x
        self.y/=vector.y
        self.CalculateVA()
        return self
class Color:
    def __init__(self,r=0,g=0,b=0):
        self.Red = r
        self.Green = g
        self.Blue = b
    def GetTuple(self):
        return (self.Red,self.Green,self.Blue)
    def setHex(self,value):
        rgb = self.hexToRGB(value)
        self.Red = rgb[0]
        self.Green = rgb[1]
        self.Blue = rgb[2]
        return self
    def hexToRGB(self,value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
