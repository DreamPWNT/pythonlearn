import shutil

# ! Top-Down func definitions

def zip_archive(destination, target, *, delete_target=False):
    shutil.make_archive(destination, "zip", target)

    if delete_target:
        shutil.rmtree(target)
    
    return destination + ".zip"