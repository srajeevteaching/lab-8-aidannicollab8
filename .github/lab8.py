# Programmers: Aidan & Nicol
# Course: CS151, Dr. Rajeev
# Date: 11/11/2021
# Lab Number: 8
# Program Inputs: name of file
# Program Outputs: a random name called

# Problem A professor needs a program that will choose a random student in class to call on when no one is raising their
# hand to offer an answer. Write a program that asks the user for a filename and then reads in the student names from
# the given file and stores them in a list. The program should then give the user a randomly-chosen name and give the
# option to continue or quit. If the user chooses to continue, the program should draw a new name (with the previous
# name having been removed from consideration).

# The names of the students in the class are supplied as a plain-text file with one name per line. Use the file
# names.txt accompanying this handout, which contains names taken from randomlists.com, to test your program.
# However, your program should work with any valid plain-text file of names.

import random
import os

def read_file(filename):
    data_list = []
    file = open(filename, "r")
    for line in file:
        data_list.append(line)
    file.close()
    return data_list

def read_filename():
    filename = input("Enter a file name: ")
    while not os.path.exists(filename):
        filename = input("Enter a file name: ")
    return filename

def main():
    filename = read_filename()
    name_list = read_file(filename)
    current_name = random.choice(name_list)
    print("You called on", current_name)
    choice = input("Enter Y to continue or Q to quit: ")
    while choice.strip().lower() == "y":
        print("You called on", random.choice(name_list))
        choice = input("Enter Y to continue or Q to quit: ")
    else:
        print("Thank you")

main()
