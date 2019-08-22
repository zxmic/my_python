class DDD():
    @staticmethod
    def decorate(func):
        def wrapper():
            print('decorate wrapper')
            func()
            print('decorate wrapper')
        return wrapper
'''
def decorate(func):
    def wrapper():
        func()
    return wrapper

def decoratex(func):
    def wrapper():
        func()
    return wrapper

@decorate
@decoratex
def test11():
    print("lllll")

test11()
'''
'''
def decorate2(func):
    def wrapper():
        print('decorate2')
        func()
        print('decorate2')
    return wrapper

@decorate2
@DDD.decorate
def test11():
    print("oooo")

test11()

# print(DDD.__dict__)
#===============================================================================
'''
'''
#通过装饰器做动态代理
def clsdeco(clz):
    class Test:
        def __init__(self):
            self.couse=clz()

        def getContent(self):
            return "couse: "+self.couse.getContent()

    return Test

@clsdeco
class Eng:
    def getContent(self):
        return "ENG"

s=Eng()
print(s.getContent())
'''
'''
def clsdemo(clz):
    class Test:
        def __init__(self):
            self.course=clz()

        def getContent(self):
            return 'course:'+self.course.getContent()

    return Test
@clsdemo
class PPP:
    def getContent(self):
        return 'PPP'
p=PPP()
print(p.getContent())
#==================================================================
'''

'''
#==================类装饰函数－－－－－需要实现call,调用被装饰者call会被调用===============================

class desc1:
    def __init__(self,func):
        print("￥￥￥￥￥")
        self.func=func
    def __call__(self, *args, **kwargs):
        print("～～～～")
        res=self.func(args[0])
        return res

@desc1
def some(arg):
    return arg+1

r=some(1)
print(r)

'''
'''
class desc1:
    def __init__(self,fuc):
        print("AAAA")
        self.fuc=fuc
    def __call__(self, *args, **kwargs):
        print("BBBB")
        res=self.fuc(args[0])
        print("CCCc")
        return res
@desc1
def some(arg):
    return arg+1

r=some(1)
print(r)
#==========================================================================


#对象修饰方法就是call修饰方法  例子opp->deco 272
class XXX():
    def __init__(self):
        pass
    def __call__(self,fun):
        def _call(*args,**kw):
            return fun(*args,**kw)
        return _call
class YYY(object):
    @XXX()
    def dis(self,test,ids):
        print('yyyyyyyy:'+test+' '+ids)

XXX().__call__(YYY().dis)("aaa","bbb")
YYY().dis

'''
'''
class decriptorxxx:
    def __init__(self):
        print("__init__")
    def __get__(self, instance, owner):
        owner.xxx(instance)
        print("get",instance,owner)
    def __set__(self, instance, value):
        print("set",instance,value)
    def __delete__(self, instance):
        print("del",instance)

class Some:
    def xxx(self):
        print("xx===============")
    d=decriptorxxx()

s=Some()
s.d="aaaa"
s.d="bbbb"
s.d
del s.d
'''
'''
class GetProp():
    def __init__(self, func):
        self.func = func
    def __get__(self, instance, cls):
        print("getprop")
        val = self.func(instance)
        return val
    def __set__(self, instance, value):
        print("setprop")
        self.func(instance, value)
class UUU():
    def __init__(self):
        pass
    @GetProp        #这么写等同于 uuu=GetProp(UUU.uuu)
    def uuu(self):
        print("get uuuuuu")
        return self.__uuu
    @GetProp
    def uuuu(self,u):
        print("set uuuuuu")
        self.__uuu=u
c = UUU()
c.uuuu="xxx"
c.uuuu="yyy"
print(c.uuu)
###################################################
'''
class Property():
    def __init__(self,fget=None,fset=None,fdel=None,doc=None):
        print("111111111111")
        self.fget=fget
        self.fset=fset
        self.fdel=fdel
        if doc is None and fget is not None:
            doc=fget.__doc__
        self.__doc__=doc
    def __get__(self, obj, objtype=None):
        print("222222222222")
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        print("333333333")
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        print("444444444")
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)
    def setter(self, fset):
        print("sssssssss")
        return type(self)(self.fget, fset, self.fdel, self.__doc__)  #修改了fset方法

    def deleter(self, fdel):
        print("ddddddddd")
        return type(self)(self.fget, self.fset, fdel, self.__doc__)  #修改了fdel方法


class Foo(object):
   def __init__(self):
       print("init")
       self._x = 1

   @Property
   def x(self):#x已经是个Property的对象了
       print('get......')
       return self._x

   @x.setter  #x是上一个x的setter方法返回的一个叫做ｘ的类的对象
   def x(self,val):
       print('set......')
       self._x = val

   @x.deleter
   def x(self):
       print('del.......')
       del self._x

f=Foo()
print("=====")
f.x="adfadfaf"
print(f.x)
del f.x

'''
class C():
    a = 'abc'

    def __setattr__(self, key, value):
        print('__setattr__() is called',key,value)

    def __getattribute__(self, *args, **kwargs):
        print("__getattribute__() is called")
        return object.__getattribute__(self, *args, **kwargs)

    def __getattr__(self, name):
        print("__getattr__() is called ",name)
        return name + " from getattr"

    def __get__(self, instance, owner):
        print("__get__() is called", instance, owner)
        return self

    def __set__(self, instance, value):
        print("__set__() is called",instance,value)

    def __del__(self):
        print("__del__() is called")

    def __delattr__(self, item):
        print("__delattr__() is called ", item)




class C2(object):
    d = C()


c = C()
c2 = C2()

print("-----1----")
c.a="aaa"
print("----2-----")
print(c.a)
print("----3-----")
print(c.zzzzzzzz)
print("+++++++++")
c2.d="xxx"
c2.d
print(c2.d.a)

del c.a

'''

