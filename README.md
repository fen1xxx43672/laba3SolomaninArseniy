# Реализация очереди через два стека

Данный проект представляет собой эффективную реализацию структуры данных **Очередь (Queue)** на языке Python, построенную с использованием двух **Стеков (Stack)**.

## Описание логики

Очередь работает по принципу **FIFO** (First In, First Out), а стек — по принципу **LIFO** (Last In, First Out). Чтобы получить поведение очереди, мы используем два списка:

1.  **`stack_in`**: Принимает все новые элементы при вызове `enqueue`.
2.  **`stack_out`**: Служит для выдачи элементов. Элементы попадают сюда из первого стека только тогда, когда этот стек пуст.

**Суть метода:** При перекладывании элементов из одного стека в другой их порядок инвертируется. Таким образом, самый "старый" элемент оказывается на вершине второго стека и извлекается первым.

---

## Основные методы

*   `enqueue(value)` — добавляет элемент в конец очереди (с проверкой на лимит `max_size`).
*   `dequeue()` — удаляет и возвращает первый элемент.
*   `front()` — возвращает значение первого элемента без удаления.
*   `size()` — возвращает общее количество элементов в двух стеках.
*   `is_empty()` — проверяет, пуста ли очередь.

---

## Исходный код
```python
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
