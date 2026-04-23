"""Heap sort implementation."""

from typing import Iterable, List, TypeVar

T = TypeVar("T")

__all__ = ["heap_sort"]


def heap_sort(values: Iterable[T]) -> List[T]:
    """Return a new list containing *values* sorted in ascending order.

    The input iterable is copied before sorting so callers keep their original
    data unchanged.
    """

    items = list(values)
    length = len(items)
    if length < 2:
        return items

    for start in range(length // 2 - 1, -1, -1):
        _sift_down(items, start, length)

    for end in range(length - 1, 0, -1):
        items[0], items[end] = items[end], items[0]
        _sift_down(items, 0, end)

    return items


def _sift_down(heap: List[T], start: int, end: int) -> None:
    root = start
    while True:
        child = 2 * root + 1
        if child >= end:
            return

        swap = root
        if heap[swap] < heap[child]:
            swap = child

        right = child + 1
        if right < end and heap[swap] < heap[right]:
            swap = right

        if swap == root:
            return

        heap[root], heap[swap] = heap[swap], heap[root]
        root = swap
