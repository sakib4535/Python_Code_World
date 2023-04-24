class ArithmeticProgression:

    def __init__(self, start=0, step=1):
        self._current = start
        self._step = step

    def __next__(self):
        result = self._current
        self._current += self._step
        return result

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))

progression = ArithmeticProgression(start=9, step=2)
progression.print_progression(10)