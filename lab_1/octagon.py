import math as m
import turtle

class Octagon():

    def __init__(self, side): 
        self.side = side 
        self.corner = 45
        k = 1 + m.sqrt(2)
        self.k = k
        self.radius_square_described()
        self.radius_square_entered()
        self.area_square_octagon()
        self.draw_octagon()

    def draw_octagon(self): 
        turtle.clear()
        turtle.speed(0)
        
        turtle.penup()
        turtle.goto(0, -self.radius_described)
        turtle.pendown()
        turtle.pencolor("blue")
        turtle.circle(self.radius_described)
        
        
        turtle.penup()
        turtle.goto(0, -self.radius_entered)
        turtle.pendown()
        turtle.pencolor("red")
        turtle.circle(self.radius_entered)

        turtle.pencolor("black")
        for i in range(8):
            turtle.left(self.corner)
            turtle.forward(self.side)
            

        turtle.done()

    def radius_square_entered(self):
        self.radius_entered = ((self.side * self.k) / 2)
        print(f"радиус вписанной окружности: {self.radius_entered}")
        self.square_entered = m.pi * self.radius_entered ** 2
        print(f"площадь вписанной окружности: {self.square_entered}")

    def radius_square_described(self):
        self.radius_described = (self.side / 2) * m.sqrt(4 + 2 * m.sqrt(2))
        print(f"радиус описанной окружности: {self.radius_described}")
        self.square_described = m.pi * self.radius_described ** 2 
        print(f"площадь описанной окружности: {self.square_described}")
    
    def area_square_octagon(self):
        self.perimetr_octagon = self.side * 8
        print(f"Периметр октагона: {self.perimetr_octagon}")
        self.squar_octagon = 2 * self.k * self.side ** 2
        print(f"Площадь октагона: {self.squar_octagon}")

    def __del__(self):
        pass
    
Octagon(100)