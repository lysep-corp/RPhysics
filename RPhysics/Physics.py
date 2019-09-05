from RPhysics.Objects import *
from RPhysics.MathObjects import const
def Relativity(speed):
    return (1-speed**2/const.c**2)**0.5
def NewtonianGravity(o,o_):
    omass = o.GetMass()
    o_mass = o_.GetMass()
    F = const.G*omass*o_mass/o.Pos.GetDistanceSquare(o_.Pos)
    angle = o_.Pos.GetTargetAngle(o.Pos)
    acc = o_.Force_(F,angle)*Relativity(o_.Vector.Value)
    return Vector2D(angle,acc)
def Collide(o,o_):
    tangent = o_.Pos.GetTargetAngle(o.Pos)+0.5*const.pi
    #o.rp.Console.log("%s Tangent : %s°"%(o.Name,math.degrees(tangent)))
    #o.rp.Console.log("%s Reflection : %s°"%(o.Name,math.degrees(2*tangent-o.Vector.Angle)))
    o.Vector.SetAngle(2*tangent-o.Vector.Angle)
    o_.Vector.SetAngle(2*tangent-o_.Vector.Angle)
    o.SwitchMomentum(o_)
def GetOrbitRadius(velocity=0,mass=0.0):
    return const.G*mass/velocity**2
def GetOrbitVelocity(radius=1.0,mass=1.0):
    return (const.G*float(mass)/float(radius))**0.5