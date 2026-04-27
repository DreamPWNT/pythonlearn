import os


class Path:
    def __init__(self, path=None):
        self.current = path or os.path.dirname(__file__)

    def parent(self):
        self.current = os.path.dirname(self.current)
        return self
    
    def get_path(self):
        return self.current
    
    def __add__(self, obj):
        if not isinstance(obj, str):
            return NotImplemented
        return Path(os.path.join(self.current, obj))

    def __radd__(self, obj):
        if not isinstance(obj, str):
            return NotImplemented
        return Path(os.path.join(self.current, obj))
    
    def __truediv__(self, obj):
        if not isinstance(obj, str):
            return NotImplemented
        return Path(os.path.join(self.current, obj))
        
    def __rtruediv__(self, obj):
        if not isinstance(obj, str):
            return NotImplemented
        return Path(os.path.join(self.current, obj))
    
    def __str__(self):
        return self.current
        

path = Path("/hello/my/object")
path2 = "home" / path

print(path2)

