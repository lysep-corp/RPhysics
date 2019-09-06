import pygame as pg
from RPhysics.MathObjects import *
from RPhysics.Objects import *
from RPhysics.Tools import *
from RPhysics.Universe import *
import time
import sys
import random
class RPhysic:
    def __init__(self):
        pg.init()
        pg.display.set_caption('RPhysics')
        self.Done = False
        self.wh = Rectangle(800,600)
        self.GameDisplay = pg.display.set_mode(self.wh.t())
        self.GameClock   = pg.time.Clock()
        self.Universe = RUniverse(self.GameDisplay,self,self.wh.width,self.wh.height)
        self.Console= Console(self.GameDisplay,self.wh,self)
        self.Mouse = Mouse(self)
        self.Keyboard = Keyboard(self)
        self.Pause = True
        self.Clock = Clock()
        setInterval(lambda :self.Console.Debug("FPS",self.Clock.FPS),0.1)
        setInterval(lambda :self.Console.Debug("CPS Universe",self.Universe.Clock.FPS if self.Universe.Clock.FPS != -1 else "Unlimited"),0.1)
        setInterval(lambda :self.Console.Debug("CPS Limit",self.Universe.Clock.FPS_LIMIT if self.Universe.Clock.FPS_LIMIT != -1 else "Unlimited"),0.1)
        setInterval(lambda :self.Console.Debug("ZOOM",self.Universe.Zoom),0.1)
        setInterval(lambda :self.Console.Debug("D_Density",self.Universe.DefaultDensity),0.1)
        setInterval(lambda :self.Console.Debug("D_Volume",self.Universe.DefaultVolume),0.1)
        self.Clock.FPS_LIMIT = 120
        self.scene_3()
    def scene_1(self):
        obj = self.Universe.AddParticle(pos=self.wh.GetCenter_p(),volume=140,color=Color(0,0,255).GetTuple(),density=1e+12,name="Alpha")
        obj2 = self.Universe.AddParticle(pos=self.wh.GetCenter_p().Divide(y=10/3),vector=Vector2D(),volume=5,density=10,name="Beta")
        vel  = GetOrbitVelocity(obj2.Pos.GetDistance(obj.Pos),obj.GetMass())
        obj2.Vector.Add_(x=vel)
    def scene_2(self):
        self.Clock.FPS_LIMIT = 120
        obj = self.Universe.AddParticle(
            pos=self.wh.GetCenter_p().Multiple(y=3/2,x=1/2),
            vector=Vector2D(math.radians(-45),1),
            volume=50,
            color=Color(0,0,255).GetTuple(),
            density=1,
            name="Alpha"
            )
        obj2 = self.Universe.AddParticle(
            pos=self.wh.GetCenter_p().Multiple(y=3/2,x=3/2),
            vector=Vector2D(math.radians(225),1),
            volume=10,
            density=1,
            name="Beta"
            )
    def scene_3(self):
        self.Clock.FPS_LIMIT = 120

        obj = self.Universe.AddParticle(
            pos=self.wh.GetCenter_p().Multiple(x=1/2,y=2/3),
            volume=50,
            density=1e+12,
            color=Color(0,0,255).GetTuple(),
            name="Alpha"
            )
        obj2 = self.Universe.AddParticle(
            pos=self.wh.GetCenter_p().Multiple(x=3/2,y=3/2),
            vector=Vector2D(math.degrees(-45),2),
            volume=50,
            density=1e+12,
            name="Beta"
            )    
        
    def Exit(self,event=None):
        DONE_INTERVALS = True
        self.Done = True
    def ButtonDown(self,event):
        self.Mouse.eventExecutor(event)
    def Key(self,event):
        self.Keyboard.eventExecutor(event)
    def EventExecutor(self,event):
        events = {
            pg.QUIT:self.Exit,
            pg.MOUSEBUTTONDOWN:self.ButtonDown,
            pg.KEYDOWN:self.Key,
            pg.KEYUP:self.Key
        }
        try:
            fun=events[event.type]
            if callable(fun):fun(event)
        except KeyError:
            return
    def init(self):
        d  = 0.0
        d_ = 0.0
        self.Universe.ThreadCalculate()
        self.Clock.Tick()
        while not self.Done:
            for event in pg.event.get():
                self.EventExecutor(event)
                if event.type == pg.QUIT:
                    self.Done = True
            self.GameDisplay.fill((0,0,0))
            #if(not self.Pause):
            #    self.Universe.Calculate()
            self.Universe.ControlCPS()
            self.Universe.MoveCam()
            self.Universe.Draw()
            self.Console.Draw()
            pg.display.update()
            self.Mouse.Tick()
            self.Clock.Limit()
            self.Clock.Tick()
        pg.quit()

