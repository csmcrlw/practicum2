from abc import ABC, abstractmethod
from typing import List


# Класс стратегии сортировки
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        pass


# Класс конкретной стратегии (сортировка пузырьком)
class BubbleSort(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        return sorted(data)


# Класс конкретной стратегии (быстрая сортировка)
class QuickSort(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return QuickSort().sort(left) + middle + QuickSort().sort(right)


# Класс конкретной стратегии (сортировка слиянием)
class MergeSort(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data
        middle = len(data) // 2
        left = MergeSort().sort(data[:middle])
        right = MergeSort().sort(data[middle:])
        return MergeSort().merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        if left:
            result.extend(left)
        if right:
            result.extend(right)
        return result


# Класс интерфейса
class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self._strategy = strategy

    def sort(self, data: List[int]) -> List[int]:
        return self._strategy.sort(data)


# Пример использования
if __name__ == "__main__":
    data = [5, 2, 7, 1, 9, 3]

    bubble_sort_strategy = BubbleSort()
    quick_sort_strategy = QuickSort()
    merge_sort_strategy = MergeSort()

    sorter = Sorter(bubble_sort_strategy)
    sorted_data = sorter.sort(data)
    print("Bubble Sort Result:", sorted_data)

    sorter.set_strategy(quick_sort_strategy)
    sorted_data = sorter.sort(data)
    print("Quick Sort Result:", sorted_data)

    sorter.set_strategy(merge_sort_strategy)
    sorted_data = sorter.sort(data)
    print("Merge Sort Result:", sorted_data)
