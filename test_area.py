from unittest import TestCase
import area 

class TestShapeAreas(TestCase):
    
    # Tests if the math works in the program
    def test_triangle_area(self):
        # A triangle with height of 4 and a base of 3 should have an area of 10
        self.assertEqual(10, area.triangle_area(4, 5))
    
    # Tests if the math works, but with floating points of numbers
    def test_triangle_area_floating_point(self):
        self.assertAlmostEqual(17.79875, area.triangle_area(7.25, 4.91))
        
    # Tests if a Value Error is raised if a negative number is used    
    def test_negative_base_height_raises_value_error(self):
        
        with self.assertRaises(ValueError):
            area.triangle_area(9, -10)
        
        with self.assertRaises(ValueError):
            area.triangle_area(-9, 10)
            
        with self.assertRaises(ValueError):
            area.triangle_area(-9, -10) 
    
    # Tests if adding a zero still equals a zero        
    def test_triangle_base_height_zero(self):
        self.assertEqual(0, area.triangle_area(0, 1))
        self.assertEqual(0, area.triangle_area(1, 0))
        self.assertEqual(0, area.triangle_area(0, 0))