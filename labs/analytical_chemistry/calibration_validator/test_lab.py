import unittest
from lab import calculate_metric

class TestLab(unittest.TestCase):
    def test_example(self):
        # Starter sanity test
        self.assertTrue(callable(calculate_metric))

if __name__ == '__main__':
    unittest.main()
