from threading import Thread
import time
from random import randint

def numbers():
    lst=[]
    for i in range(10):
        time.sleep(1)
        s=randint(1,10)
        lst.append(s)
    return lst

number=numbers()
print(number)
def summ(lst):
    print(sum(lst))

def middle(lst):
    print(sum(lst)/len(lst))

x=Thread(target=numbers)
x.start()
x.join()
x1=Thread(target=summ, args=(number,))
x2=Thread(target=middle, args=(number,))
x1.start()
x2.start()






