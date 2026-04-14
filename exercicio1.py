
import math
import os
import random
import re
import sys


if __name__ == '__main__':

    n = int(input())
    
    #se o num inserido, ao dividir por zero, for diferente de 0, significa que ele é ímpar
    if n % 2 != 0:
        print("Weird")
        
    else:
        if   2 <= n <= 5:
            print("Not Weird")
        elif  6 <= n  <= 20:
            print("Weird")
        if n > 20:
            print("Not Weird")