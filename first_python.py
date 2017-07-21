# -*- coding: utf-8 -*-
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

def triangles():
	list = [1]
	i = -1
	while True:
		yield list
		i = i + 1
		j = i
		while j > 0:
			list[j] = list[j] + list[j - 1]
			j = j - 1
			pass
		pass
		list.append(1)
n = 0
for t in triangles():
	print (t)
	n = n +1
	if n == 10:
		break



