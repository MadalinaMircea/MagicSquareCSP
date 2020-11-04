from Tile import Tile
from CSPSolution import CSPSolution
import datetime as dt
from copy import deepcopy

"""
Variables: Tiles on the grid
Variable Domains: Numbers from 1 to n^2
Constraints: The sum on all the lines, columns and both diagonals needs to be equal ( (n * (n^2 + 1) / 2 )
"""
class CSPBacktracking:
    def __init__(self, n):
        self.__n = n
        self.__n2 = n * n
        self.__sum = (self.__n * (self.__n2 + 1)) / 2
        self.__domain = [i for i in range(1, self.__n2 + 1)]
        self.__tiles = []
        self.create_tiles()

    def create_tiles(self):
        for i in range(self.__n):
            for j in range(self.__n):
                t = Tile(i, j)
                t.set_domain(self.__domain)
                self.__tiles.append(t)

    def is_valid(self, currentPos):
        for i in range(currentPos):
            if self.__tiles[i].get_value() == self.__tiles[currentPos].get_value():
                return False

        line = self.__tiles[currentPos].get_line()
        col = self.__tiles[currentPos].get_col()

        lineSum = self.__tiles[currentPos].get_value()
        colSum = lineSum
        mainSum = lineSum
        secSum = lineSum

        for k in range(currentPos):
            lineK = self.__tiles[k].get_line()
            colK = self.__tiles[k].get_col()

            if lineK == line:
                lineSum += self.__tiles[k].get_value()

            if colK == col:
                colSum += self.__tiles[k].get_value()

            if line == col and lineK == colK:
                mainSum += self.__tiles[k].get_value()

            if line + col == self.__n - 1 and lineK + colK == self.__n - 1:
                secSum += self.__tiles[k].get_value()

            if lineSum > self.__sum or colSum > self.__sum or mainSum > self.__sum or secSum > self.__sum:
                return False

        if col < self.__n - 1 and lineSum >= self.__sum:
            return False

        if col == self.__n - 1 and lineSum != self.__sum:
            return False

        if line < self.__n - 1 and colSum >= self.__sum:
            return False

        if line == self.__n - 1 and colSum != self.__sum:
            return False

        if line == col:
            if line < self.__n - 1 and mainSum >= self.__sum:
                return False

            if line == self.__n - 1 and mainSum != self.__sum:
                return False

        if line + col == self.__n - 1:
            if line < self.__n - 1 and secSum >= self.__sum:
                return False

            if line == self.__n - 1 and secSum != self.__sum:
                return False
        
        return True

    def is_solution(self, currentPos):
        return currentPos == len(self.__tiles) - 1

    def back(self, maxSolutions):
        currentPos = 0
        start = dt.datetime.now()
        solutions = []

        while currentPos > -1:
            chosen = False
            while not chosen and currentPos < len(self.__tiles) and \
                    self.__tiles[currentPos].can_increment_index():
                self.__tiles[currentPos].increment_index()
                chosen = self.is_valid(currentPos)
            if chosen:
                if self.is_solution(currentPos):
                    sol = CSPSolution(deepcopy(self.__tiles),
                                                 (dt.datetime.now() - start).total_seconds(), self.__n)
                    solutions.append(sol)
                    yield sol
                    if len(solutions) == maxSolutions:
                        return solutions
                currentPos += 1
            else:
                if currentPos < len(self.__tiles):
                    self.__tiles[currentPos].set_current_index(-1)
                currentPos -= 1

        return solutions
