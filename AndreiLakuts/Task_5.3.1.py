# Task 5.3
# File data/students.csv stores information about students in CSV format.
# This file contains the student’s names, age and average mark.
# 1.	Implement a function which receives file path and returns names of top performer students
# def get_top_performers(file_path, number_of_top_students=5):
#     pass
#
# print(get_top_performers("students.csv"))
# >>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']


def get_top_performers(file_path, number_of_top_students=5):
    """get_top_performers(file_path: str, number_of_top_students: int, as default 5)
    Function receives file path and returns "number_of_top_students" names of top performer students"""

    # Read data from input csv file put the "header"
    with open(file_path, 'r', encoding="utf-8") as file:

        line_counter = 0
        header = []
        students = []

        for line in file:
            # save "header"
            if line_counter == 0:
                for word in line.strip().split(","):
                    header.append(word)
                line_counter += 1

            # save other lines into the list "students"
            # transform "age" to integer and "average mark" to float
            else:
                temp_student = line.strip().split(",")
                temp_student[1] = int(temp_student[1])
                temp_student[2] = float(temp_student[2])
                students.append(temp_student)
    # end with

    # sort students by "average mark"
    mark_sorted_students = sorted(students, key=lambda average_mark: average_mark[2], reverse=1)

    top_students = []

    # Choose the "number_of_top_students" of most successful students
    for i in range(number_of_top_students):
        top_students.append(mark_sorted_students[i][0])

    return top_students


print(get_top_performers("students.csv"))
