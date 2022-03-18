# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 21:15:51 2021

@author: Don
"""

alpha ="ABCEDEFGHIJKLMNOPQRSTUVWXYZ"
str_ln = input("Enter messagem like HELLO:")
shift = input("Shift value like 3:")
shift = int(shift)
n = len(str_ln)
str_out = ""
for i in range(n):
    c = str_ln[i]
    loc = alpha.find(c)
    newloc = (loc + shift)%26
    str_out += alpha[newloc]

print("Obsfuscated version " + str(str_out))