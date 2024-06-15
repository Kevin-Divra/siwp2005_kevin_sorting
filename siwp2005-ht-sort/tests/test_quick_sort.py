import unittest
from sort.quick_sort import QuickSort

class TestQuickSort(unittest.TestCase):
    def test_bubble(self):
        arr = [0, 80, 87, 34, 32, 20]
        print('this is the unsorted list:')
        print(arr)
        result = QuickSort.sort(arr)
        print('this is the (Quick) sorted list:')
        print(result)

if __name__ == '__main__':
    unittest.main()
