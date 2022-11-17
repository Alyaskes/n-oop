class Matrix:
    def __init__(self):
        self.size = 0
        self.out_type = 0

    def read_from(self, stream):
        self.size = int(stream.readline().rstrip('\n'))
        self.out_type = int(stream.readline().rstrip('\n'))

    def write_to(self, stream):
        stream.write(f'\tSize: {self.size}\n')
        stream.write(f'\t\tOutput type: {self.out_type}\n')

    def sum(self):
        s = 0
        for item in self.data:
            if isinstance(item, int):
                s += item
            else:
                s += sum(item)
        return s

    @staticmethod
    def create_from(stream, line):
        k = int(line)

        if k == 1:
            matrix = TwoDimArray()
        elif k == 2:
            matrix = Diagonal()
        else:
            stream.close()
            raise Exception('Error type')

        matrix.read_from(stream)
        return matrix

    def sum(self):
        s = 0
        for item in self.data:
            if isinstance(item, int):
                s += item
            else:
                s += sum(item)
        return s

    def compare(self, other):
        return self.sum() < other.sum()

<<<<<<< HEAD
=======
    def write_two_dim_array_to(self, stream):
        pass

>>>>>>> filter-out

class TwoDimArray(Matrix):
    def __init__(self):
        super().__init__()
        self.data = []

    def read_from(self, stream):
        super().read_from(stream)
        for i in range(self.size):
            line = stream.readline().rstrip('\n')
            self.data.append(list(map(lambda x: int(x), line.split())))

    def write_to(self, stream):
        stream.write('\tThis is two-dimensional array\n')
        stream.write(f'\tSum: {self.sum()}\n')

        if self.out_type == 1:
            stream.write('\t\t')
            for i in range(self.size):
                for j in range(self.size):
                    stream.write(f'{self.data[i][j]} ')
                stream.write('\n\t\t')

        elif self.out_type == 2:
            stream.write('\t\t')
            for i in range(self.size):
                for j in range(self.size):
                    stream.write(f'{self.data[j][i]} ')
                stream.write('\n\t\t')

        elif self.out_type == 3:
            stream.write('\t\t')
            for i in range(self.size):
                for j in range(self.size):
                    stream.write(f'{self.data[i][j]} ')
            stream.write('\n\t\t')
        else:
            stream.write('\tError matrix output type\n')

        super().write_to(stream)

    def write_two_dim_array_to(self, stream):
        self.write_to(stream)


class Diagonal(Matrix):
    def __init__(self):
        super().__init__()
        self.data = None

    def read_from(self, stream):
        super().read_from(stream)
        self.data = list(map(lambda x: int(x), stream.readline().rstrip('\n').split()))

    def write_to(self, stream):
        stream.write('\tThis is diagonal matrix\n')
        stream.write(f'\tSum: {self.sum()}\n')

        if self.out_type == 1 or self.out_type == 2:
            stream.write('\t\t')
            for i in range(self.size):
                for j in range(self.size):
                    stream.write('{} '.format(self.data[i] if i == j else 0))
                stream.write('\n\t\t')

        elif self.out_type == 3:
            stream.write('\t\t')
            for i in range(self.size):
                for j in range(self.size):
                    stream.write('{} '.format(self.data[i] if i == j else 0))
            stream.write('\n\t\t')
        else:
            stream.write('\tError matrix output type\n')

        super().write_to(stream)
