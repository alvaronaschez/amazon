from typing import Callable
from threading import Lock
import time


class DiningPhilosophers:
    def __init__(self):
        self.locks = [Lock() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self, philosopher: int, pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        if philosopher != 0:
            first, second = philosopher, (philosopher + 1) % 5
        else:
            second, first = philosopher, (philosopher + 1) % 5
        with self.locks[first]:
            with self.locks[second]:
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()


class DiningPhilosophers_my_first_solution:
    def __init__(self):
        self.forks = [Lock() for _ in range(5)]
        self.last_bite = [time.time() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self, philosopher: int, pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        left = philosopher
        right = (philosopher + 1) % 5
        timeout = (time.time() - self.last_bite[philosopher]) / 3
        while True:
            if self.forks[left].acquire(timeout=timeout):
                if self.forks[right].acquire(timeout=timeout):
                    break
                self.forks[left].release()
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        self.last_bite[philosopher] = time.time()
        self.forks[right].release()
        self.forks[left].release()
