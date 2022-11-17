import sys


class Matrix:
    def __init__(self):
        self.size = 0
        self.out_type = 0

    def read_from(self, stream):
        try:
            self.size = int(stream.readline().rstrip('\n'))
        except Exception:
            print('Reading size error')
            stream.close()
            sys.exit(1)
        try:
            self.out_type = int(stream.readline().rstrip('\n'))
        except Exception:
            print('Reading out type error')
            stream.close()
            sys.exit(1)

    def write_to(self, stream):
        try:
            stream.write(f'\tSize: {self.size}\n')
            stream.write(f'\t\tOutput type: {self.out_type}\n')
        except Exception:
            print('Writing to file error')
            stream.close()
            sys.exit(1)

    @staticmethod
    def create_from(stream, line):
        try:
            k = int(line)
        except Exception:
            print('Conversion to int error')
            stream.close()
            sys.exit(1)

        if k == 1:
            matrix = TwoDimArray()
        elif k == 2:
            matrix = Diagonal()
        elif k == 3:
            matrix = Triangle()
        else:
            stream.close()
            raise Exception('Error type')

        matrix.read_from(stream)
        return matrix

    def sum(self):
        try:
            s = 0
            for item in self.data:
                if isinstance(item, int):
                    s += item
                else:
                    s += sum(item)
            return s
        except Exception:
            print('Sum calculation error')

    def compare(self, other):
        return self.sum() < other.sum()

    def write_two_dim_array_to(self, stream):
        pass

    @staticmethod
    def check_matrices(matrix_1, matrix_2):
        match matrix_1, matrix_2:
            case TwoDimArray(), TwoDimArray():
                print("Matrices are the same type: TwoDimArray and TwoDimArray")

            case TwoDimArray(), Diagonal():
                print("Matrices are different type: TwoDimArray and Diagonal")

            case TwoDimArray(), Triangle():
                print("Matrices are different type: TwoDimArray and Triangle")

            case Diagonal(), TwoDimArray():
                print("Matrices are different type: Diagonal and TwoDimArray")

            case Diagonal(), Diagonal():
                print("Matrices are the same type: Diagonal and Diagonal")

            case Diagonal(), Triangle():
                print("Matrices are different type: Diagonal and Triangle")

            case Triangle(), TwoDimArray():
                print("Matrices are different type: Triangle and TwoDimArray")

            case Triangle(), Diagonal():
                print("Matrices are different type: Triangle and Diagonal")

            case Triangle(), Triangle():
                print("Matrices are the same type: Triangle and Triangle")

            case _:
                print('Unknown type')
                return

        print(f"First: {matrix_1}, second: {matrix_2}")
        print()


class TwoDimArray(Matrix):
    def __init__(self):
        super().__init__()
        self.data = []

    def read_from(self, stream):
        super().read_from(stream)
        try:
            for i in range(self.size):
                line = stream.readline().rstrip('\n')
                self.data.append(list(map(lambda x: int(x), line.split())))
        except Exception:
            print('Reading two-dimensional array from file error')
            stream.close()
            sys.exit(1)

    def write_to(self, stream):
        stream.write('\tThis is two-dimensional array\n')
        stream.write(f'\tSum: {self.sum()}\n')
        try:
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
        except Exception:
            print('Writing two-dimensional array to file error')
            stream.close()
            sys.exit(1)

        super().write_to(stream)

    def write_two_dim_array_to(self, stream):
        try:
            self.write_to(stream)
        except Exception:
            print('Writing two-dimensional array to file error')
            stream.close()
            sys.exit(1)


class Diagonal(Matrix):
    def __init__(self):
        super().__init__()
        self.data = None

    def read_from(self, stream):
        try:
            super().read_from(stream)
            self.data = list(map(lambda x: int(x), stream.readline().rstrip('\n').split()))
        except Exception:
            print('Reading diagonal matrix from file error')
            stream.close()
            sys.exit(1)

    def write_to(self, stream):
        try:
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
        except Exception:
            print('Writing diagonal matrix to file error')
            stream.close()
            sys.exit(1)


class Triangle(Matrix):
    def __init__(self):
        super().__init__()
        self.data = []

    def read_from(self, stream):
        try:
            super().read_from(stream)
            self.data = list(map(lambda x: int(x), stream.readline().rstrip('\n').split()))
        except Exception:
            print('Reading triangle matrix from file error')
            stream.close()
            sys.exit(1)

    def write_to(self, stream):
        stream.write('\tThis is triangle matrix\n')
        stream.write(f'\tSum: {self.sum()}\n')

        try:
            if self.out_type == 1 or self.out_type == 2:
                stream.write('\t\t')
                index = 0
                for i in range(self.size):
                    for j in range(self.size):
                        if j >= i:
                            stream.write(str(self.data[index]) + ' ')
                            index += 1
                        else:
                            stream.write('0 ')
                    stream.write('\n\t\t')

            elif self.out_type == 3:
                stream.write('\t\t')
                for i in range(self.size):
                    for j in range(self.size):
                        stream.write('{} '.format(self.data[i] if i == j else 0))
            else:
                stream.write('\tError matrix output type\n')

            super().write_to(stream)
        except Exception:
            print('Writing triangle matrix to file error')
            stream.close()
            sys.exit(1)

