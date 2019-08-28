'''
class classmath:
    def __init__(self,mth):
        self.mth=mth

    def __get__(self, instance, owner):  #利用get的第三个参数，来修改调用类方法的第一个参数，来实现类方法
        def wrapper(*args,**kwargs):
            return self.mth(owner,*args,**kwargs)

        return wrapper

class Other:
    @classmethod
    def doit(clz,a,b):
        print(clz,a,b)
        return a+b

class Other1:
    def doit(clz,a,b):
        print(clz,a,b)
        return a+b

print(Other.doit(1,2))
o=Other1()
#c=classmeth

'''
#==================================================================
#desception  的 __enter__和__exit__  案例oop deco 443

class MyException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Res:
    def __init__(self,name):
        self.name=name

    def __enter__(self):
        print(self.name+" enter ")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.name+" exit ")
        return False

class MyGeneratorContextManger():
    def __init__(self,gen):
        print("__init__ called")
        self.gen=gen

    def __enter__(self):
        print("__enter__ called")
        return self.gen.__next__()

    def __exit__(self, type, value, traceback):
        try:
            self.gen.throw(type,value,traceback)
        except:
            return True

def MyContextManger(func):
    def tmpf(*args):
        print("func info:",func)
        return MyGeneratorContextManger(func(*args))
    return tmpf

