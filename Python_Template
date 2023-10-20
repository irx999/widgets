#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
# By:                                                                                                   #
#         ########              ##         ##  #########  ########  #########   ########   ##      ##   #
#       ##      ##             ##         ##        ###       ###        ###  ##      ##   ##    ##     #
#      ##           ########   ##  ########        ##        ##         ##   ####           ## ##       #
#     ##           ##    ##   ##  ##    ##      ##         ##        ##          ####       ###         #
#    ##       ##  ##    ##   ##  ##    ##     ##         ##        ##      ##      ##       ##          #
#    ##########   #######   ###  #######    ##         ##        ##        #########       ##           #
#                                                                                               V:0.0.1 #
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
"""
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
# PROJECT MADE WITH: ####
import os,sys
sys.path.append('./code/')
#from os import *

class Class_1:


    def __init__(self, value=None):
        self.value = value
        self.folder = "导出文件夹/"
        self.path = f"{os.path.split(os.path.realpath(__file__ ))[0]}/{self.folder}"
    
    def __getattr__(self, key):
        print(f"__getattr__ called: unexisted key {key}")
        return None
    
    def __getattribute__(self, key):
        print(f"__getattribute__ called: key {key}")
        return super(Class_1, self).__getattribute__(key)

    def __setattr__(self, key, value):
        if key in self.__dict__:
            print(f"__setattr__ called: key existed {key}")
        else:
            print(f"__setattr__ called: key unexisted {key}")
        self.__dict__[key] = value
    
    def __delattr__(self, key):
        print(f"__delattr__ called: key {key}")
        del self.__dict__[key]

    def function_1(self,pram_1=None,pram_2=None):
        try:
            print(123)
        
        except Exception as e:
            print(e)

    def function_2(self,pram_1=None,pram_2=None):
        try:
            pass

        except Exception as e:
            print(e)


if __name__ == '__main__':
    #前置配置

    if True:
        print([x for x in range(1,20)])

        a = lambda x :x == x
        b = lambda x ,y: x*y
        c = lambda x : x if x == 1 else 2
        print(a(2))
        print(list(filter(a,range(1,11))))
        print(list(map(b,[1,2,3],[1,3,2,1])))
        print(c(3))
        Class_1(value=None).function_1(pram_1=None,pram_2=None)    

    elif True:
        Class_1.function_2(pram_1=None,pram_2=None)

    else:
        pass
