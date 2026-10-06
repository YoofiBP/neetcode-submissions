class MinStack:

    def __init__(self):
        self.pos = None
        self.minPos = None
        self.counter = {}
        self.minCounter = {}

    def push(self, val: int) -> None:
        self.pos = 0 if self.pos is None else self.pos + 1
        self.counter[self.pos] = val

        minValue = min(val, self.minCounter[self.minPos] if self.minPos is not None and self.minPos > -1 else val)

        if self.minPos is None:
            self.minPos = 0
        else:
            self.minPos += 1

        self.minCounter[self.minPos] = minValue


    def pop(self) -> None:
        if self.pos < 0 or self.pos is None:
            print("Nothing here")
            return
        del self.counter[self.pos]
        self.pos -= 1
        del self.minCounter[self.minPos]
        self.minPos -= 1

    def top(self) -> int:
        return self.counter[self.pos]

    def getMin(self) -> int:
        return self.minCounter[self.minPos]
