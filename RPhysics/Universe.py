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
        self.DefaultDensity = 1e+10
        self.DefaultVolume = 5
    def AddParticle(self,pos=Position2D(0,0),color=Color(255,255,255),vector = Vector2D(0,0),volume=0,density=0):
        if(not density): density = self.DefaultDensity
        if(not volume): volume = self.DefaultVolume
        obj = Circle(pos=pos,color=color,vector=vector,volume=volume,density=density)
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