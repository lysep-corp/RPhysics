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
    tangent = o.Pos.GetTargetAngle(o_.Pos)
    o.Vector.SetAngle(2*tangent-o.Vector.Angle)
    o_.Vector.SetAngle(2*tangent-o_.Vector.Angle)
    #s1 = o.Vector.Value
    #s2 = o_.Vector.Value
    #o_.Vector.SetValue(s1)
    #o.Vector.SetValue(s2)
def GetOrbitRadius(velocity=0,mass=0.0):
    return const.G*mass/velocity**2
def GetOrbitVelocity(radius=1.0,mass=1.0):
    return (const.G*float(mass)/float(radius))**0.5