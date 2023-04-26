from abc import ABCMeta, abstractmethod
import math
class LogarithmProblem(metaclass=ABCMeta):

    @abstractmethod
    def solve(self):
        """Solving the problem of logarithmic math"""

class MultiplyLogarithmicProblem(LogarithmProblem):
    """ Class representing a logarithmic math problme """

    def __init__(self, base, x, y):
        self.base = base
        self.x = x
        self.y = y

    def solve(self):
        return math.log10(self.x) + math.log10(self.y)

class DivideLogarithmicProblem(LogarithmProblem):
    """Class representing a logarithmic math problem using division"""

    def __init__(self, base, x, y):
        self.base = base
        self.x = x
        self.y = y

    def solve(self):
        return math.log10(self.x) - math.log10(self.y)



log_problem = MultiplyLogarithmicProblem(10, 100, 1000)
print(log_problem.solve())  

log_problem = DivideLogarithmicProblem(10, 1000, 100)
print(log_problem.solve())