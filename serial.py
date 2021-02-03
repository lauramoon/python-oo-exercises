"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial
    <SerialGenerator start=100 current=103>

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        "create generator of integers starting with 'start'"
        self.start = start
        self.current = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} current={self.current}>"

    def generate(self):
        "returns the number one higher than the last one"
        self.current += 1
        return self.current - 1

    def reset(self):
        "resets the generator so the next number returned is the original starting number"
        self.current = self.start
