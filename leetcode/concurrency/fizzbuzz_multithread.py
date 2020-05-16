from typing import Callable
from threading import Barrier, Event, Lock, Thread


class FizzBuzzBarrier:
    def __init__(self, n: int):
        self.n = n
        self.b = Barrier(4)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            self.barrier.wait()
            if i % 3 == 0 and i % 5 != 0:
                printFizz()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            self.barrier.wait()
            if i % 3 != 0 and i % 5 == 0:
                printBuzz()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            self.barrier.wait()
            if i % 3 == 0 and i % 5 == 0:
                printFizzBuzz()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.barrier.wait()
            if i % 3 != 0 and i % 5 != 0:
                printNumber(i)


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.lock = Lock()
        self.event_fizz = Event()
        self.event_buzz = Event()
        self.event_fizzbuzz = Event()
        self.i = 1

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.event_fizz.wait()
            self.event_fizz.clear()
            if self.i > self.n:
                break
            printFizz()
            self.i += 1
            self.lock.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.event_buzz.wait()
            self.event_buzz.clear()
            if self.i > self.n:
                break
            printBuzz()
            self.i += 1
            self.lock.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.event_fizzbuzz.wait()
            self.event_fizzbuzz.clear()
            if self.i > self.n:
                break
            printFizzBuzz()
            self.i += 1
            self.lock.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while self.i <= self.n:
            if self.i % 3 == 0 and self.i % 5 != 0:
                self.event_fizz.set()
                self.lock.acquire()
                continue
            if self.i % 3 != 0 and self.i % 5 == 0:
                self.event_buzz.set()
                self.lock.acquire()
                continue
            if self.i % 3 == 0 and self.i % 5 == 0:
                self.event_fizzbuzz.set()
                self.lock.acquire()
                continue
            printNumber(self.i)
            self.i += 1
        self.event_fizz.set()
        self.event_buzz.set()
        self.event_fizzbuzz.set()


n = 15
fb = FizzBuzz(n)
th1 = Thread(name='1', target=fb.fizz, args=(lambda: print("fizz"), ))
th2 = Thread(name='2', target=fb.buzz, args=(lambda: print("buzz"), ))
th3 = Thread(name='3', target=fb.fizzbuzz, args=(lambda: print("fizzbuzz"), ))
th4 = Thread(name='4', target=fb.number, args=(lambda x: print(x), ))
th1.start()
th2.start()
th3.start()
th4.start()
