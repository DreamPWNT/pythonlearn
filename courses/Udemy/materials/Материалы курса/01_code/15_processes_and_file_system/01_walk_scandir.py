import os

path = "/"
exclude_dirs = ["root", "etc", "snap"]

paths = []

for address, dirs, files in os.walk(path):

    for exclude in exclude_dirs:
        if exclude in dirs:
            dirs.remove(exclude)

    for file in files:
        if "neuron" in file:
            paths.append(os.path.join(address, file))
    
print(paths)