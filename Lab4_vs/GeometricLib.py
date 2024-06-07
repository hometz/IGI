from abc import ABC, abstractmethod
import math
import matplotlib.pyplot as plt

class FigureColor:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

class GeometricFigure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

class Rectangle(GeometricFigure):
    figure_name = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigureColor(color)

    def area(self):
        return self.width * self.height

    def draw(self):
        fig, ax = plt.subplots()
        ax.add_patch(plt.Rectangle((0, 0), self.width, self.height, color=self.color.color))
        plt.xlim(-1, self.width + 1)
        plt.ylim(-1, self.height + 1)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.title(self.figure_name)
        plt.show()

    def __str__(self):
        return "Фигура: {0}, Цвет: {1}, Ширина: {2}, Высота: {3}, Площадь: {4:.2f}".format(
            self.figure_name, self.color.color, self.width, self.height, self.area()
        )

    @classmethod
    def get_figure_name(cls):
        return cls.figure_name

class Triangle(GeometricFigure):
    figure_name = "Треугольник"

    def __init__(self, side_a, side_b, angle_C, color):
        self.side_a = side_a
        self.side_b = side_b
        self.angle_C = angle_C
        self.color = FigureColor(color)

    def area(self):
        angle_C_radians = math.radians(self.angle_C)
        return 0.5 * self.side_a * self.side_b * math.sin(angle_C_radians)

    def draw(self):
        angle_C_radians = math.radians(self.angle_C)
        x3 = self.side_a * math.cos(angle_C_radians)
        y3 = self.side_a * math.sin(angle_C_radians)

        fig, ax = plt.subplots()
        triangle = plt.Polygon([[0, 0], [self.side_b, 0], [x3, y3]], color=self.color.color)
        ax.add_patch(triangle)
        plt.xlim(-1, max(self.side_b, x3) + 1)
        plt.ylim(-1, max(y3, self.side_b) + 1)
        plt.title(self.figure_name)
        plt.show()

def save_to_file(figure):
    with open("output3.txt", "w", encoding="utf-8") as file:
        file.write(str(figure))
