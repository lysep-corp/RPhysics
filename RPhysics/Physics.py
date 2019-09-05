from RPhysics.Objects import *
from RPhysics.MathObjects import const
def NewtonianGravity(o,o_):
    omass = o.GetMass()
    o_mass = o_.GetMass()
    F = const.G*omass*o_mass/o.Pos.GetDistanceSquare(o_.Pos)
    angle = o_.Pos.GetTargetAngle(o.Pos)
    acc = o_.Force_(F,angle)
    return Vector2D(angle,acc)
def Collide(o,o_):
    a = Vector2D(o_.Vector.Angle,100)
    a.Value = 100
    b = Vector2D(o.Vector.Angle,100)
    b.Value = 100
    tangent = o_.Pos.GetTargetAngle(o.Pos)
    o.Vector.SetAngle(2*tangent-o.Vector.Angle)
    o_.Vector.SetAngle(2*tangent-o_.Vector.Angle)
    o.rp.Console.ShowVector(a,o_,o)
    o.rp.Console.ShowVector(b,o,o_)
    s1 = o.Vector.Value
    s2 = o_.Vector.Value
    o_.Vector.SetValue(s1)
    o.Vector.SetValue(s2)
def GetOrbitRadius(velocity=0,mass=0.0):
    return const.G*mass/velocity**2
def GetOrbitVelocity(radius=1.0,mass=1.0):
    return (const.G*float(mass)/float(radius))**0.5