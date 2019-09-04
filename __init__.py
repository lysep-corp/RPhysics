import pygame as pg
from RPhysics.MathObjects import *
from RPhysics.Objects import *
from RPhysics.Tools import *
from RPhysics.Universe import *
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
        self.scene_1()
    def scene_1(self):
        pass#obj = self.Universe.AddParticle(pos=self.wh.GetCenter_p())
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
        while not self.GameDone:
            for event in pg.event.get():
                self.EventExecutor(event)
                if event.type == pg.QUIT:
                    self.GameDone = True
            self.GameDisplay.fill((0,0,0))
            self.Universe.Calculate()
            self.Universe.Draw()
            self.Console.Draw()
            pg.display.update()
        pg.quit()

