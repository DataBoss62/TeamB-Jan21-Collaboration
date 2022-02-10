from pickle import TUPLE1
from random import randint   

# def die():
    
#  (randint(1,6))  # generated a random number in range 1 to 6
#  return 


def die():
     var1 = randint(1,6)
     var2 = randint(1,6)
     tup1 = var1, var2
     return (tup1)



