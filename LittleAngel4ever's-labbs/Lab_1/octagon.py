from math import sqrt, pi, cos, sin
import matplotlib.pyplot as pl


class Octagon:
    
    def __init__(self, hand:int):
        self.hand = hand
        self.degree = 45
        self.k = 1 + sqrt(2)

    # Calculating the radius of a circumscribed circle    
    def  radius_opis(self) -> float:    
        radius = sqrt((1 + sqrt(2)) / ((1 + sqrt(2)) - 1)) * self.hand
        return radius
    
    # Calculating the radius of an inscribed circle
    def radius_vpis(self) -> float: 
        radius = (self.hand / 2) * (1 + sqrt(2))
        return radius
    
    def square_opis(self):
        S = pi * int(self.radius_opis()) ** 2
        return S
        
    def square_vpis(self):
        S = pi * int(self.radius_vpis()) ** 2
        return S
    
    # Perimeter of an octagon
    def perimetr(self):
        print(f'The perimeter of an octagon is: {self.hand * 8}\n')

    # Area of ​​an octagon
    def square(self):
        S = 2 * (self.hand ** 2) * (sqrt(2) + 1)
        print(f'The area of ​​an octagon is equal to: {S}\n')

    # Finding the peaks
    def peaks(self) -> list: 
        # List of vertices
        peaks_1 = []
        peaks_2 = []     

        # Creating a list of vertices
        for i in range(8):      
            x = self.radius_opis() * cos((pi/8) + i * (pi/4))
            y = self.radius_opis() * sin((pi/8) + i * (pi/4))
            peaks_1.append(x)
            peaks_2.append(y)

        # Add the first coordinate to the end to close the vertices
        peaks_1.append(peaks_1[0])      
        peaks_2.append(peaks_2[0])
        return peaks_1, peaks_2
    
    # Drawing figures
    def paint(self):

        # Describe a circle around an octagon
        circle_1 = pl.Circle((0, 0), self.radius_opis(), color = 'green', fill = False)     
        ax = pl.gca()
        ax.add_patch(circle_1)

        # Inscribe a circle into an octagon
        circle_2 = pl.Circle((0, 0), self.radius_vpis(), color = 'gold', fill = False)      
        ax = pl.gca()
        ax.add_patch(circle_2)

        # Vertex octagon
        x,y = self.peaks()      
        pl.plot(x, y, color = 'purple')

        # Show on screen
        pl.axis('scaled')       
        pl.show()

    def __del__(self):
        print('The octagon was removed successfully!')
    
def left():

    value = input('Enter the length of the side of the octagon\n')
    oct = Octagon(int(value))
    print(oct.radius_opis())
    print(oct.radius_vpis())
    oct.square()
    oct.paint()
    print('-------------')
    x,y = oct.peaks()
    print(x)
    print(y)


def main():
    left()


if __name__ == '__main__':
    main()