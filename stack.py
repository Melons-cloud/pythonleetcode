# coding:utf-8
class Stack(object):
    def __int__(self):
        self.__list=[]

    def push(self,item):
        self.__list.append(item)
        pass
    def pop(self):
        self.__list.pop()
        pass
    def peek(self):
        pass
    def is_empty(self):
        pass
    def size(self):
        pass

if __name__=="__main__":
    s=Stack();