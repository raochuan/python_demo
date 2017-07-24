# -*- coding: utf-8 -*-
from functools import reduce
#first 第一个Python程序
#a = 100
#if a>= 0:
#    print(a)
#else:
 #   print(-a)

#print('I\'m ok !')


#L = ['aaa','bbb','ccc']
#for x in L:
 #   print('hello,%s'%x)


#def my_max(a):
#	if a>=0:
#		return a
#	else:
#		return -a
#my_max(10)



#def  enroll(name,gender,age=6,city='北京'):
    # print('name:',name)
    # print('gender:',gender)
#     print('age:',age)
#     print('city:',city)	
# enroll('Adam','M','8','siChuan')

# def person(name,age,*,city,job):
# 	print('name:', name, 'age:', age, 'other:', kw)
# dict = {'addr':'Chaoyang', 'zipcode':123456,'city':'成都','job':'IT'}
# person('chuan',city='13232',job='IIT')

# def fib(max):
# 	n,a,b = 0,0,1
# 	while n < max:
# 		yield b
# 		a,b = b,a+b
# 		n = n+1
# 	return 'doen'

# f = fib(6)
# for n in f:
# 	print (n)

# def triangles():
# 	list = [1]
# 	i = -1
# 	while True:
# 		yield list
# 		i = i + 1
# 		j = i
# 		while j > 0:
# 			list[j] = list[j] + list[j - 1]
# 			j = j - 1
# 			pass
# 		pass
# 		list.append(1)
# n = 0
# for t in triangles():
# 	print (t)
# 	n = n +1
# 	if n == 10:
# 		break
name = ['adam', 'LISA', 'barT'];
def normalize(name):
	b = [];
	i = 0;
	for n in name:
		if i == 0:
			b.append(n.upper())
			pass
		else:
			b.append(n.lower())
		i = i+ 1
	pass
	return b

result = map(normalize,name)
print (result)

def add (x,y):
	return x * y
result = reduce(add,[1,3,4,7,9])


# L = [3, 5, 7, 9];
# def prod(L):
# 	def multiply(x,y):
# 		return x * y
#     return reduce(multiply,L)
# result = prod(L)
# print (result)
f = '12993.45699'
def str2float(s):
	def multy(x):
		f = 1;
		while x:
			f = f* 0.1
			x = x - 1;
		return  f
	def add(x,y):
		return  x + y
	def fn(x,y):
		return  x * 10 +y
	def char2num(x):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':None}[x]
	def dot(s):
		t = list(map(char2num,s))
		n = s.find('.')
		a = reduce(fn,t[0:n])
		b = reduce(fn,t[n+1:])
		return [a,b*multy(len(t[n+1:]))]
	return  reduce(add,dot(s))
print (str2float(f));


