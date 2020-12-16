#!/bin/python

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    cost_dict = {}
    for i,cos in enumerate(cost):
        if money-cos in cost_dict:
            print(str(cost_dict[money-cos]+1) + ' ' + str(i+1))
            return 
        else:
            cost_dict[cos] = i

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        money = int(raw_input())

        n = int(raw_input())

        cost = map(int, raw_input().rstrip().split())

        whatFlavors(cost, money)
