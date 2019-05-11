import fire
from collections import OrderedDict

def test():
    data = [('a', 1), ('b', 2), ('c', 3)]
    return OrderedDict(data)

if __name__ == "__main__":
    fire.Fire(test)
