"""
https://leetcode.com/problems/print-foobar-alternately/

1115. Print FooBar Alternately
Medium

Suppose you are given the following code:

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
The same instance of FooBar will be passed to two different threads. Thread A
will call foo() while thread B will call bar(). Modify the given program to
output "foobar" n times.



Example 1:

Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them
calls foo(), while the other calls bar(). "foobar" is being output 1 time.
Example 2:

Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times.
"""
from threading import Lock
from typing import Callable


class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock1 = Lock()
        self.lock2 = Lock()
        self.lock2.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.lock1.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.lock2.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.lock2.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.lock1.release()
