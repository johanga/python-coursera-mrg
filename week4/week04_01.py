import os.path
import tempfile

class File:
    def __init__(self, path):
        self._path = path
        
    def __add__(self, other):
        obj = File(os.path.join(tempfile.gettempdir(), "tmp.txt"))
        obj.write(self.read() + other.read())
        return obj
    
    def __iter__(self):
        self._curr = 0
        with open(self._path, "r") as f:
            self._lines = f.readlines()
        return self
    
    def __next__(self):
        try:
            line = self._lines[self._curr]
            self._curr += 1
            return line
        except IndexError:
            raise StopIteration
    
    def __str__(self):
        return self._path
        
    def read(self):
        with open(self._path, "r") as f:
            return f.read()
        
    def write(self, data):
        with open(self._path, "w") as f:
            f.write(data)
