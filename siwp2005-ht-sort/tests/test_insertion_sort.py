import unittest
from sort.insertion_sort import InsertionSort

class TestInsertionSort(unittest.TestCase):
    def test_bubble(self):
        arr = [0, 90, 73, 55, 67, 45] 
        print('this is the unsorted list:')
        print(arr)
        result = InsertionSort.sort(arr)
        print('this is the (insertion) sorted list:')
        print(result)

if __name__ == '__main__':
    unittest.main()
