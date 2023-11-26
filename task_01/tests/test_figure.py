import unittest
from geometry.figure import Area

class TestArea(unittest.TestCase):
    def setUp(self):
        self.area = Area()

    def test_circle_type(self):
        self.assertEqual(Area(3).result[0], 'Круг')

    def test_circle_result(self):
        self.assertEqual(Area(3).result[1], 28.274333882308138)
    
    def test_triangle_type(self):
        self.assertEqual(Area(3, 5, 7).result[0], 'Треугольник обычный')

    def test_triangle_result(self):
        self.assertEqual(Area(3, 5, 7).result[1], 6.49519052838329)

    def test_right_triangle_type(self):
        self.assertEqual(Area(3, 5, 4).result[0], 'Треугольник прямоугольный')

    def test_right_triangle_result(self):
        self.assertEqual(Area(3, 5, 4).result[1], 6)
    
    def test_unknown_type(self):
        self.assertEqual(Area(3, 4).result[0], 'Такой фигуры у нас нет')

    def test_unknown_result(self):
        self.assertEqual(Area(3, 4).result[1], None)

if __name__ == '__main__':
    unittest.main(verbosity=2)