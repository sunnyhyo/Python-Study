# -*- coding: utf-8 -*-
"""
Created on Sun May 13 16:29:10 2018

@author: HS
"""

#%% 4.1.1

import math 

def myfun(x,y):
    a=math.cos(3*(x-1))+\  #해당 줄이 끝나지 않았음 , 들여쓰기 무시
    math.sin(3*(y-1))
    
    return a

x,y=2.0,5.0
print("myfun(x,y)=%f" %myfun(x,y))

#%% 4.1.1 4.2 들여쓰기

def myfunc(n,b):
    x=n%b
    if x==0:
        return 1
    else:
        return 0
    
n=123456
b=3

myfunc(n,b)

#%% 데이터 타입
my_list = [4,6,"pencil", 3.2+4.5j, [3,4]]
my_list[2]="ball"
print(my_list)

my_tup=(4,6,"pencil", 3.2+4.j, [3,4])
my_tup[2]="ball"
#%%
my_dic={"kenji":41, "koji":14, "yasuko":37, "nobu":40 }
my_dic["kenji"]

a_set={1,2,3} #집합생성

b_list=["a",2,True,3+2j,2]  #리스트 생성
b_set=set(b_list)  #집합생성
print(b_set)

c_set=set()  #빈 집합을 생성
c_set.add(3)  #집합에 데이터를 추가
print(c_set)  

fs=frozenset(['d',7,5.6j])
print(fs)

#%%
mystr='이것이 문자열 리터럴입니다.'
print(mystr)
mystr="이것이 문자열 리터럴입니다."
mystr = '''이런 방법으로 
작성할 수도
있습니다'''

#%%
mystr="Python is \
easy to learn"
print(mystr)

