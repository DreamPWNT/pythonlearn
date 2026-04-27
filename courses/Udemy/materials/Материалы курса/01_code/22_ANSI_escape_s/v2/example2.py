colorsd = {"green": "32", "yellow": "33", "blue": "34", "red": "31"}

class Palette:
    def __getattribute__(self, name):
        print("getattribute")
        return super().__getattribute__(name)
    
    def __getattr__(self, name):
        print("getattr")
        self.__dict__[name] = None
        return None
    
    def __setattr__(self, name, value):
        print("setattr")
        self.__dict__[name] = value
    
    def __delattr__(self, name):
        print("delattr")
        super().__delattr__(name)


for key in colorsd:
    setattr(Palette, key, colorsd[key])

color = Palette.green
print(f"\033[{color}mКрасный текст\033[0m")
print(Palette.__dict__)
