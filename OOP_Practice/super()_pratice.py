class shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled

    def describe(self):
        print(f"The shape is {self.color} in color and it is {'filled' if self.is_filled==True else 'not filled'}")
        
class circle(shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled) #use of super
        self.radius=radius

    def describe(self): #method overriding used here
        print(f"This circle has a radius of {self.radius} and hence has an area of {3.14*self.radius*self.radius}")

class square(shape):
    def __init__(self,color,is_filled,side):
        super().__init__(color,is_filled)
        self.side=side

My_Circle=circle("red",True,10)

My_Circle.describe()