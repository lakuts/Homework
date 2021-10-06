# Task 9.1
# Implement the [dining philosophers problem]
# (https://en.wikipedia.org/wiki/Dining_philosophers_problem).

#  Implementation using Semaphore
#  the program works endlessly


from threading import Thread, Semaphore
from time import sleep
from random import randint


class Philosopher(Thread):
    def __init__(self, number, left_fork, right_fork):
        Thread.__init__(self)
        self.number = number
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self) -> None:
        while True:
            # Philosopher thinks from 20 to 30 seconds
            sleep(randint(20, 30))
            print(f"Philosopher {self.number} is hungry")
            self.eating()

    def eating(self):
        """if both forks are free, philosopher starts eating"""
        fork1, fork2 = self.left_fork, self.right_fork
        while True:
            if fork1._value:
                fork1.acquire()
                if fork2._value:
                    fork2.acquire()
                    print(f"Philosopher {self.number} started eating")
                    # Philosopher eats from 5 to 10 seconds
                    sleep(randint(5, 10))
                    print(f"Philosopher {self.number} finished eating")
                    fork2.release()
                fork1.release()
                break

# create 5 "forks" - Semaphore() class objects
forks = [Semaphore() for i in range(5)]

# create 5 "philosophers" - Philosopher() class objects
philosophers = [Philosopher(i, forks[i % 5], forks[(i + 1) % 5]) for i in range(5)]

for philosopher in philosophers:
    philosopher.start()
