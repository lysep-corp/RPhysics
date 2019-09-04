import pygame as pg
from RPhysics.MathObjects import *
from RPhysics.Objects import *
from RPhysics.Tools import *
from RPhysics.Universe import *
import time

class RPhysic:
    def __init__(self):
        pg.init()
        pg.display.set_caption('RPhysics')
        self.GameDone = False
        self.wh = Rectangle(800,600)
        self.GameDisplay = pg.display.set_mode(self.wh.t())
        self.GameClock   = pg.time.Clock()
        self.Universe = RUniverse(self.GameDisplay,self.wh.width,self.wh.height)
        self.Console= Console(self.GameDisplay,self.wh,self)
        self.Mouse = Mouse(self)
        self.Keyboard = Keyboard(self)
        self.Pause = True
        self.Clock = Clock()
        self.scene_1()
    def scene_1(self):
        fpsd = setInterval(lambda :self.Console.Debug("FPS",self.Clock.FPS),0.1)
        obj = self.Universe.AddParticle(pos=self.wh.GetCenter_p(),volume=5)
        obj2 = self.Universe.AddParticle(pos=self.wh.GetCenter_p().Divide(y=4),vector=Vector2D(),volume=5)
        obj2.Vector.Add_(x=GetOrbitVelocity(obj.Pos.GetDistance(obj2.Pos),obj.GetMass()))
    def Exit(self,event=None):
        self.GameDone = True
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
        d  =0.0
        d_ = 0.0
        while not self.GameDone:
            for event in pg.event.get():
                self.EventExecutor(event)
                if event.type == pg.QUIT:
                    self.GameDone = True
            self.GameDisplay.fill((0,0,0))
            if(not self.Pause):
                self.Universe.Calculate()
            self.Universe.Draw()
            self.Console.Draw()
            pg.display.update()
            self.Clock.Tick()
        pg.quit()

