#coding:utf-8
'''
print 'Exercise2.4.1'
import math
r = raw_input('Semidiameter=')

r = float(r)
V = 4/3 * math.pi * r**3
print V
##############################
print 'Exercise2.4.2'
p = float(raw_input('price = '))
dis = float(raw_input('discount = '))
count = int(raw_input('total number = '))
cost_book = count*p*dis
cost_post = 3 + (count-1)*0.75
cost = cost_book + cost_post
print '总共需要',cost,'元'
############################
print 'Exercise2.4.3'
'''
import math
print 2*(2**0.5)*(math.pi)