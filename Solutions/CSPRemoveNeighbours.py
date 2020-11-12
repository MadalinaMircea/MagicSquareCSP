from Domain.TileRemoveNeighbours import TileRemoveNeighbours
from Utils.CSPSolution import CSPSolution
import datetime as dt
from copy import deepcopy
import networkx as nx

"""
Variables: Tiles on the grid
Variable Domains: Numbers from 1 to n^2
Constraints: The sum on all the lines, columns and both diagonals needs to be equal ( (n * (n^2 + 1) / 2 )
"""
class CSPRemoveNeighbours:
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
                t = TileRemoveNeighbours(i, j, self.__n)
                t.set_domain(self.__domain)
                self.__tiles.append(t)

        for i in range(len(self.__tiles)):
            for j in range(len(self.__tiles)):
                if i != j:
                    self.__tiles[i].add_if_neighbour(self.__tiles[j])

    def assign_tile(self, currentPos):
        prev_val, current_val = self.__tiles[currentPos].increment_index()
        if not self.is_valid(currentPos):
            return False

        for c in self.__tiles:
            if c != self.__tiles[currentPos]:
                if not c.is_assigned():
                    c.remove_from_domain(current_val)
                    if prev_val is not None:
                        c.add_to_domain(prev_val)
                    if c.empty_domain():
                        return False

        return True

    def reset_tiles(self, currentPos):
        for c in self.__tiles[:currentPos]:
            c.add_to_domain(self.__tiles[currentPos].get_value())
        self.__tiles[currentPos].reset_current_index()

    def is_valid(self, currentPos):
        # for i in range(currentPos):
        #     if self.__tiles[i].get_value() == self.__tiles[currentPos].get_value():
        #         return False

        line = self.__tiles[currentPos].get_line()
        col = self.__tiles[currentPos].get_col()

        lineSum = self.__tiles[currentPos].get_value()
        colSum = lineSum
        mainSum = lineSum
        secSum = lineSum

        for x in self.__tiles[currentPos].get_line_neighbours():
            if x.get_current_index() != -1:
                lineSum += x.get_value()

        if col < self.__n - 1 and lineSum >= self.__sum:
            print("Line sum >=")
            return False

        if col == self.__n - 1 and lineSum != self.__sum:
            print("Line sum !=")
            return False

        for x in self.__tiles[currentPos].get_col_neighbours():
            if x.get_current_index() != -1:
                colSum += x.get_value()

        if line < self.__n - 1 and colSum >= self.__sum:
            print("Col sum >=")
            return False

        if line == self.__n - 1 and colSum != self.__sum:
            print("Col sum !=")
            return False

        if line == col:
            for x in self.__tiles[currentPos].get_main_diag_neighbours():
                if x.get_current_index() != -1:
                    mainSum += x.get_value()

            if line < self.__n - 1 and mainSum >= self.__sum:
                print("Main diag sum >=")
                return False

            if line == self.__n - 1 and mainSum != self.__sum:
                print("Main diag sum !=")
                return False

        if line + col == self.__n - 1:
            for x in self.__tiles[currentPos].get_sec_diag_neighbours():
                if x.get_current_index() != -1:
                    secSum += x.get_value()

            if line < self.__n - 1 and secSum >= self.__sum:
                print("Sec diag sum >=")
                return False

            if line == self.__n - 1 and secSum != self.__sum:
                print("Sec diag sum !=")
                return False

        return True

    def is_solution(self, currentPos):
        return currentPos == len(self.__tiles) - 1

    def pretty_print(self):
        result = ""
        for t in self.__tiles:
            result = result + str(t.get_value()) + " "

        return result

    def back(self, maxSolutions):
        currentPos = 0
        start = dt.datetime.now()
        solutions = []
        graph = nx.Graph()
        nodes = ["0"]
        prev_node = 0
        graph.add_node("0")

        while currentPos > -1:
            chosen = False
            while not chosen and currentPos < len(self.__tiles) and \
                    self.__tiles[currentPos].can_increment_index():
                chosen = self.assign_tile(currentPos)
            if chosen:
                print(self.pretty_print())
                current_node = self.pretty_print()
                if not graph.has_node(current_node):
                    graph.add_node(current_node)
                graph.add_edge(nodes[prev_node], current_node)
                nodes.append(current_node)
                prev_node += 1
                if self.is_solution(currentPos):
                    sol = CSPSolution(deepcopy(self.__tiles),
                                                 (dt.datetime.now() - start).total_seconds(), self.__n)
                    solutions.append(sol)
                    if len(solutions) == maxSolutions:
                        return solutions, graph
                currentPos += 1
            else:
                self.reset_tiles(currentPos)
                if currentPos < len(self.__tiles):
                    self.reset_tiles(currentPos)
                currentPos -= 1
                if prev_node != 0:
                    prev_node -= 1

        return solutions, graph
