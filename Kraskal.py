class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Количество вершин
        self.graph = []    # Список рёбер

    def add_edge(self, u, v, w):
        self.graph.append((w, u, v))

    def find_parent(self, parent, i):
        # Метод нахождения родителя вершины
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        # Метод объединения двух подмножеств
        xroot = self.find_parent(parent, x)
        yroot = self.find_parent(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []  # Хранит минимальное остовное дерево
        i = 0  # Индекс для рёбер
        e = 0  # Индекс для результата

        # Шаг 1: Сортируем рёбра по весу
        self.graph.sort()

        parent = []
        rank = []

        # Создаём подмножества для каждой вершины
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Шаг 2: Обрабатываем рёбра
        while e < self.V - 1 and i < len(self.graph):
            # Наименьшее ребро
            w, u, v = self.graph[i]
            i += 1

            # Получаем индексы для текущих вершин
            x = self.find_parent(parent, ord(u) - ord('A'))
            y = self.find_parent(parent, ord(v) - ord('A'))

            # Если они не находятся в одном множестве, добавляем это ребро в результат
            if x != y:
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)

        # Печатаем рёбра минимального остовного дерева
        print("Минимальное остовное дерево:")
        for u, v, weight in result:
            print(f"{u} - {v}: {weight}")
        total_weight = sum(weight for _, _, weight in result)
        print(f"Общий вес минимального остовного дерева: {total_weight}")


# Пример использования
g = Graph(5)
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 4)
g.add_edge('C', 'D', 5)

g.kruskal()
