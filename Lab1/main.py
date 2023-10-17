# 1. Find The greatest common divisor of multiple numbers read from the console.
#
# Write a script that calculates how many vowels are in a string.
#
# Write a script that receives two strings and prints the number of occurrences of the first string in the second.
#
# Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
#
# Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order (as in t
# he example):
# firs      1  2  3  4    =>   first_python_lab
# n_lt      12 13 14 5
# oba_      11 16 15 6
# htyp      10 9  8  7
#
# Write a function that validates if a number is a palindrome.
#
# Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function will return 123, or if the text is "abc123abc" the function will extract 123). The function will extract only the first number that is found.
#
# Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"
#
# Write a functions that determine the most common letter in a string. For example if the string is "an apple is not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent the same character.
#
# Write a function that counts how many words exists in a text. A text is considered to be form out of words that are separated by only ONE space. For example: "I have Python exam" has 4 words.


#####################################################################################################################
# 1
def ex1():
    input_str = input("Numbers: ")
    numbers_str = input_str.split()

    #aflam primul numar
    num1 = int(numbers_str[0])

    #parcurgem lista cu numere
    for num_str in numbers_str:

        #convertim numarul la int
        num2 = int(num_str)

        #aflam cmmdc dintre cele doua
        while num2:
            num1, num2 = num2, num1 % num2

    print(num1)

#####################################################################################################################
#2
def ex2():
    #parcurgem fiecare pozitie din sir verificand daca este vocala

    vocale = "aeiouAEIOU"

    str = input("String: ")

    count = 0

    for char in str:
        if char in vocale:
            count = count + 1

    print(count)

#####################################################################################################################
#3
def ex3():
    str1 = input("String 1: ")
    str2 = input("String 2: ")

    #print(str2.count(str1)) 

    count = 0
    for i in range(len(str2) - len(str1) + 1):
        if str2[i:i + len(str1)] == str1:
            count += 1

    print(count)

####################################################################################################################
#4
def ex4():
    camelCase = input("CamelCase string: ")

    index = 0

    snakeCase = camelCase[:1].lower()
    camelCase = camelCase[1:]

    for char in camelCase:
        index = index + 1
        if char == char.upper():
            snakeCase = snakeCase + "_" + camelCase[index-1:index].lower()
        else:
            snakeCase = snakeCase + camelCase[index - 1:index].lower()

    print("Snake case: " + snakeCase)

####################################################################################################################
#5
def ex5():
    input_str = input("Dimensiunea matricii: ")
    n = int(input_str)

    matrix = []

    #Read the matrix
    for i in range(n):
        row = input()
        matrix.append(row)

    top = 0
    left = 0
    bottom = n - 1
    right = n - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            print(matrix[top][i], end="")
        top = top + 1

        for i in range(top, bottom + 1):
            print(matrix[i][right], end="")
        right = right - 1

        if top < bottom:
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i], end="")
            bottom = bottom - 1

        if left < right:
            for i in range(n - bottom, top - 1, -1):
                print(matrix[i][left], end="")
            left = left + 1

    #Print the matrix
    # for i in range(n):
    #     for j in range(n):
    #         print(matrix[i][j], end=" ")
    #     print()

####################################################################################################################
#6
def ex6():
    number = input("Numarul: ")

    length = len(number)
    pal = 1
    for i in range(length//2):
        if number[i] != number[length - 1 - i]:
            pal = 0
            break

    if pal == 1:
        print("Palindrom")
    else:
        print("Nu este palindrom")

####################################################################################################################
#7
def ex7():
    text = input("Textul: ")

    numbers = "0123456789"
    index = 0
    found = 0

    for char in text:
        if (char in numbers) and (found == 0):
            found = 1
            while char in numbers:
                print(char, end="")
                if index + 1 < len(text):
                    index = index + 1
                    char = text[index]
                else:
                    break
            else:
                break
        index = index + 1

####################################################################################################################
#8
def ex8():
    num = int(input("Numar: "))

    b1 = 0
    while num > 0:
        if num%2 == 1:
            b1 += 1
        num //=2

    print("Number has", b1, "bits of 1")

####################################################################################################################
#9
def ex9():
    text = input("Text: ")
    maxim = 0

    c = ""

    for char in text:
        if text.count(char) > maxim and not(char.isspace()):
            maxim = text.count(char)
            c = char

    print(c)

####################################################################################################################
#10
def ex10():
    text = input("Text: ")
    count = len(text.split())
    print("Word count: ", count)


####################################################################################################################
def main():
    print("Main function")
    #ex1()
    #ex2()
    ex3()
    #ex4()
    #ex5()
    #ex6()
    #ex7()
    #ex8()
    #ex9()
    #ex10()


if __name__ == "__main__":
    main()