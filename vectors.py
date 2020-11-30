from math import hypot, sin, cos, tan, atan2


class Vector(object):
    
    def __init__(self, x=0, y=0):
        
        if type(x) in [float, int] and \
            type(y) in [float, int]:
                
            self.x = x
            self.y = y
        else:
            raise TypeError("valid types: int, float")
    
    @property
    def magnitude(self):
        '''
        returns the magnitude of the vector
        '''
        
        return round(hypot(self.x, self.y),5)
    
    @magnitude.setter
    def magnitude(self, value):
        angle = self.angle
        self.x = round(cos(angle),5) * value
        self.y = round(sin(angle),5) * value
    
    @property
    def angle(self):
        '''
        returns the angle of the vector
        '''
        
        return atan2(self.y, self.x)
    
    @angle.setter
    def angle(self, value):
        magnitude = self.magnitude
        self.x = round(cos(value),5) * magnitude
        self.y = round(sin(value),5) * magnitude
        
    def __add__(self, other): 
        return Vector(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y)
    
    def __mul__(self, other):
        
        if type(other) in [float, int]:
            v = Vector(self.x, self.y)
            v.set_magnitude(self.magnitude*other)
            return v
        else:
            raise NotImplementedError("supported types: float, int")
        
    def __str__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, mag={round(self.magnitude,2)})"
    
class Force(Vector):
    
    def __init__(self, force : tuple=(0,0), time : float=0):
        
        if type(force) in (tuple, list):    
            super().__init__(*force)
        else:
            super().__init__(force.x, force.y)
        
        if type(time) in [float, int]:
            self.time = time
        else:
            raise TypeError("valid types: int, float")
    
    def normalize(self, time : float=1):
        '''
        Compresses or stretches the magnitude to the desired time length
        '''
        
        if type(time) not in [float, int]:
            raise TypeError("valid types: int, float")
        
        scale = self.time / time
        self.magnitude *= scale
    
    def __add__(self, other):      
        if type(other) == Vector:
            return Force(self.x+other.x, self.y+other.y, self.time)
        elif type(other) == Force:
            return [self, other]

    def __sub__(self, other):
        if type(other) == Vector:
            return Force(self.x-other.x, self.y-other.y, self.time)
        elif type(other) == Force:
            return [self, other]
    
    def __mul__(self, other):
        
        if type(other) in [float, int]:
            v = Vector(self.x, self.y)
            v.set_magnitude(self.magnitude*other)
            return Force(v, self.time)
        else:
            raise NotImplementedError("supported types: float, int")
    
    def __str__(self):
            return f"{self.__class__.__name__}(x={self.x}, y={self.y}, mag={round(self.magnitude,2)}), sec={round(self.time,2)}"
        

x = Force(Vector(3,4),5)
x.normalize(1)
print(x)