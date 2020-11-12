class TileWithSum:
    def __init__(self, line, col, n):
        self.__line = line
        self.__col = col
        self.__n = n
        self.__current_index = -1
        self.__domain = []
        self.__line_neighbour = None
        self.__col_neighbour = None
        self.__main_diag_neighbour = None
        self.__sec_diag_neighbour = None
        self.__line_sum = 0
        self.__col_sum = 0
        self.__main_diag_sum = 0
        self.__sec_diag_sum = 0

    def get_line_sum(self):
        return self.__line_sum

    def get_sol_cum(self):
        return self.__col_sum

    def get_main_diag_sum(self):
        return self.__main_diag_sum

    def get_sec_diag_sum(self):
        return self.__sec_diag_sum

    def get_line(self):
        return self.__line

    def get_col(self):
        return self.__col

    def get_value(self):
        if self.__current_index == -1:
            return -1
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
