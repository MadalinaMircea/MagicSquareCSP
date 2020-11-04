class Tile:
    def __init__(self, line, col):
        self.__line = line
        self.__col = col
        self.__current_index = -1
        self.__domain = []

    def get_line(self):
        return self.__line

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