
import unittest
import random

def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    
    
def heaplify(lst, i, n):

    left_elem = left(i)
    right_elem = right(i)
    largest = i
    
    if left_elem < n and lst[left_elem] > lst[largest]:
        largest = left_elem
        
    if right_elem < n and lst[right_elem] > lst[largest]:
        largest = right_elem 
    
    if largest != i:
        swap(lst, largest, i)
        heaplify(lst, largest, n)
        
    
def pop(lst, n):
    if n <= 0:
        return 
    swap(lst, 0, n - 1)
    heaplify(lst, 0 , n - 1)
    

def heapsort(lst):
    n = len(lst)
    for i in range(n // 2 - 1, -1 ,- 1):
        heaplify(lst, i, n)
    
    for i in range(n - 1, 0 , -1):
        pop(lst, i + 1)
    
    sorted_lst = lst
    return sorted_lst



class TestHeapSort(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(heapsort(list(range(1, 101))), list(range(1, 101)))

    def test_reverse_sorted_array(self):
        self.assertEqual(heapsort(list(range(100, 0, -1))), list(range(1, 101)))

    def test_empty_array(self):
        self.assertEqual(heapsort([]), [])

    def test_single_element_array(self):
        self.assertEqual(heapsort([42]), [42])

    def test_large_numbers(self):
        self.assertEqual(heapsort([1000000000, 500, 0, -5000, 123456789, -999999999, 987654321] * 10), 
                         sorted([1000000000, 500, 0, -5000, 123456789, -999999999, 987654321] * 10))

    def test_floats(self):
        self.assertEqual(heapsort([1.1, 2.2, 0.5, -1.0, 3.3, -5.5, 4.4] * 15), 
                         sorted([1.1, 2.2, 0.5, -1.0, 3.3, -5.5, 4.4] * 15))

    def test_repeated_elements(self):
        self.assertEqual(heapsort([1, 1, 1, 1, 1, 1, 1, 1, 1, 1] * 10), [1] * 100)

    def test_large_dataset(self):
        
        large_list = random.sample(range(1, 10001), 5000)  # Случайная выборка из 5000 уникальных чисел
        self.assertEqual(heapsort(large_list), sorted(large_list))

    def test_negative_numbers(self):
        self.assertEqual(heapsort([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10] * 10), 
                         sorted([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10] * 10))

    def test_large_and_small_numbers(self):
        self.assertEqual(heapsort([1, -1, 100000, -100000, 0, 500, -500] * 20), 
                         sorted([1, -1, 100000, -100000, 0, 500, -500] * 20))

if __name__ == '__main__':
    unittest.main()