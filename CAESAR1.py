# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 21:15:51 2021

@author: Don
"""

alpha ="ABCEDEFGHIJKLMNOPQRSTUVWXYZ"
str_ln = input("Enter messagem like HELLO:")
n = len(str_ln)
str_out = ""
for i in range(n):
    c = str_ln[i]
    loc = alpha.find(c)
    print(str(i) + ":" + str(c) + " " +str(loc))
    newloc = loc + 3
    str_out += alpha[newloc]
    print(str(newloc) + ":" + str(str_out))
print("Obsfuscated version " + str(str_out))