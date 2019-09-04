from RPhysics.Objects import *
from RPhysics.MathObjects import const
def NewtonianGravity(o,o_):
    omass = o.Volume*o.Density
    o_mass = o.Volume*o.Density
    F = const.G*omass*o_mass/o.Pos.GetDistanceSquareWithTarget(o_.Pos)
    acc = F/o_mass
    angle = o.Pos.GetTargetAngle(o_.Pos)
    o_.Vector.SplitVectorAdd(acc,angle)