import os


class Path:
    def __init__(self, path=None):
        self.CWD = os.getcwd()
        self.sep = os.sep
        if path:
            self.current = os.fspath(path)
        else:
            self.current = os.path.dirname(__file__)

    def parent(self):
        self.current = os.path.dirname(self.current)
        return self
    
    def add_child(self, *dirname):
        self.current = os.path.join(self.current, *dirname)
        return self

    def get_children(self, *, just_names=True):
        if just_names:
            return os.listdir(self.current)
        
        children = []
        for child in os.scandir(self.current):
            if child.is_dir():
                obj = Path(child.path)
                children.append(obj)
        return children

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
        """Returns path depth."""
        return self.depth()
    
    def __bool__(self):
        """Returns True if exists."""
        return self.exists()
    
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
    
    def __repr__(self):
        return f"Path('{self.current}')"

    def __str__(self):
        return self.current


class File(Path):
    def __init__(self, path):
        # Path.__init__(self, path)
        super().__init__(path)
        self.current = os.fspath(path)

    def depth(self):
        return super().depth() - 1
    
    def create(self):
        return None

    def get_children(self, *, just_names=True):
        return None

    def add_child(self, *dirname):
        return None

    def file_name(self):
        return self.current.rsplit(os.sep)[-1]
    
    def __add__(self, obj):
        return NotImplemented
    
    def __radd__(self, obj):
        return NotImplemented
    
    def __truediv__(self, obj):
        return NotImplemented

    def __rtruediv__(self, obj):
        return NotImplemented
    
    def __repr__(self):
        return f"File('{self.current}')"


x = File("/home/pyhs/Рабочий стол/Материалы курса/target.png")

