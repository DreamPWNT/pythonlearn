import os


class Path:
    def __init__(self, path=None):
        self.CWD = os.getcwd()
        self.sep = os.sep
        self.current = path or os.path.dirname(__file__)

    def parent(self):
        self.current = os.path.dirname(self.current)
        return self
    
    def add_child(self, dirname):
        self.current = os.path.join(self.current, dirname)
        return self

    def get_children(self, *, just_names=True):
        if just_names:
            return os.listdir(self.current)
        
        # Пока просто смотреть:
        # children = []
        # for child in os.scandir(self.current):
        #     if child.is_dir():
        #         obj = Path(child.path)
        #         children.append(obj)
        # return children

    def exists(self):
        return os.path.exists(self.current)
    
    def is_link(self):
        return os.path.islink(self.current)
    
    def depth(self):
        return len(self.current.split(self.sep))
    
    def get_path(self):
        return self.current
    
    def create(self):
        os.makedirs(self.current)
        return self

    def __add__(self, obj):
        if isinstance(obj, str):
            return Path(os.path.join(self.current, obj))
        elif isinstance(obj, Path):
            return Path(os.path.join(self.current, obj.current))
        return NotImplemented
        
    def __radd__(self, obj):
        if not isinstance(obj, str):
            return NotImplemented
        return Path(os.path.join(self.current, obj))
    
    def __truediv__(self, obj):
        if isinstance(obj, str):
            return Path(os.path.join(self.current, obj))
        elif isinstance(obj, Path):
            return Path(os.path.join(self.current, obj.current))
        return NotImplemented
        
    def __rtruediv__(self, obj):
        if not isinstance(obj, str):
            return NotImplemented
        return Path(os.path.join(self.current, obj))
    
    def __len__(self):
        return len(self.current)
    
    def __bool__(self):
        """Returns True if exists."""
        return os.path.exists(self.current)
    
    def __eq__(self, obj):
        if isinstance(obj, str):
            return self.current == obj
        elif isinstance(obj, Path):
            return self.current == obj.current
        return NotImplemented
    
    def __ne__(self, obj):
        return NotImplemented
    
    def __contains__(self, obj):
        if isinstance(obj, str):
            return obj in self.current
        elif isinstance(obj, Path):
            return obj.current in self.current
        return NotImplemented
    
    def __fspath__(self):
        return str(self)
    
    def __str__(self):
        return self.current


path = Path("/home/pyhs")

print(path)
