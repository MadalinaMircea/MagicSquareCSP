import datetime as dt


class Backtracking:
    def __init__(self, n):
        self.n = n

    def get_x(self, index):
        return index // self.n

    def get_y(self, index):
        return index % self.n

    """
    Check if the last added number is valid for a candidate solution
    In this case, it is valid if it is different than the other
    values in the vector and if the sums on the lines, columns
    and diagonals are smaller or equal to the desired sum.
    The sum of all of the elements in the matrix is (n^2 * (n^2 + 1)) / 2
    and it is equal on all the (i.e.) lines, so the desired sum per lines
    is (n * (n^2 + 1) / 2)
    """
    def is_valid(self, candidate, desired):
        for x in candidate[:-1]:
            if x == candidate[-1]:
                return False

        line = self.get_x(len(candidate) - 1)
        col = self.get_y(len(candidate) - 1)

        lineSum = candidate[-1]
        colSum = candidate[-1]
        mainSum = candidate[-1]
        secSum = candidate[-1]

        for k in range(len(candidate) - 1):
            lineK = self.get_x(k)
            colK = self.get_y(k)

            if lineK == line:
                lineSum += candidate[k]

            if colK == col:
                colSum += candidate[k]

            if line == col and lineK == colK:
                mainSum += candidate[k]

            if line + col == self.n - 1 and lineK + colK == self.n - 1:
                secSum += candidate[k]

            if lineSum > desired or colSum > desired or mainSum > desired or secSum > desired:
                return False

        if col < self.n - 1 and lineSum >= desired:
            return False

        if col == self.n - 1 and lineSum != desired:
            return False

        if line < self.n - 1 and colSum >= desired:
            return False

        if line == self.n - 1 and colSum != desired:
            return False

        if line == col:
            if line < self.n - 1 and mainSum >= desired:
                return False

            if line == self.n - 1 and mainSum != desired:
                return False

        if line + col == self.n - 1:
            if line < self.n - 1 and secSum >= desired:
                return False

            if line == self.n - 1 and secSum != desired:
                return False

        # # parse the column
        # sum = candidate[-1]
        # for i in range(line):
        #     sum += candidate[i * self.n + col]
        #
        # if sum > desired:
        #     return False
        #
        # if line == self.n - 1 and sum != desired:
        #     return False
        #
        # # parse the line
        # sum = candidate[-1]
        # for i in range(col):
        #     sum += candidate[line * self.n + i]
        #
        # if sum > desired:
        #     return False
        #
        # if col == self.n - 1 and sum != desired:
        #     return False
        #
        # # parse the main diagonal
        # if line == col:
        #     sum = candidate[-1]
        #     for i in range(line):
        #         sum += candidate[i * self.n + i]
        #
        #     if sum > desired:
        #         return False
        #
        #     if line == self.n - 1 and sum != desired:
        #         return False
        #
        # # parse the secondary diagonal
        # if line + col == self.n - 1:
        #     sum = candidate[-1]
        #     for i in range(line):
        #         sum += candidate[i * self.n + (self.n - i - 1)]
        #
        #     if sum > desired:
        #         return False
        #
        #     if line == self.n - 1 and sum != desired:
        #         return False

        return True

    """
    Check if a candidate is a valid solution
    In this case, it is a solution if the length is
    equal to n^2
    """
    def is_solution(self, candidate):
        return len(candidate) == self.n * self.n

    def pretty_print(self, solution):
        result = ""
        for i in range(len(solution)):
            if i % self.n == 0:
                result += '\n'
            result += str(solution[i])
            result += ' '

        print(result)

    """
    Iterative backtracking method
    We represent the matrix as a vector for the backtracking
    method and use the methods getX and getY to obtain
    the corresponding index in the matrix
    """
    def back(self):
        start = dt.datetime.now()
        candidate = [0]
        desired_sum = (self.n * (self.n * self.n + 1)) / 2
        k = 0

        while len(candidate) > 0:

            chosen = False
            while not chosen and candidate[-1] < self.n * self.n:
                candidate[-1] += 1
                chosen = self.is_valid(candidate, desired_sum)
            if chosen:
                if self.is_solution(candidate):
                    print((dt.datetime.now() - start).total_seconds())
                    self.pretty_print(candidate)
                    k+=1
                    if k == 10:
                        break
                candidate.append(0)
            else:
                candidate = candidate[:-1]
