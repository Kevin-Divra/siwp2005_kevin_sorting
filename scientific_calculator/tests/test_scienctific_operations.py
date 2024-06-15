import unittest
import math
from calculator.scientific_operations import sin, cos, tan, log

class TestScientificOperations(unittest.TestCase):

    def test_sin(self):
        self.assertAlmostEqual(sin(math.pi / 2), 1.0)
        self.assertAlmostEqual(sin(0), 0.0)

    def test_cos(self):
        self.assertAlmostEqual(cos(math.pi), -1.0)
        self.assertAlmostEqual(cos(0), 1.0)

    def test_tan(self):
        self.assertAlmostEqual(tan(math.pi / 4), 1.0)
        with self.assertRaises(ValueError):
            tan(math.pi / 2)

    def test_log(self):
        self.assertAlmostEqual(log(math.e), 1.0)
        with self.assertRaises(ValueError):
            log(-1)

unittest.main()
