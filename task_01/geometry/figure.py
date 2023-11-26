from math import pi


class Circle:
    def __init__(self, args):
        self.args = args
        self.type_f = "Круг"
        self.res = pi * self.args**2
        return self.type_f, self.res


class Triangle:
    def __init__(self, args) -> None:
        self.args = list(args)
        self.args.sort()
        if (self.args[0] + self.args[1] > self.args[2] and 
            self.args[1] + self.args[2] > self.args[0] and  
            self.args[2] + self.args[0] > self.args[1]):
            if self.args[2]**2 == self.args[1]**2 + self.args[0]**2:
                self.type_f = 'Треугольник прямоугольный'
            else:
                self.type_f = 'Треугольник обычный'
            p = sum(self.args)/2
            self.res = ((p*(p-self.args[0])*(p-self.args[1])*(p-self.args[2])))**0.5
        else:
            self.type_f = 'Треугольника не существует'
            self.res = None
        return self.type_f, self.res

    
class Area:
    def __init__(self, *args: int|float) -> None:
        self.args = args
        if len(args) == 1:
            result = Circle.__init__(self, args[0])
        elif len(args) == 3:
            result = Triangle.__init__(self, args)
        else:
            result = 'Такой фигуры у нас нет', None
        self.result = result