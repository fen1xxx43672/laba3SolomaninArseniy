class QueueWithStacks:
    def __init__(self, max_size):
        # Инициализация двух стеков и максимального размера
        self.stack_in = []
        self.stack_out = []
        self.max_size = max_size

    def enqueue(self, value):
        """Добавление элемента в конец очереди"""
        if self.size() >= self.max_size:
            print("Очередь переполнена")
            return
        self.stack_in.append(value)

    def dequeue(self):
        """Извлечение первого элемента"""
        if self.is_empty():
            print("Очередь пуста")
            return None
        self._move_elements()
        return self.stack_out.pop()

    def front(self):
        """Просмотр первого элемента"""
        if self.is_empty():
            print("Очередь пуста")
            return None
        self._move_elements()
        return self.stack_out[-1]

    def _move_elements(self):
        """Внутренняя логика перекладывания данных между стеками"""
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

    def is_empty(self):
        return len(self.stack_in) == 0 and len(self.stack_out) == 0

    def size(self):
        return len(self.stack_in) + len(self.stack_out)

# --- Пример использования ---
queue = QueueWithStacks(max_size=3)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(f"Первый элемент: {queue.front()}")   # 10
print(f"Удален элемент: {queue.dequeue()}") # 10
print(f"Текущий размер: {queue.size()}")    # 2
