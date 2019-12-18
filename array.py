#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Dec 2019
# This program uses a 2D array

import random


def sum_of_numbers(passed_in_2D_list):
    # this function adds up all the elements in  a 2D array

    total = 0
    for row_value in passed_in_2D_list:
        for single_element in row_value:
            total += single_element
            avarage = (total / len(passed_in_2D_list)) / len(row_value)

    return avarage


def main():
    # this function uses a 2D array

    a_2d_list = []

    # input
    rows = int(input("How many row would you like: "))
    columns = int(input("How many columns would you like: "))

    for loop_counter_rows in range(0, rows):
        temp_column = []
        for loop_counter_columns in range(0, columns):
            a_random_number = random.randint(0, 50)
            temp_column.append(a_random_number)
            print("{0} ".format(a_random_number), end="")
        a_2d_list.append(temp_column)
        print("")

    sum = sum_of_numbers(a_2d_list)
    print("The avarage: {:.2f} ".format(sum))


if __name__ == "__main__":
    main()
