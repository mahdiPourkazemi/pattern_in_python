from shape import Circle,Rectangle,Triangle
from area_calculator import AreaCalculator

def main():
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 7)
    
    calculator = AreaCalculator()
    
    print(f"Circle Area: {circle.calculate_area_with(calculator)}")
    print(f"Rectangle Area: {rectangle.calculate_area_with(calculator)}")
    print(f"Triangle Area: {triangle.calculate_area_with(calculator)}")
    
if __name__=="__main__":

    main()