import abc
class InvalidOperationError(Exception):
    pass

class Stream:
    def __init__(self):
        self.is_open = False

    def open(self):
        if self.is_open:
            raise InvalidOperationError("Invalid operation, cannot open")
        self.is_open = True


@abstractmethod
def write(self):
    pass
class NetworkStream(Stream):
    def read(self):
        print("reading data from a network....")


class MemoryStream(Stream):
    def write(self):
        print("writing data to a memory stream.. ")