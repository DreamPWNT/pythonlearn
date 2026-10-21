import b
import sys
import os

b.job('Python')

print(sys.stdlib_module_names)
print(sys.modules['os'] is os)
print(sorted(sys.modules))
print(sys.path)
print(os.getcwd())


for p in sys.path:
    print(p)
