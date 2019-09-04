from RPhysics.Objects import *

class RUniverse(object):
    """description of class"""
    def __init__(self,GameDisplay,Width=1360,Height=768):
        self.UniverseObjects = []
        self.Width = Width
        self.Height = Height
        self.GameDisplay = GameDisplay
        self.CamPos = Position2D(0,0)
        self.Zoom = 1
        self.DefaultDensity = 5e+13
    def AddParticle(self,pos=Position2D(0,0),color=Color(255,255,255),vector = Vector2D(0,0),volume=1,density=0,radius=5):
        if(not density): density = self.DefaultDensity
        obj = Circle(pos=pos,color=color,vector=vector,volume=volume,density=density,radius=radius)
        self.UniverseObjects.append(obj)
        return obj
    def Draw(self):
        for Object in self.UniverseObjects:
            Object.DrawRelative(self.GameDisplay,self.CamPos,self.Zoom)
    def Calculate(self):
        for Object in self.UniverseObjects:
            for Object_2 in self.UniverseObjects:
                if(Object != Object_2):
                    Object._(Object_2)