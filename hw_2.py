class Figure:

    unit = "cm"

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass




class Square(Figure):

    def __init__(self,side_length):
        self.__side_length = side_length

    def calculate_area(self):#площадь КВАДРАТА(переопределенный)
        return self.__side_length**2

    def info(self):#вывод информации о фигуре(переопределенный)
        return (f"Square side length: {self.__side_length}{Figure.unit},"
              f" area: {self.calculate_area()}{Figure.unit}.")


class Rectangle(Figure):

    def __init__(self,length,width):
        self.__length = length
        self.__width = width

    def calculate_area(self):#площадь ПРЯМОУГОЛЬНИКА(переопределенный)
        return self.__length * self.__width

    def info(self):#вывод информации о фигуре(переопределенный)
        return (f"rectangle length: {self.__length}{Figure.unit}, "
                      f"width:{self.__width}{Figure.unit},"
                      f" area: {self.calculate_area()}{Figure.unit}.")


#начало запуска
square1 = Square(10)
square2 = Square(7)
rect1 = Rectangle(15,5)
rect2 = Rectangle(11,7)
rect3 = Rectangle(12,5)

list_figure = [square1,square2,rect1,rect2,rect3]

for information in list_figure:
    print(information.info())