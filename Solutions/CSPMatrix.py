from Domain.TileMatrix import TileMatrix
from Utils.CSPSolution import CSPSolution
import datetime as dt
from copy import deepcopy
import networkx as nx

"""
Variables: Tiles on the grid
Variable Domains: Numbers from 1 to n^2
Constraints: The sum on all the lines, columns and both diagonals needs to be equal ( (n * (n^2 + 1) / 2 )
"""


class CSPMatrix:
    def __init__(self, n):
        self.__n = n
        self.__n2 = n * n
        self.__sum = (self.__n * (self.__n2 + 1)) // 2
        self.__domain = [i for i in range(1, self.__n2 + 1)]
        self.__tiles = []
        self.create_tiles()

    def create_tiles(self):
        self.__tiles = [[TileMatrix(-1,-1) for x in range(self.__n)] for y in range(self.__n)]

        for i in range(self.__n):
            for j in range(self.__n):
                t = TileMatrix(i, j)
                t.set_domain(self.__domain)
                self.__tiles[i][j] = t

    def pretty_print(self):
        result = ""
        for i in range(len(self.__tiles)):
            for j in range(len(self.__tiles[i])):
                result = result + str(self.__tiles[i][j].get_value()) + " "

        return result

    def is_valid(self, currentI, currentJ):
        # self.print()

        lineSum = 0
        colSum = 0
        mainSum = 0
        secSum = 0

        onMain = (currentI == currentJ)
        onSec = (currentI + currentJ == self.__n - 1)

        for i in range(self.__n):
            for j in range(self.__n):
                if not self.__tiles[i][j].is_assigned():
                    break

                if (i != currentI or j != currentJ) and \
                        self.__tiles[i][j].get_value() == self.__tiles[currentI][currentJ].get_value():
                    return False

                value = self.__tiles[i][j].get_value()
                if i == currentI:
                    lineSum += value
                if j == currentJ:
                    colSum += value
                if i == j and onMain:
                    mainSum += value
                if i + j == self.__n - 1 and onSec:
                    secSum += value

                if lineSum > self.__sum or colSum > self.__sum or mainSum > self.__sum or secSum > self.__sum:
                    return False

        if currentJ < self.__n - 1 and lineSum >= self.__sum:
            # print("Partial Line >= Sum")
            return False

        if currentJ == self.__n - 1 and lineSum != self.__sum:
            # print("Line != Sum")
            return False

        if currentI < self.__n - 1 and colSum >= self.__sum:
            # print("Partial Col >= Sum")
            return False

        if currentI == self.__n - 1 and colSum != self.__sum:
            # print("Cine != Sum")
            return False

        if onMain:
            if currentI < self.__n - 1 and mainSum >= self.__sum:
                # print("Partial Main Diag >= Sum")
                return False

            if currentI == self.__n - 1 and mainSum != self.__sum:
                # print("Main Diag != Sum")
                return False

        if onSec:
            if currentI < self.__n - 1 and secSum >= self.__sum:
                # print("Partial Sec Diag >= Sum")
                return False

            if currentI == self.__n - 1 and secSum != self.__sum:
                # print("Sec Diag != Sum")
                return False

        return True

    def print(self):
        res = "\n"
        for i in range(self.__n):
            for j in range(self.__n):
                res += str(self.__tiles[i][j])
                res += " "
            res += '\n'
        print(res)

    def is_solution(self, currentI, currentJ):
        return currentI == self.__n - 1 and currentJ == self.__n - 1

    def back(self, maxSolutions):
        currentI = 0
        currentJ = 0
        start = dt.datetime.now()
        solutions = []
        graph = nx.Graph()
        nodes = ["0"]
        prev_node = 0
        graph.add_node("0")

        while currentI > -1:
            chosen = False
            while not chosen and currentI < self.__n and \
                    self.__tiles[currentI][currentJ].can_increment_index():
                self.__tiles[currentI][currentJ].increment_index()
                chosen = self.is_valid(currentI, currentJ)
            if chosen:
                current_node = self.pretty_print()
                if not graph.has_node(current_node):
                    graph.add_node(current_node)
                graph.add_edge(nodes[prev_node], current_node)
                nodes.append(current_node)
                prev_node += 1
                if self.is_solution(currentI, currentJ):
                    sol = CSPSolution(deepcopy(self.__tiles),
                                      (dt.datetime.now() - start).total_seconds(), self.__n, 2)
                    solutions.append(sol)
                    if len(solutions) == maxSolutions:
                        return solutions, graph
                currentJ += 1
                if currentJ == self.__n:
                    currentJ = 0
                    currentI += 1
            else:
                if currentI < self.__n and currentJ < self.__n:
                    self.__tiles[currentI][currentJ].set_current_index(-1)
                currentJ -= 1
                if currentJ == -1:
                    currentJ = self.__n - 1
                    currentI -= 1
                if prev_node != 0:
                    prev_node -= 1

        return solutions, graph
