'''
print("="*50)
def add(i,j=100):
    print(str(i+j)+"xxx")

#print(add(4,j=1))
#print(add(i=3))
'''
import queue
import random
import time

'''
total=100
def pp(i):
    global total
    total=20
    print(total)
pp(2)
print(total)
'''
'''
def pp(i):
    total=20
    print(total)
    def xx(i):
        nonlocal total
        total=6
        print(total)
'''

#lambda 表达式

'''
#写一个闭包
def fun():
    i=1
    print("fun====="+str(i))
    def fun1():
        nonlocal i
        print("fun1==="+str(i))
        return lambda :print('fun1 return==='+str(i))
    return fun1()
print(fun()())
'''


'''
#解构
def some(**aaa):
    print(aaa)
'''

'''
#空体 python不能有空体
for i in range(10):
    pass
'''

''' 不懂
#生成器 yield（yield与retuan不能共存）  天生的协程
def product():#生成器 yield就像断点 yield也像return 会返回
    while True:
        print('开始生产')
        data=random.randint(0,9)
        print('生产者生产了'+str(data))
        yield data
        uuu=yield data
        print("xxx:",uuu)
p=product()#声明
c=next(p)
print(c)
c=p.send("222")
print(c)
'''

'''
myque = queue.Queue(1)
def runner():
    print('start....')
    yield getinput()
    print("ok")

def getinput():
    time.sleep(1)
    print("xxxx")
    time.sleep(1)
    myque.put("xxxxxxxxxxxxxxx")

if __name__ =="__main__":
    r=runner()
    next(r)
    res=""
'''

'''
#try catch
while True:
    try:
        print('mainnext:',next)
        print('mainsend',f.send(i))
        i+=1
        print("+"*50)
    except StopIteration as e:
        break
'''
mylist = []
#单句解释







