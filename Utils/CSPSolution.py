class CSPSolution:
    def __init__(self, tiles, timestamp, n, dimensions):
        self.__tiles = tiles
        self.__timestamp = timestamp
        self.__n = n
        self.__dimensions = dimensions

    def get_tiles(self):
        return self.__tiles

    def get_timestamp(self):
        return self.__timestamp

    def __str__(self):
        matrix = [[-1 for x in range(self.__n)] for y in range(self.__n)]

        if self.__dimensions == 1:
            for p in self.__tiles:
                matrix[p.get_line()][p.get_col()] = p.get_value()
        else:
            for i in range(self.__n):
                for j in range(self.__n):
                    matrix[i][j] = self.__tiles[i][j].get_value()

        result = str(self.__timestamp) + '\n'

        for i in range(self.__n):
            for j in range(self.__n):
                result += str(matrix[i][j])
                result += '\t'
            result += '\n'

        return result