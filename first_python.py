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

def person(name,age,*,city,job):
	print('name:', name, 'age:', age, 'other:', kw)
dict = {'addr':'Chaoyang', 'zipcode':123456,'city':'成都','job':'IT'}
person('chuan',city='13232',job='IIT')