#!/usr/bin/env python

year=input()

print (year%400==0) or (year%4==0 and year%100!=0)
 
