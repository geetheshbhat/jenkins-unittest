import unittest
from surface_area import surface_area

class TestSurface(unittest.TestCase):
    def test_positive_value(self):
        self.assertEqual(surface_area(10,20),200)
    
    def test_large_value(self):
        self.assertEqual(surface_area(999,181),181*999)

    def test_with_x_zero(self):
        with self.assertRaises(ValueError):
            surface_area(0,2)

    def test_with_y_zero(self):
        with self.assertRaises(ValueError):
            surface_area(2,0)

    def test_with_negative_value(self):
        with self.assertRaises(ValueError):
            surface_area(-3,2)
    
    def test_with_char(self):
        with self.assertRaises(TypeError):
            surface_area('a',2)
    
    def test_with_list(self):
        with self.assertRaises(TypeError):
            surface_area([1,2],2)
    
    def test_with_boolean(self):
        with self.assertRaises(TypeError):
            surface_area(True,False)

if __name__ == '__main__':
    unittest.main()