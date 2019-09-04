from RPhysics.Objects import *
from RPhysics.MathObjects import const
def NewtonianGravity(o,o_):
    omass = o.GetMass()
    o_mass = o_.GetMass()
    F = const.G*omass*o_mass/o.Pos.GetDistanceSquare(o_.Pos)
    acc = F/o_mass
    angle = o.Pos.GetTargetAngle(o_.Pos)
    o_.Vector.SplitVectorSub(acc,angle)
def Collide(o,o_):
    pass
def GetOrbitRadius(velocity=0,mass=0.0):
    return const.G*mass/velocity**2
def GetOrbitVelocity(radius=1.0,mass=1.0):
    return (const.G*float(mass)/float(radius))**0.5