def map():
    list = range(10)
    result = [x + 2 for x in list]
    print(result)

def reduce():
    list = range(10)
    result = [ x -2 for x in list]
    print(result)


if __name__=="__main__" :
    map()
    reduce()