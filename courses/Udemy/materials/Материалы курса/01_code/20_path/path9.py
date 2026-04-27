import os


class Path:
    def __init__(self, path=None):
        self.CWD = os.getcwd()
        self.sep = os.sep
        if path:
            self.__current = os.fspath(path)
        else:
            self.__current = os.path.dirname(__file__)

    def _get_current(self):
        return self.__current
    
    def _set_current(self, path):
        self.__current = os.fspath(path)  # Добавил в метод использование функции os.fspath

    def parent(self):
        # self.__current = os.path.dirname(self.__current)
        self.__current = os.path.dirname(self)  # Так как есть __fspath__
        return self

    def exists(self):
        # return os.path.exists(self.__current)
        return os.path.exists(self)  # Так как есть __fspath__
    
    def is_link(self):
        # return os.path.islink(self.__current)
        return os.path.islink(self)  # Так как есть __fspath__
    
    def depth(self):
        # return len(self.__current.split(self.sep))
        # Добавил функцию нормализации пути, чтоб убрать конечный слеш,
        # если вдруг путь получится /a/b/c/  а не нормальный /a/b/c,
        # чтоб корректно отработала len во всех случаях.
        # И конечно в функцию normpath можно передать просто self,
        # а не self.__current, так как там будет использован __fspath__.
        return len(os.path.normpath(self).split(self.sep))
    
    def get_path(self):
        return self.__current
    
    def __len__(self):
        """Returns path depth."""
        return self.depth()
    
    def __bool__(self):
        """Returns True if exists."""
        return self.exists()
    
    def __eq__(self, obj):
        if isinstance(obj, str):
            return self.__current == obj
        elif isinstance(obj, Path):
            return self.__current == obj.__current
        return NotImplemented
    
    def __contains__(self, obj):
        if isinstance(obj, str):
            return obj in self.__current
        elif isinstance(obj, Path):
            return obj.__current in self.__current
        return NotImplemented
    
    def __fspath__(self):
        return str(self)
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__current}')"

    def __str__(self):
        return self.__current


class Dir(Path):
    def add_child(self, *dirname):
        # self._set_current(os.path.join(self._get_current(), *dirname))
        self._set_current(os.path.join(self, *dirname))  # Так как есть __fspath__
        return self

    def get_children(self, *, just_names=True):
        if just_names:
            # return os.listdir(self._get_current())
            return os.listdir(self)  # Так как есть __fspath__
        
        children = []
        # for child in os.scandir(self._get_current()):
        for child in os.scandir(self):  # Так как есть __fspath__
            if child.is_dir():
                obj = Dir(child.path)  # Подправил с Path на Dir
                children.append(obj)
        return children
    
    def create(self):
        # os.makedirs(self._get_current())
        os.makedirs(self)  # Так как есть __fspath__
        return self
        
    def _join(self, obj):
        return Dir(os.path.join(self, obj)) # Так как есть __fspath__ просто self и obj

    def __add__(self, obj):
        if isinstance(obj, str):
            return self._join(obj)
        elif isinstance(obj, Path):
            return self._join(obj)
        return NotImplemented
        
    def __radd__(self, obj):
        if not isinstance(obj, str):
            return NotImplemented
        return self._join(obj)
    
    def __truediv__(self, obj):
        if isinstance(obj, str):
            return self._join(obj)
        elif isinstance(obj, Path):
            return self._join(obj)
        return NotImplemented
        
    def __rtruediv__(self, obj):
        if not isinstance(obj, str):
            return NotImplemented
        return self._join(obj)
    

class File(Path):
    def __init__(self, path):
        super().__init__()  # Исполняется код Path.__init__
        self._set_current(path)  # Добавил в метод _set_current использование функции os.fspath

    def depth(self):
        return super().depth() - 1  # Исполняется Path.depth

    def file_name(self):
        # return self._get_current().rsplit(self.sep)[-1]
        # Можно использовать эту функцию из os.path для получения имени:
        return os.path.basename(self)  # И конечно там тоже будет использован __fspath__

    def parent(self):
        # Создаем экземпляр Dir как есть, и потом к нему применяем ЕГО метод parent
        return Dir(self).parent()

