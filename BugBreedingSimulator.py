# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 15:44:40 2021

@author: simon
"""
import random

#Bug Class
class Bug:
    def __init__(self, name, size, strength, intelligence):
        self.name = name
        self.size = size
        self.strength = strength
        self.intelligence = intelligence
        
    def printstats(self):
        print(f'''{self.name}'s stats:''')
        print('Size:', self.size)
        print('Strength:',self.strength)
        print('Intelligence:',self.intelligence)
        
p1 = Bug('Parent 1', 50, 70, 30)
p2 = Bug('Parent 2',50, 30, 70)

c = Bug(0,0,0,0)
def statgen(x1, x2, x):
    x.name = input('Enter a name for your bug: ')
    if x1.size < x2.size:   x.size = random.randint(p1.size, p2.size)
    elif x1.size > x2.size: x.size = random.randint(p2.size, p1.size)
    else: x.size = random.randint(p1.size-5, p2.size+5)
    
    if x1.strength < x2.strength:   x.strength = random.randint(p1.strength, p2.strength)
    elif x1.strength > x2.strength: x.strength = random.randint(p2.strength, p1.strength)
    else: x.strength = random.randint(p1.strength-5, p2.strength+5)
    
    if x1.intelligence < x2.intelligence:   x.intelligence = random.randint(p1.intelligence, p2.intelligence)
    elif x1.intelligence > x2.intelligence: x.intelligence = random.randint(p2.intelligence, p1.intelligence)
    else: x.intelligence = random.randint(p1.intelligence-5, p2.intelligence+5)
    
statgen(p1, p2, c)
c.printstats()

