class TileWithReferences:
    def __init__(self, line, col, n):
        self.__line = line
        self.__col = col
        self.__n = n
        self.__current_index = -1
        self.__domain = []
        self.__line_neighbours = []
        self.__col_neighbours = []
        self.__main_diag_neighbours = []
        self.__sec_diag_neighbours = []

    def get_line_neighbours(self):
        return self.__line_neighbours

    def get_col_neighbours(self):
        return self.__col_neighbours

    def get_main_diag_neighbours(self):
        return self.__main_diag_neighbours

    def get_sec_diag_neighbours(self):
        return self.__sec_diag_neighbours

    def get_line(self):
        return self.__line

    def add_if_neighbour(self, tile):
        linet = tile.get_line()
        colt = tile.get_col()

        if self.__line == linet:
            self.__line_neighbours.append(tile)

        if self.__col == colt:
            self.__col_neighbours.append(tile)

        if self.__line == self.__col and linet == colt:
            self.__main_diag_neighbours.append(tile)

        if self.__line + self.__col == self.__n - 1 and linet + colt == self.__n - 1:
            self.__sec_diag_neighbours.append(tile)


    def get_col(self):
        return self.__col

    def get_value(self):
        return self.__domain[self.__current_index]

    def can_increment_index(self):
        return self.__current_index < len(self.__domain) - 1

    def set_domain(self, domain):
        self.__domain = domain

    def increment_index(self):
        self.__current_index += 1

    def set_current_index(self, index):
        self.__current_index = index

    def get_current_index(self):
        return self.__current_index