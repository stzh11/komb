def heapify(arr, n, i):

    largest = i  # Инициализируем текущий узел как наибольший
    left = 2 * i + 1  # Левый потомок
    right = 2 * i + 2  # Правый потомок

    # Проверяем, существует ли левый потомок и больше ли он текущего узла
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Проверяем, существует ли правый потомок и больше ли он текущего узла
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший элемент не текущий узел, меняем их местами и продолжаем heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    """
    Реализация алгоритма Heapsort.
    :param arr: массив для сортировки.
    """
    n = len(arr)

    # Построение кучи (перестройка массива)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        # Перемещаем корень в конец
        arr[0], arr[i] = arr[i], arr[0]
        # Восстанавливаем структуру кучи
        heapify(arr, i, 0)

# Пример использования
weights = [12, 4, 7, 23, 9, 15]
heapsort(weights)
print("Отсортированные веса коробок:", weights)

