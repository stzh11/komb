class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Количество вершин
        self.edges = []    # Список рёбер

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))  # Добавление ребра в граф

    def bellman_ford(self, start):
        # Шаг 1: Инициализация расстояний
        distances = [float('inf')] * self.V
        distances[start] = 0

        # Шаг 2: Основной цикл алгоритма
        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

        # Шаг 3: Проверка на отрицательные циклы
        for u, v, weight in self.edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                print("Граф содержит отрицательный цикл!")
                return

        return distances


# Пример использования
if __name__ == "__main__":
    g = Graph(4)  # 4 города: A, B, C, D (0, 1, 2, 3)
    g.add_edge(0, 1, 4)  # A - B
    g.add_edge(0, 2, 1)  # A - C
    g.add_edge(1, 2, -3) # B - C
    g.add_edge(1, 3, 2)  # B - D
    g.add_edge(2, 3, 5)  # C - D

    start_city = 0  # Начинаем с города A
    distances = g.bellman_ford(start_city)

    if distances:
        print("Кратчайшие расстояния от города A до остальных:")
        for i in range(len(distances)):
            print(f"Расстояние до города {i}: {distances[i]}")
