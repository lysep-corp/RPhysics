from RPhysics.Objects import *
from RPhysics.Tools import Clock
import threading
class RUniverse(object):
    """description of class"""
    def __init__(self,GameDisplay,rp,Width=1360,Height=768):
        self.UniverseObjects = []
        self.Width = Width
        self.Height = Height
        self.GameDisplay = GameDisplay
        self.CamPos = Position2D(0,0)
        self.Zoom = 1
        self.DefaultDensity = 10
        self.DefaultVolume = 5
        self.rp = rp
        self.Clock = Clock()
        self.Clock.FPS_LIMIT = 120
        self.UniverseCPSController = 0
        self.MovePos=Position2D(0,0)
        self.TC = threading.Thread(target=self.ThreadCalculate_)
    def AddParticle(self,pos=Position2D(0,0),color=Color(255,255,255),vector = Vector2D(0,0),volume=0,density=0,name=None):
        if(not density): density = self.DefaultDensity
        if(not volume): volume = self.DefaultVolume
        obj = Circle(self.rp,pos=pos,color=color,vector=vector,volume=volume,density=density,name=name)
        self.UniverseObjects.append(obj)
        return obj
    def MoveCam(self):
        self.CamPos.Add(self.MovePos)
    def ControlCPS(self):
        if(self.Clock.FPS_LIMIT > 0 and self.UniverseCPSController == -1):
            self.Clock.FPS_LIMIT += self.UniverseCPSController
        elif(self.UniverseCPSController == 1):
            self.Clock.FPS_LIMIT += self.UniverseCPSController
    def Draw(self):
        for Object in self.UniverseObjects:
            Object.DrawRelative(self.GameDisplay,self.CamPos,self.Zoom)
    def Calculate(self):
        for Object in self.UniverseObjects:
            for Object_2 in self.UniverseObjects:
                if(Object != Object_2):
                    Object._(Object_2)
    def ThreadCalculate_(self):
        while not self.rp.Done:
            if(not self.rp.Pause):
                self.Calculate()
            self.Clock.Limit()            
            self.Clock.Tick()
    def ThreadCalculate(self):
        self.TC.start()