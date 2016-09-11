#coding:utf-8

##print "s",and let the last character of "s" in the 70th column
def right_justify(s):
	a = int(len(s))
	num_space = 69 - a
	space = ' '
	print(space*num_space,s)

right_justify('hello')
