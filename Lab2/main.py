from itertools import zip_longest


def ex1_classic(n):
    l = list()
    a = 1
    b = 1

    for i in range(n):
        #print(a)
        l.append(a)
        aux = a
        a = b
        b = b + aux

    return l

#max(n) = 994
def ex1_rec(n, a = 1, b = 1, count = 0):
    if count < n:
        print(a, end=" ")
        ex1_rec(n, b, a + b, count + 1)

def ex2(number_list):
    return [number_list[i] for i in range(2,len(number_list)) if len(list(j for j in range(2, number_list[i] // 2+1) if number_list[i] % j == 0)) == 0]

def ex3(a_list, b_list):
    intersection = []
    for x in a_list:
        if x in b_list:
            intersection.append(x)

    union = a_list.copy()
    for x in b_list:
        if x not in a_list:
            union.append(x)

    dif_a_b = []
    for x in a_list:
        if x not in b_list:
            dif_a_b.append(x)

    dif_b_a = []
    for x in b_list:
        if x not in a_list:
            dif_b_a.append(x)

    return intersection, union, dif_a_b, dif_b_a

def ex4(notes, moves, start):
    index = start % len(notes)
    result = []
    result.append(notes[index])

    for move in moves:
        index = (index + move) % len(notes)
        result.append(notes[index])

    return result

def ex5(matrix):
    #check if we have a square matrix
    for row in matrix:
        if len(row) != len(matrix):
            print("Error! Please input a square matrix")
            return None

    #initialize the result matrix
    result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if i > j:
                result[i][j] = 0
            else:
                result[i][j] = matrix[i][j]

    return result

def ex6(x, *args):
    result = []

    lists = []
    for lst in args:
        lists += lst

    list_set = set(lists)
    for element in list_set:
        if lists.count(element) == x:
            result.append(element)

    return result

def ex7(num_list):

    #function taken from Lab1 (Ex 6)
    def is_palindrome(number):
        length = len(number)
        for i in range(length//2):
            if number[i] != number[length - 1 - i]:
                return False

        return True

    count = 0
    greatest = -1

    for element in num_list:
        if is_palindrome(str(element)):
            count += 1
            if greatest == -1 or element > greatest:
                greatest = element

    return (count, greatest)

def ex8(str_list, x=1, flag=True):
    index = 0
    result = []

    if flag:
        for string in str_list:
            #check each character
            chars = []
            for char in string:
                if ord(char) % x == 0:
                    chars += char

            result.append("ceva")
            result[index] = chars
            index += 1
    else:
        for string in str_list:
            #check each character
            chars = []
            for char in string:
                if ord(char) % x != 0:
                    chars += char

            result.append("ceva")
            result[index] = chars
            index += 1

    return result

def ex9(matrix):
    result = []
    result_index = 0
    row = matrix[0]

    # for each column iterate form the top to the bottom
    for column in range(len(row)):
        current_greatest = matrix[0][column]
        for line in range(len(matrix)):
            if matrix[line][column] > current_greatest:
                current_greatest = matrix[line][column]

            #program will only account for *taller* persons that the tallest found yet
            elif matrix[line][column] < current_greatest:
                result.append("ceva")
                result[result_index] = (line, column)
                result_index += 1

    return result

def ex10(*args):
    result = list(zip_longest(*args))
    return result

def ex11(lst):
    def compare_function(tpl):
        if len(tpl) > 1 and len(tpl[1]) > 2:
            return tpl[1][2]

    result = sorted(lst, key=compare_function)
    return result

def ex12(lst):
    #remove all the words that have the length less than 2
    words = list(filter(lambda element: len(element) >= 2, lst))

    result = []
    index = 0

    #compare the elements two by two
    while len(words) != 0:
        w = words[0]
        words.remove(w)
        word_list = []
        word_list.append(w)

        for word in words:
            if w[-2:] == word[-2:]:
                word_list.append(word)
                words.remove(word)

        result.append("ceva")
        result[index] = word_list
        index += 1

    return result

def main():
    
    #n = int(input("Number of elements: ").strip())
    #ex1_classic()
    #ex1_rec(n)

    # ex2_list = ex2([0])
    # print(ex2_list)

    ex3_a_list = [1, 2, 3, 4, 5]
    ex3_b_list = [3, 4, 5, 6, 7]
    intersection, union, dif_a_b, dif_b_a = ex3(ex3_a_list, ex3_b_list)
    print("A intersected with B: ", intersection)
    print("A reunited with B: ", union)
    print("A - B: ", dif_a_b)
    print("B - A: ", dif_b_a)

    # ex4_notes = ["do", "re", "mi", "fa", "sol"]
    # ex4_moves = [1, -3, 4, 2]
    # ex4_start = int(input("Start position: ").strip())
    # result = ex4(ex4_notes, ex4_moves, ex4_start)
    # print(result)

    # ex5_in_matrix = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]
    # ]
    # ex5_out_matrix = ex5(ex5_in_matrix)
    # if ex5_out_matrix is not None:
    #     for row in ex5_out_matrix:
    #         for element in row:
    #             print(element, end=" ")
    #         print()

    # list1 = [1, 2, 3, 1, 6]
    # list2 = [2, 3, 4]
    # list3 = [4, 5, 6]
    # list4 = [4, 1, "test"]
    # result = ex6(2, list1, list2, list3, list4)
    # print(result)

    # ex7_list = [12, 11211, 121, 345, 434, 123454321, 2345678, 543234]
    # cnt, greatest = ex7(ex7_list)
    # print(f"There are {cnt} palindrome numbers and the greatest one was: {greatest}")

    # ex8_list = ["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "wxyz"]
    # ex8_list2 = ["test", "hello", "lab002"]
    # result = ex8(ex8_list2, 2, False)
    # print(result)

    # ex9_matrix = [
    #     [1, 2, 3, 2, 1, 1],
    #     [2, 4, 4, 3, 7, 2],
    #     [5, 5, 2, 5, 6, 4],
    #     [6, 6, 7, 6, 7, 5]
    # ]
    # result = ex9(ex9_matrix)
    # print(result)

    # ex10_list1 = [1, 2, 3, 4]
    # ex10_list2 = [5, 6]
    # ex10_list3 = [7, 8, 9, 10, 11]
    # result = ex10(ex10_list1, ex10_list2, ex10_list3)
    # print(result)

    # result = ex11([('abc', 'bcd'), ('abc', 'zza')])
    # print(result)

    # words = ['ana', 'banana', 'carte', 'arme', 'parte']
    # result = ex12(words)
    # print(result)


if __name__ == "__main__":
    main()