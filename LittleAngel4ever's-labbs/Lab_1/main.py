from octagon import Octagon

def func():
    inp = input('Enter the length of the side of the octagon\n')
    octagon = Octagon(int(inp))
    print(f'The radius of a circle circumscribed about an octagon is \n{octagon.radius_opis()}')
    print(f'The radius of a circle inscribed in an octagon is \n{octagon.radius_vpis()}')
    print(f'The square of the circle described about the octagon is equal to \n{octagon.square_opis()}')
    print(f'The square of a circle inscribed in an octagon is equal to \n{octagon.square_vpis()}')
    octagon.square()
    octagon.perimetr()
    octagon.paint()
    octagon.square()
    
def main():
    func()


if __name__ == '__main__':
    main()