from RPhysics import Position2D,Rectangle,Color,Vector2D
from pygame import Surface,font,mouse
from pygame.draw import rect,line
from pygame import Rect,K_BACKQUOTE,K_BACKSPACE,KEYDOWN,KEYUP,K_t,K_r,K_F3,K_c,K_SPACE,K_q,K_UP,K_DOWN,K_LEFT,K_RIGHT,K_w,K_a,K_s,K_d
import threading
import time
import math
K_ENTER = 13
import shlex
DONE_INTERVALS = False
class Float:
    TOP=0
    RIGHT=1
    BOTTOM=2
    LEFT=3

class Margin:
    def __init__(self,top=0,right=0,bottom=0,left=0,float_=0):
        self.top=top
        self.right=right
        self.bottom=bottom
        self.left=left
        self.float=float_
def IntervalFunction(function,delay):
    global DONE_INTERVALS
    while not DONE_INTERVALS:
        function()
        time.sleep(delay)
def setInterval(function,delay):
    if callable(function):
        a = threading.Thread(target=IntervalFunction,args=(function,delay,))
        a.start()
        return a
class Clock:
    d = 0.0
    d_ = 0.0
    FPS = 0.0
    FPS_LIMIT = 0 # 0 Unlimited
    def __init__(self):
        pass
    def Tick(self):
        self.d = time.time()-self.d_
        if(self.d != 0):
            self.FPS= 1.0/self.d 
        else:
            self.FPS=-1
        self.d_ = time.time()
    def Limit_t(self):
        if(self.FPS_LIMIT):
            self.d = time.time()-self.d_
            if(self.d != 0):
                self.FPS= 1.0/self.d
            else:
                self.FPS=-1
            tt = 1.0/self.FPS_LIMIT
            d = tt-self.d
            if(d > 0.0):
                time.sleep(d)
            self.d_ = time.time()
        else:
            self.Tick()
    def Limit(self):
        if(self.FPS_LIMIT):
            t = time.time()-self.d_
            tt = 1.0/self.FPS_LIMIT
            d = tt-t
            if(d > 0):
                time.sleep(d)
class Keyboard:
    def __init__(self,rp):
        self.rp = rp 
    def executeCommand(self,event):
        pass
    def eventExecutor(self,event):
        if(event.key is K_BACKQUOTE and event.type is KEYDOWN):
                self.rp.Console.Open = not self.rp.Console.Open
        if(event.type is KEYDOWN and not self.rp.Console.Open):
            if(event.key is K_SPACE):
                self.rp.Pause = not self.rp.Pause
            elif(event.key is K_c):
                self.rp.Console.Clear([])
            elif(event.key is K_F3):
                self.rp.Console.DebugPointer = not self.rp.Console.DebugPointer
            elif(event.key is K_r):
                self.rp.Console.Reset([])
            elif(event.key == K_UP):
                self.rp.Universe.Clock.FPS_LIMIT+=5
            elif(event.key == K_DOWN):
                self.rp.Universe.Clock.FPS_LIMIT-=5
            elif(event.key == K_q):
                self.rp.Exit([])
            elif(event.key == K_w):
                self.rp.Universe.MovePos.y=1
            elif(event.key == K_s):
                self.rp.Universe.MovePos.y=-1
            elif(event.key == K_a):
                self.rp.Universe.MovePos.x=1
            elif(event.key == K_d):
                self.rp.Universe.MovePos.x=-1
        elif(event.type is KEYUP and not self.rp.Console.Open):
            if(event.key == K_w):
                self.rp.Universe.MovePos.y=0
            elif(event.key == K_s):
                self.rp.Universe.MovePos.y=0
            elif(event.key == K_a):
                self.rp.Universe.MovePos.x=0
            elif(event.key == K_d):
                self.rp.Universe.MovePos.x=0
        if(self.rp.Console.Open):
            self.rp.Console.Type(event)
        else:
            self.executeCommand(event)
class Mouse:
    def __init__(self,rp):
        self.rp = rp 
        self.i = 0
        self.mousepos = Position2D()
    def Tick(self):
        m = mouse.get_pos()
        self.mousepos.Set(m[0],m[1])
    def GetMouseHoverObject(self,mousepos=None):
        for obj in self.rp.Universe.UniverseObjects:
            if(obj.IsHover(mousepos if mousepos else self.mousepos)):
                return obj
    def eventLeftMouse(self,pos:Position2D):
        pos_ = self.rp.Universe.CamPos.Add_(pos)
        obj = self.GetMouseHoverObject()
        if(obj):
            obj.InfoBox = not obj.InfoBox
        else:
            self.rp.Universe.AddParticle(pos)
    def eventRightMouse(self,pos:Position2D):
        print("right mouse")
    def eventMiddleMouse(self,pos:Position2D):
        self.rp.Console.log("Test %s"%(self.i))
        self.i+=1
    def eventExecutor(self,event):
        if(event.button == 1):
            self.eventLeftMouse(Position2D(tuple_=event.pos))
        elif(event.button == 3):
            self.eventRightMouse(Position2D(tuple_=event.pos))
        elif(event.button == 2):
            self.eventMiddleMouse(Position2D(tuple_=event.pos))
