# Task 6.2
# Implement custom dictionary that will memorize 10 latest changed keys.
# Using method "get_history" return this keys.
# Example:
# >>> d = HistoryDict({"foo": 42})
# >>> d.set_value("bar", 43)
# >>> d.get_history()
#
# ["bar"]


class HistoryDict():

    def __init__(self,  work_dict = {}):
        self.work_dict = work_dict
        self.key_counter = []

    def set_value(self, key, value):
        self.work_dict[key] = value

        if key in self.key_counter:
            self.key_counter.remove(key)
            self.key_counter.append(key)
        elif len(self.key_counter) < 10:
            self.key_counter.append(key)
        else:
            self.key_counter.pop(0)
            self.key_counter.append(key)

    def get_history(self):
        print(self.key_counter)



