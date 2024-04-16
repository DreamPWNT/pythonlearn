def intersect(*args):
    res = []
    for el in args[0]:
        print(el)
        if el in res:
            print("continue")
            continue
        else:
            for e in args[1:]:
                print(e)
                if not el in e:
                    break
            else:
                res.append(el)

    return res
  
def union(*args):
    res = []
    for el in args:
        for e in el:
            if not e in res:
                res.append(e)

    return res