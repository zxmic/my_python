class AAAmeta(type):
    def __new__(clz, *args, **kwargs):
        print("meta__new__")
        instance=clz
        print("meta__init__")


class AAA(metaclass=AAAmeta):
    def __new__(cls, *args, **kwargs):
        print("AAA__new__")

    def __init__(self):
        print("AAA__init__")

if __name__=="__main__":
    a=AAA()