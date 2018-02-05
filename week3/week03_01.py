class FileReader:
    def __init__(self, path):
        self._path = path
    def read(self):
        try:
            with open(self._path, "r") as f:
                return f.read()
        except IOError:
            return ""
