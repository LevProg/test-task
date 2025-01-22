# Вопрос №1: Реализация функции определения четности числа

def isEven_mod(value):
    """
    Определение четности с использованием оператора %.
    Плюсы:
        Простота и понятность кода.
        Легко читается и поддерживается.
    Минусы:
        Операция взятия остатка от деления может быть медленнее, чем побитовые операции.
    """
    return value % 2 == 0

def isEven_bit(value):
    """
    Определение четности с использованием побитового оператора &.
    Плюсы:
        Побитовые операции обычно выполняются быстрее, чем арифметические операции.
    Минусы:
        Менее интуитивно понятен для тех, кто не знаком с побитовыми операциями.
        Может быть сложнее для чтения и понимания.
    """
    return (value & 1) == 0

# Вопрос №2: Реализация циклического буфера FIFO

# Реализация 1: Использование списка
class CircularBufferList:
    """
    Реализация циклического буфера на основе списка.
    Плюсы:
        Полный контроль над логикой буфера.
        Понятная и прозрачная реализация.
    Минусы:
        Более сложная реализация с ручным управлением индексами.
        Может быть менее эффективной по сравнению с использованием `deque`.
    """
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.count = 0

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Buffer is full")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Buffer is empty")
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return item

# Реализация 2: Использование deque из collections
from collections import deque

class CircularBufferDeque:
    """
    Реализация циклического буфера на основе `deque`.
    Плюсы:
        Простота реализации благодаря встроенным методам `deque`.
        Высокая производительность, так как `deque` оптимизирован для таких операций.
    Минусы:
        Меньше контроля над внутренней логикой буфера.
        Зависимость от стандартной библиотеки.
    """
    def __init__(self, size):
        self.size = size
        self.buffer = deque(maxlen=size)

    def is_full(self):
        return len(self.buffer) == self.size

    def is_empty(self):
        return len(self.buffer) == 0

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Buffer is full")
        self.buffer.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Buffer is empty")
        return self.buffer.popleft()

# Вопрос №3: Алгоритм сортировки

def fast_sort(arr):
    """
    Реализация быстрой сортировки (Quicksort).
    Плюсы:
        В среднем работает за O(n log n).
        Эффективен для больших массивов.
        Не требует дополнительной памяти
    Минусы:
        В худшем случае (редко) может деградировать до O(n^2).
        Нестабильная сортировка (порядок равных элементов может измениться).
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return fast_sort(left) + middle + fast_sort(right)