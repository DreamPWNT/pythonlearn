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
    
    def __eq__(self, obj):
        return self.current == obj.current
    
    def __ne__(self, obj):
        return NotImplemented
    
    def __lt__(self, obj):
        return self.current < obj.current

    def __gt__(self, obj):
        return NotImplemented

    def __le__(self, obj):
        return self.current <= obj.current
    
    def __ge__(self, obj):
        return self.current >= obj.current
    
    def __contains__(self, obj):
        return obj in self.current
    
    def __fspath__(self):
        return str(self)
    
    def __str__(self):
        return self.current
    

path = Path("/home/pyhs/course")
path2 = Path("/home/pyhs")

print("course" in path)
