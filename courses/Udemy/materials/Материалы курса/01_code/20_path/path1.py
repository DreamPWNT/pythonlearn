import os
from pathlib import Path

# x = Path(__file__).parent
# print(x)

class Path:
    def __init__(self, path=None):
        self.CWD = os.getcwd()
        self.current = path or os.path.dirname(__file__)
    def parent(self):
        self.current = os.path.dirname(self.current)
        return self
    def get_parent(self):
        return os.path.dirname(self.current)
    def add_dir(self, dirname):
        self.current = os.path.join(self.current, dirname)
        return self
    def get_path(self):
        return self.current
    def __str__(self):
        return self.current
        

path = Path("/hello/my/object")

print(path.get_path())


