from math import *

class Vector(object):
    
    def __init__(self, mag=0, angle=0):

        self.duration = 0
        
        if type(mag) in [float, int] and \
            type(angle) in [float, int]:
                
            self.magnitude = mag
            self.angle = angle
        else:
            raise TypeError("valid types: int, float")
    
    def components(self, x=0, y=0):
        
        # do stuff

        return self

    @property
    def x(self):
        return cos(self.angle)*self.magnitude
    
    @property
    def y(self):
        return sin(self.angle)*self.magnitude

    @x.setter
    def x(self, val):
        x = val
        y = self.y

        self.magnitude = hypot(x, y)
        self.angle = atan2(y, x)
    
    @y.setter
    def y(self, val):
        x = self.x
        y = val

        self.magnitude = hypot(x, y)
        self.angle = atan2(y, x)

    def __add__(self, other): 
        return Vector().components(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector().components(self.x-other.x, self.y-other.y)
    
    def __mul__(self, other):
        
        if type(other) in [float, int]:
            v = Vector(self.magnitude*other, self.angle)
            return v
        else:
            raise NotImplementedError("supported types: float, int")
        
    def __str__(self):
        return f"{self.__class__.__name__}(angle={round(self.angle,2)}, mag={round(self.magnitude,2)}, x={round(self.x,2)}, y={round(self.y,2)})"


class Particle()