# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 15:44:40 2021

@author: simon
"""
import random
sizemutation = False
strmutation = False
intmutation = False
#Bug Class
class Bug:
    def __init__(self, size, strength, intelligence):
        self.size = size    
        self.strength = strength
        self.intelligence = intelligence

#creates parents
p1 = Bug(50,70,30)
p2 = Bug(50,30,70)

#creates child stats

mfactor = random.randint(1,100)
if p1.size < p2.size:
    size = random.randint(p1.size, p2.size)
    if mfactor >= 95:
        size = random.randint(p2.size, p2.size+10)
        sizemutation = True
    elif mfactor <= 5:
         size = random.randint(p1.size-10, p1.size)
         sizemutation = True
elif p1.size == p2.size:
    size = random.randint(p1.size-5, p2.size+5)
elif p1.size > p2.size:
    size = random.randint(p2.size, p1.size)
    if mfactor >= 95:
        size = random.randint(p1.size, p1.size+10)
        sizemutation = True
    elif mfactor <= 5:
         size = random.randint(p2.size-10, p2.size)
         sizemutation = True

   
mfactor = random.randint(1,100)
if p1.strength < p2.strength:
    strength = random.randint(p1.strength, p2.strength)
    if mfactor >= 95:
        strength = random.randint(p2.strength, p2.strength+10) 
        strmutation = True
    elif mfactor <= 5:
         strength = random.randint(p1.strength-10, p1.strength)
         strmutation = True
elif p1.strength == p2.strength:
    strength = random.randint(p1.strength-5, p2.strength+5)
elif p1.strength > p2.strength:
    strength = random.randint(p2.strength, p1.strength)
    if mfactor >= 95:
        strength = random.randint(p1.strength, p1.strength+10) 
        strmutation = True
    elif mfactor <= 5:
         strength = random.randint(p2.strength-10, p2.strength)
         strmutation = True
         
        
mfactor = random.randint(1,100)
if p1.intelligence < p2.intelligence:
    intelligence = random.randint(p1.intelligence, p2.intelligence)
    if mfactor >= 95:
        intelligence = random.randint(p2.intelligence, p2.intelligence+10)
        intmutation = True
    elif mfactor <= 5:
         intelligence = random.randint(p1.intelligence-10, p1.intelligence)
         intmutation = True
elif p1.intelligence == p2.intelligence:
    intelligence = random.randint(p1.intelligence-5, p2.intelligence+5)
elif p1.intelligence > p2.intelligence:
    intelligence = random.randint(p2.intelligence, p1.intelligence)
    if mfactor >= 95:
        intelligence = random.randint(p1.intelligence, p1.intelligence+10)
        intmutation = True
    elif mfactor <= 5:
         intelligence = random.randint(p2.intelligence-10, p2.intelligence)
         intmutation = True
         
         
print('Parent 1:')
print('Size:',p1.size)
print('Strength:',p1.strength)
print('Intelligence:',p1.intelligence)
print('')


print('Parent 2:')
print('Size:',p2.size)
print('Strength:',p2.strength)
print('Intelligence:',p2.intelligence)
print('')


print('Child:')
if sizemutation == True:
    print('Size:',size, '- MUTATION!')
else:
    print('Size:',size)
if strmutation == True:
    print('Strength:',strength, '- MUTATION!')
else:
    print('Strength:',strength)
if intmutation == True:
    print('Intelligence:',intelligence, '- MUTATION!')
else:
    print('Intelligence:',intelligence)