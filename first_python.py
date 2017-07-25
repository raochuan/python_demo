# -*- coding: utf-8 -*-
from functools import reduce
import  functools
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
# name = ['adam', 'LISA', 'barT'];
# def normalize(name):
# 	b = [];
# 	i = 0;
# 	for n in name:
# 		if i == 0:
# 			b.append(n.upper())
# 			pass
# 		else:
# 			b.append(n.lower())
# 		i = i+ 1
# 	pass
# 	return b
#
# result = map(normalize,name)
# print (result)
#
# def add (x,y):
# 	return x * y
# result = reduce(add,[1,3,4,7,9])


# L = [3, 5, 7, 9];
# def prod(L):
# 	def multiply(x,y):
# 		return x * y
#     return reduce(multiply,L)
# result = prod(L)
# print (result)
# f = '12993.45699'
# def str2float(s):
# 	def multy(x):
# 		f = 1;
# 		while x:
# 			f = f* 0.1
# 			x = x - 1;
# 		return  f
# 	def add(x,y):
# 		return  x + y
# 	def fn(x,y):
# 		return  x * 10 +y
# 	def char2num(x):
# 		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':None}[x]
# 	def dot(s):
# 		t = list(map(char2num,s))
# 		n = s.find('.')
# 		a = reduce(fn,t[0:n])
# 		b = reduce(fn,t[n+1:])
# 		return [a,b*multy(len(t[n+1:]))]
# 	return  reduce(add,dot(s))
# print (str2float(f));

#奇数生成
# def odd_iter():
# 	n = 1
# 	while True:
# 		n = n + 2
# 		yield  n
#
#
# def not_divisible(n):
# 	return lambda x: x %n > 0
#
# def primes():
# 	yield  2
# 	it = odd_iter()
# 	while True:
# 		n = next(it)
# 		yield  n
# 		it = filter(not_divisible(n),it)
# for n in primes():
# 	if n < 1000:
# 		print(n)
# 	else:
# 		break


# def is_palindrome(n):
# 	a = str(n)
# 	b = a[::-1]
# 	return  a == b
#
# output = filter(is_palindrome,range(10000,100000))
# print (list(output))

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# # def by_name(t):
# # 	return  t[-1]
# # 	pass
#
# L2 = sorted(L,key=lambda t:t[-1])
# print (L2)

# def lazy_sum(*args):
# 	def sum():
# 		ax = 0
# 		for n in args:
# 			ax = n + ax
# 		return  ax
# 	return  sum
#
# f = lazy_sum([1,3,5,7,9])
# a = f()
# print (a)

#闭包
# def count():
# 	fs = []
# 	for i in range(1,4):
# 		def f():
# 			return  i* i
# 		fs.append(f)
# 	return fs
# f1,f2,f3 = count()
# print (f1(),f2(),f3())

# def count():
# 	def f(j):
# 		def g():
# 			return  j*j
# 		return  g
# 	fs = []
# 	for i in range(1,4):
# 		fs.append(f(i))
# 	return  fs
# f1,f2,f3 = count()
# print (f1(),f2())

def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print ('call %s():' % func.__name__)
		return func(*args,**kw)
	return  wrapper
@log
def now():
	print ("2017-7-25")

@log
def test():
	print ("test---log")
now();
test();

print (now.__name__,test.__name__);


def log(text = '默认值'):
	def decorator_test(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print ('start有参数的logo %s-- %s():' %(text,func.__name__))
			func(*args,**kw)
			print ('end有参数的logo %s-- %s():' % (text, func.__name__))
			return
		return wrapper
	return decorator_test

@log()
def now():
	print ("2017-7-25")

@log('now_test')
def test():
	print ("test---log")
now();
test();

print (now.__name__,test.__name__);
