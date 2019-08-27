#路径要写绝对路径
input="/home/zx/PycharmProjects/my_python/my_py/Filess/day6file/Hello.txt"
output="/home/zx/PycharmProjects/my_python/my_py/Filess/day6file/Hello_out.txt"

f=open(input,'r')
print(f.tell())    #tell方法返回文件的当前位置，文件指针当前位置
print(f.read())    #read是把这个文件一次性全都读取出来
print(f.read(1))
#print(f.tell())
#print(f.seek(4))
#print(f.read(1))
f.close()