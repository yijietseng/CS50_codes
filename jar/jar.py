class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Invalid capacity')
        else:
            self._capacity = capacity
            self._size = 0

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        if n > self._capacity:
            raise ValueError('Exceed capacity')
        if self._size + n > self._capacity:
            raise ValueError('Exceed capacity')
        else:
            self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError('n larger than size')
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size