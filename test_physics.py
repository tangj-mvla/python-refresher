import physics as p
import unittest

class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertAlmostEqual(p.calculate_buoyancy(1,1),9.81)
        with self.assertRaises(ValueError):
            p.calculate_buoyancy(0,1)
        with self.assertRaises(ValueError):
            p.calculate_buoyancy(1,0)
        