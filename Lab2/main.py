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
    intersection = list(set(a_list) & set(b_list))
    union = list(set(a_list) | set(b_list))
    dif_a_b = list(set(a_list) - set(b_list))
    dif_b_a = list(set(b_list) - set(a_list))

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

def main():
    
    #n = int(input("Number of elements: ").strip())
    #ex1_classic()
    #ex1_rec(n)

    # ex2_list = ex2([0])
    # print(ex2_list)

    # ex3_a_list = [1, 2, 3, 4, 5]
    # ex3_b_list = [3, 4, 5, 6, 7]
    # intersection, union, dif_a_b, dif_b_a = ex3(ex3_a_list, ex3_b_list)
    # print("A intersected with B: ", intersection)
    # print("A reunited with B: ", union)
    # print("A - B: ", dif_a_b)
    # print("B - A: ", dif_b_a)

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

    list1 = [1, 2, 3, 1, 6]
    list2 = [2, 3, 4]
    list3 = [4, 5, 6]
    list4 = [4, 1, "test"]
    result = ex6(2, list1, list2, list3, list4)
    print(result)

    #ex7()
    #ex8()
    #ex9()
    #ex10()


if __name__ == "__main__":
    main()