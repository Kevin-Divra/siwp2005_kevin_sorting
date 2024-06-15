import unittest
from sort.bubble_sort import BubbleSort

class TestBubbleSort(unittest.TestCase):
    def test_bubble(self):
        arr = [10, 54, 37, 24, 96, 45]
        print('this is the unsorted list:')
        print(arr)
        result = BubbleSort.sort(arr)
        print('this is the (bubble) sorted list:')
        print(result)

if __name__ == '__main__':
    unittest.main()
