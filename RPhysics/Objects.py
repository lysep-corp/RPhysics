from RPhysics.MathObjects import *
from RPhysics.Physics import *
from pygame import Surface
from pygame.draw import circle
class Rectangle:
    def __init__(self,width=0,height=0,pos=Position2D()):
        self.width=width
        self.height=height
        self.pos=pos
    def GetCenter_t(self):
        return (self.width//2,self.height//2)
    def GetCenter_p(self):
        return Position2D(self.width/2,self.height/2)
    def t(self):
        return (self.width,self.height)
class Object:
    def __init__(self,pos=Position2D(0,0),color=Color(255,255,255),vector = Vector2D(0,0),volume=1,density=1):
        self.Pos = pos
        self.Color = Color(255,255,255)
        self.Vector = vector
        self.Volume = volume
        self.Density = density
    def _(self,obj):
        NewtonianGravity(self,obj)
        self.Collide(obj)
        self.__()
    def GetMass(self):
        return self.Volume*self.Density
    def Collide(self,obj):
        pass
    def GetRadius(self):
        return self.Volume
    def GetRadiusi(self):
        return int(self.Volume)
    def __(self):
        self.Pos.x+=self.Vector.x
        self.Pos.y+=self.Vector.y
class Circle(Object):
    def Draw(self,screen:Surface):
        circle(screen,self.Color.GetTuple(),self.Pos.GetTuple(),self.GetRadiusi())
    def DrawRelative(self,screen:Surface,camera:Position2D,zoom:float):
        A = self.Pos.Subtract_(camera).GetTuple()
        B = (screen.get_width(),screen.get_height()) 
        r = self.GetRadius()
        if(B[0]+r >= A[0] and B[1]+r >= B[1] and B[0] >= 0 and B[1] >= 0):
            circle(screen,self.Color.GetTuple(),A,self.GetRadiusi()*int(zoom))
    def Collide(self,obj:Object):
        d = self.Pos.GetDistance(obj.Pos)
        d_clear = d-(self.GetRadius()+obj.GetRadius())
        if(d_clear <= 0):
            print("Colliding.")