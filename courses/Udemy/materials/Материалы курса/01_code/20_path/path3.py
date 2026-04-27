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
    
    def __len__(self):
        return len(self.current)
    
    def __bool__(self):
        return bool(len(self))
    
    def __fspath__(self):
        return str(self)
    
    def __str__(self):
        return self.current
    

        

path = Path("")

print(bool(path))
if path:
    print("Only True")



