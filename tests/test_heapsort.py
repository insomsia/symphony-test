import unittest

from heapsort import heap_sort


class HeapSortTests(unittest.TestCase):
    def test_returns_empty_list_for_empty_input(self) -> None:
        self.assertEqual(heap_sort([]), [])

    def test_returns_single_element_list_unchanged(self) -> None:
        self.assertEqual(heap_sort([42]), [42])

    def test_sorts_duplicates_and_negative_numbers(self) -> None:
        values = [5, -1, 3, 5, 0, -7, 3]
        self.assertEqual(heap_sort(values), [-7, -1, 0, 3, 3, 5, 5])

    def test_preserves_sorted_order(self) -> None:
        values = [1, 2, 3, 4, 5]
        self.assertEqual(heap_sort(values), [1, 2, 3, 4, 5])

    def test_sorts_reverse_ordered_input(self) -> None:
        values = [9, 7, 5, 3, 1]
        self.assertEqual(heap_sort(values), [1, 3, 5, 7, 9])

    def test_does_not_mutate_input_sequence(self) -> None:
        values = [4, 1, 6, 2]
        result = heap_sort(values)
        self.assertEqual(result, [1, 2, 4, 6])
        self.assertEqual(values, [4, 1, 6, 2])


if __name__ == "__main__":
    unittest.main()
