from threading import Thread
import time
from random import randint
from math import factorial
import sympy

def numbers(file):
    with open(file, 'w') as f:
        for i in range(10):
            f.write(f'{randint(1,10)}')
    with open(file, 'r') as f:
        lst=f.readlines()
    return lst

x=Thread(target=numbers)
x.start()
x.join()
number=numbers(input('Name file: '))
print(number[0])
def easy(lst):
    new_lst=[]
    for i in lst[0]:
        if sympy.isprime(int(i)):
            new_lst.append(int(i))
    print(new_lst)
    return new_lst

def fact(lst):
    new_lst=[]
    for i in lst[0]:
        new_lst.append(factorial(int(i)))
    print(new_lst)
    return new_lst


x1=Thread(target=easy, args=(number,))
x2=Thread(target=fact, args=(number,))
x1.start()
x2.start()
with open('new_file.txt', 'w') as f:
    f.write(f'{easy(number)}\n{fact(number)}')
