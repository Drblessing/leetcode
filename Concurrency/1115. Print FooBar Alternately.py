from threading import Condition


class FooBar:
    def __init__(self, n):
        self.n = n
        self.condition = Condition()
        self.foo_turn = True

    def foo(self, printFoo: "Callable[[], None]") -> None:
        for _ in range(self.n):
            with self.condition:
                while not self.foo_turn:
                    self.condition.wait()
                printFoo()
                self.foo_turn = False
                self.condition.notify()

    def bar(self, printBar: "Callable[[], None]") -> None:
        for _ in range(self.n):
            with self.condition:
                while self.foo_turn:
                    self.condition.wait()
                printBar()
                self.foo_turn = True
                self.condition.notify()
