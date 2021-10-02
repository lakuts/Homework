# Task_7.1
# Implement class-based context manager for opening and
# working with file, including handling exceptions.
# Do not use 'with open()'. Pass filename and mode via constructor.

class FileManager:
    def __init__(self, file_name, method="r"):
        self.file_name = file_name
        self.method = method
        self.file_obj = None

    def __enter__(self):
        try:
            self.file_obj = open(self.file_name, self.method)
        except FileNotFoundError as error:
            print(f"{error}. File {self.file_name} not found")
        return self.file_obj

    def __exit__(self, type, value, traceback):
        if self.file_obj:
            self.file_obj.close()
        if type:
            print(f"Exception: {type}, {value}, {traceback}")
        return True


#Test
# with FileManager('demo.txt', 'r') as file:
#     file.write("Hello -1! \n")
#
# with FileManager('demo.txt', 'w') as file:
#     file.write("Hello -2! \n")
#
# with FileManager('demo.txt', 'r') as file:
#     file.write("Hello -3! \n")
#
# with FileManager('demo.txt', 'a') as file:
#     file.write("Hello -4! \n")
