import math
from interface import AreaCalculatorInterface


class AreaCalculator(AreaCalculatorInterface):

    def calculate_circle_area(self, circle):
        # مساحت دایره = π * r^2
        return math.pi * circle.radius ** 2

    def calculate_rectangle_area(self, rectangle):
        # مساحت مستطیل = طول * عرض
        return rectangle.width * rectangle.height

    def calculate_triangle_area(self, triangle):
        # مساحت مثلث = (قاعده * ارتفاع) / 2
        return (triangle.base * triangle.height) / 2