class ConsoleText:
    def __init__(self,content="",class_="",id=0):
        self.id=id
        self.content=content
        self.class_=class_

class Console:
    UNDEFINED_VECTOR=Color(255,255,255)
    DEFINED_VECTOR=Color(255,0,0)
    def __init__(self,screen:Surface,screenResolution:Rectangle,rp):
        font.init()
        self.rp = rp
        self.screen = screen
        self.history = []
        self.cmdhistory = []
        self.screenRes = screenResolution
        self.IdCounter = 0
        self.Open = False
        self.UserInput = ""
        self.kpointer = False
        self.DebugPointer = True
        self.DebugVariables = {}
        #Options
        self.DebugColor     = Color(0,255,0) 
        self.PauseColor     = Color(0,255,0)
        self.Background     = Color().setHex("#313131")
        self.UserInputColor = Color().setHex("#212121")
        self.TextColor      = Color().setHex("#eeeeee")
        self.TextToShow = 5
        self.TextToShowOpen = 20
        self.TextSize=13
        self.VectorTextSize=12
        self.LineMargin = 3
        self.TopMargin = 5
        self.LeftMargin = 5
        self.BottomMargin = 5
        self.DebugMargin = Margin(5,5)
        self.DebugLineMargin = Margin(bottom=3)
        self.KeyDelay = 15
        self.Font = font.SysFont("Consolas",self.TextSize)
        self.Font_v = font.SysFont("Consolas",self.VectorTextSize)
    def _(self):
        lst = self.GetTexts()
        print(repr(lst))
    def ShowVector(self,Vector:Vector2D,dest=None,source=None):
        r = dest.GetRadius()
        spos = Position2D(
            dest.Pos.x+r*math.cos(Vector.Angle),
            dest.Pos.y+r*math.sin(Vector.Angle)
        )
        vl = (10 if Vector.Value <= 1 else Vector.Value*10)
        epos = Position2D(
            spos.x+vl*math.cos(Vector.Angle),
            spos.y+vl*math.sin(Vector.Angle)
        )
        #line(self.rp.GameDisplay,(255,255,255),(1,1),(10,10),width=10)
        #if(source):
            #text = self.Font_v.render("%s : %.2f"%(source.Name,Vector.Value),False,self.TextColor.GetTuple())
            #line(self.screen,self.DEFINED_VECTOR.GetTuple(),spos.GetTuple(),epos.GetTuple(),3)
            #self.screen.blit(text,epos.Add(Position2D(10,-6)).GetTuple())
        #else:
        text = "%s : %.2f"%(source.Name if source else "R",Vector.Value)
        text = self.Font_v.render(text,False,self.TextColor.GetTuple())
        line(self.rp.GameDisplay,(self.DEFINED_VECTOR if source else self.UNDEFINED_VECTOR).GetTuple(),spos.Add(self.rp.Universe.CamPos).GetTuple(),epos.Add(self.rp.Universe.CamPos).GetTuple(),3)
        self.rp.GameDisplay.blit(text,epos.Add(Position2D(6,-6)).GetTuple())
    def Debug(self,key,value):
        self.DebugVariables[key] = value
    def setCommand(self,args):
        if(len(args) >= 2):
            variableName = args[0]
            value = args[1]
            if(variableName == "density"):
                try:
                    d = self.rp.Universe.DefaultDensity
                    v = float(value) 
                    self.rp.Universe.DefaultDensity = v
                    self.log("Density changed %s to %s"%(d,v))
                except:
                    pass
            if(variableName == "volume"):
                try:
                    d = self.rp.Universe.DefaultVolume
                    v = float(value) 
                    self.rp.Universe.DefaultVolume = v
                    self.log("Volume changed %s to %s"%(d,v))
                except:
                    pass
            if(variableName == "zoom"):
                try:
                    d = self.rp.Universe.Zoom
                    v = float(value) 
                    self.rp.Universe.Zoom = v
                    self.log("Zoom changed %s to %s"%(d,v))
                except:
                    pass
    def Reset(self,args):
        self.Clear(args)
        self.rp.scene_1()
        self.log("Universe reset")
    def Clear(self,args):
        self.rp.Universe.UniverseObjects = []
        self.log("Universe cleared")
    def executeConsoleCommand(self,command):
        parsed = shlex.split(command)
        self.cmdhistory.append(command)
        cmd = "" if len(parsed) == 0 else parsed[0]
        args = [] if not len(parsed) > 0 else parsed[1:]
        cmds = {
            "exit":self.rp.Exit,
            "clear":self.Clear,
            "reset":self.Reset,
            "set":self.setCommand
        }
        if(cmd in cmds):
            if(callable(cmds[cmd])):
                cmds[cmd](args)

    def Type(self,event,w=0):
        if(event.type is KEYDOWN):
            if(event.key==K_BACKSPACE):
                self.UserInput = self.UserInput[:-1]
            elif(event.key==K_ENTER):
                cmd = self.UserInput
                self.UserInput = ""
                threading.Thread(target=self.executeConsoleCommand,args=(cmd,)).start()
            else:
                if(event.key != K_BACKQUOTE):
                    self.UserInput+=event.unicode
    def GetTexts(self):
        return list(self.history[len(self.history)-self.TextToShowOpen:] if len(self.history) > self.TextToShowOpen else self.history) if self.Open else list(self.history[len(self.history)-self.TextToShow:] if len(self.history) > self.TextToShow else self.history)
    def log(self,text=None,tag=None):
        if(text):
            if(tag):
                text = "[%s] %s"%(tag,text if type(text) is str else repr(text))
                self.history.append(ConsoleText(content=text,id=self.IdCounter))
                self.IdCounter+=1
            else:
                text = text if type(text) is str else repr(text)
                self.history.append(ConsoleText(content=text,id=self.IdCounter))
                self.IdCounter+=1
    def DrawInfoBox(self,hvrobj=None):
        if(not hvrobj):
            return None
        w = hvrobj.GetRadius()
        text = [
            "%s"%(hvrobj.Name),
            "X:%.2f"%(hvrobj.Pos.x),
            "Y:%.2f"%(hvrobj.Pos.y),
            "V_X:%.2f"%(hvrobj.Vector.x),
            "V_Y:%.2f"%(hvrobj.Vector.y),
            "Speed : %.2f"%(hvrobj.Vector.Value),
            "Angle : %.2f Degrees"%(math.degrees(hvrobj.Vector.Angle)),
            "Density : %.2E"%(hvrobj.Density),
            "Volume : %.2E"%(hvrobj.Volume)
        ]
        surfaces = [self.Font.render(i,False,self.TextColor.GetTuple())  for i in text]
        maxwidth = max([i.get_width() for i in surfaces])
        rect(
            self.screen,
            self.UserInputColor.GetTuple(),
            Rect(
                hvrobj.Pos.x+w,hvrobj.Pos.y-w+5,
                maxwidth+10,len(surfaces)*(self.TextSize+self.LineMargin)
            )
        )
        for surface,i in zip(surfaces,range(len(surfaces))):
            self.screen.blit(surface,(
                hvrobj.Pos.x+w+5,
                hvrobj.Pos.y-w+5+(i*self.TextSize+self.LineMargin)
            ))
    def Draw(self):
        lst = self.GetTexts()
        textoshow = self.TextToShow if not self.Open else self.TextToShowOpen
        if(self.rp.Pause):
            surface = self.Font.render("Paused",False,self.PauseColor.GetTuple())
            self.screen.blit(
                surface,
                (
                    self.LeftMargin+8,
                    self.screenRes.height-self.BottomMargin-self.TextSize
                )
            )
        self.DrawInfoBox(self.rp.Mouse.GetMouseHoverObject())
        for obj in self.rp.Universe.UniverseObjects:
            if(obj.InfoBox):
                self.DrawInfoBox(obj)
            #self.ShowVector(obj.Vector,obj)
            #for obj_ in obj.Vectors:
            #    self.ShowVector(obj.Vectors[obj_],obj_,obj)
        if(self.Open):
            rect(
                self.screen,
                self.Background.GetTuple(),
                Rect(
                    0,0,
                    self.screenRes.width,
                    self.TopMargin+(textoshow+1)*(self.TextSize+self.LineMargin)+self.BottomMargin
                    )
                )
            rect(
                self.screen,
                self.UserInputColor.GetTuple(),
                Rect(
                    self.LeftMargin+5,self.TopMargin+(textoshow)*(self.TextSize+self.LineMargin),
                    self.screenRes.width-(self.LeftMargin+5)*2,
                    self.TextSize+self.LineMargin
                    )
                )
            if(self.UserInput != ""):
                surface = self.Font.render(self.UserInput,False,self.TextColor.GetTuple())
                self.screen.blit(
                    surface,
                    (
                        self.LeftMargin+8,
                        self.TopMargin+(textoshow)*(self.TextSize+self.LineMargin)+2
                    )
                )
        for (line,i) in zip(lst,range(len(lst))):
            surface = self.Font.render(line.content,False,self.TextColor.GetTuple())
            pos = Position2D(
                self.LeftMargin,
                self.TopMargin+i*(self.TextSize+self.LineMargin)
                )
            self.screen.blit(surface,pos.GetTuple())
        if(self.DebugPointer):
            for key,i in zip(self.DebugVariables,range(len(self.DebugVariables))):
                text = "%s : %s"%(self.DebugVariables[key] if type(self.DebugVariables[key]) is str else (repr(self.DebugVariables[key]) if not type(self.DebugVariables[key]) is float else ("%.2f"%(self.DebugVariables[key]) if self.DebugVariables[key] < 10e+4 else "%.2E"%(self.DebugVariables[key]) )),key)
                surface = self.Font.render(text,False,self.DebugColor.GetTuple())
                self.screen.blit(
                    surface,
                    (
                        self.screenRes.width-(surface.get_width()+self.DebugMargin.right),
                        self.DebugMargin.top+i*(self.DebugLineMargin.bottom+self.TextSize)
                    )
                )