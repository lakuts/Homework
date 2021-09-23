# Task 5.3
# File data/students.csv stores information about students in CSV format.
# This file contains the student’s names, age and average mark.
# 2.	Implement a function which receives the file path with students info
# and writes CSV student information to the new file in descending order of age. Result:
# student name,age,average mark
# Verdell Crawford,30,8.86
# Brenda Silva,30,7.53
# ...
# Lindsey Cummings,18,6.88
# Raymond Soileau,18,7.27

def sort_age_students(unsorted_file_path, sorted_file_path = "age_sorted_students.csv"):
    """sort_age_students(unsorted_file_path: str, sorted_file_path: str, as default "age_sorted_students.csv")
    Function receives the CSV file path with students info
    and writes CSV student information to the new file in descending order of age.
    """

    # Read data from input csv file put the "header"
    with open(unsorted_file_path, 'r', encoding="utf-8") as file:

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

    # sort students by "age"
    age_sorted_students = sorted(students, key=lambda age: age[1], reverse=1)

    # write data into the output file
    with open(sorted_file_path, 'w+', encoding="utf-8") as file:

        # write "header"
        add_to_file = f"{header[0]},{header[1]},{header[2]}\n"
        file.write(add_to_file)

        # write "students"
        for student in age_sorted_students:
            add_to_file = f"{student[0]},{student[1]},{student[2]}\n"
            file.write(add_to_file)
    # end with


sort_age_students("students.csv")
