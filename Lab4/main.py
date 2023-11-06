def copy_element(element):
    if isinstance(element, dict):
        copy_dict = {}
        for key in element:
            copy_dict[key] = copy_element(element[key])
        return copy_dict

    elif isinstance(element, list):
        copy_list = []
        for item in element:
            copy_list.append(copy_element(item))
        return copy_list

    elif isinstance(element, set):
        copy_set = {}
        for item in element:
            copy_set.add(copy_element(item))
        return copy_set

    elif isinstance(element, tuple):
        copy_tuple = []
        for item in element:
            copy_tuple.append(copy_element(item))
        return tuple(copy_tuple)

    else:
        return element

class Stack:
    def __init__(self) -> None:
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        length = len(self.elements)
        if length == 0:
            return None
        else:
            element = self.elements[length - 1]
            del self.elements[length - 1]
            return element

    def peek(self):
        if len(self.elements) == 0:
            return None
        return copy_element(self.elements[len(self.elements) - 1])

class Queue:
    def __init__(self) -> None:
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if len(self.elements) == 0:
            return None
        else:
            element = self.elements[0]
            del self.elements[0]
            return element

    def peek(self):
        if len(self.elements) == 0:
            return None
        return copy_element(self.elements[0])

class Matrix:
    def __init__(self, lines, cols) -> None:
        if lines <= 0 or cols <= 0:
            return "Error: Please input a valid number of lines and columns"

        self.matrix = [[None for i in range(cols)] for j in range(lines)]
        self.lines = lines
        self.cols = cols

    def get_element(self, line, col):
        if 0 <= line <= self.lines - 1 and 0 <= col <= self.cols - 1:
            return self.matrix[line][col]
        else:
            return "Error: Index out of bounds"

    def set_element(self, line, col, content):
        if 0 <= line <= self.lines - 1 and 0 <= col <= self.cols - 1:
            self.matrix[line][col] = content
        else:
            return "Error: Index out of bounds"

    def transpose(self):
        self.matrix = [[self.matrix[i][j] for j in range(self.lines)] for i in range(self.cols)]
        self.lines, self.cols = self.cols, self.lines

    def multiply_by_number(self, number):
        #only for integers or floats
        ok = True
        for i in range(self.lines):
            for j in range(self.cols):
                if not(isinstance(self.matrix[i][j], int) or isinstance(self.matrix[i][j], float)):
                    ok = False
                    break

        if not ok:
            return "Error: Incompatible types"

        for i in range(self.lines):
            for j in range(self.cols):
                self.matrix[i][j] = self.matrix[i][j] * number

    def multiply_by_matrix(self, matrix2):
        #only for integers or floats
        ok = True
        for i in range(self.lines):
            for j in range(self.cols):
                if not(isinstance(self.matrix[i][j], int) or isinstance(self.matrix[i][j], float)):
                    ok = False
                    break

        if not ok:
            return "Error: Incompatible types"

        if len(self.matrix[0]) != len(matrix2):
            return "Error: Invalid dimensions"

        result = [[0 for i in range(len(matrix2[0]))] for j in range(self.lines)]
        for i in range(self.lines):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j] += self.matrix[i][k] * matrix2[k][j]

        self.matrix = result
        self.lines = len(result)
        self.cols = len(result[0])

    def transform(self, function):
        for i in range(self.lines):
            for j in range(self.cols):
                self.matrix[i][j] = function(self.matrix[i][j])

    def printMatrix(self):
        for i in range(self.lines):
            for j in range(self.cols):
                print(self.matrix[i][j], end=" ")
            print()

def main():
    # # # # # # # #ex1
    # s = Stack()
    # s.push(1)
    # s.push(2)
    # s.push(3)
    # s.push(4)
    # s.push(5)
    # s.push(6)
    # print(s.pop())
    # print(s.peek())

    # # # # # # # #ex2
    # q = Queue()
    # q.push(1)
    # q.push(2)
    # q.push(3)
    # q.push(4)
    # q.push(5)
    # q.push(6)
    # print(q.pop())
    # print(q.peek())

    #ex3
    m = Matrix(2, 3)
    m.set_element(1, 2, "ceva")
    print(m.get_element(1, 2))

    m.set_element(0, 0, 1)
    m.set_element(0, 1, 2)
    m.set_element(0, 2, 3)
    m.set_element(1, 0, 4)
    m.set_element(1, 1, 5)
    m.set_element(1, 2, 6)

    m.printMatrix()
    print()

    m.multiply_by_number(2)
    m.printMatrix()
    print()

    m2 = [[7, 8], [9, 10], [11, 12]]
    m.multiply_by_matrix(m2)
    m.printMatrix()
    print()

    m.transform(lambda x: "This cell contains: \"" + str(x) + "\"")
    m.printMatrix()

if __name__ == "__main__":
    main()