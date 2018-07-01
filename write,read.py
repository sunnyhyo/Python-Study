# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 22:12:35 2018

@author: HS PARK
"""


####파일 쓰고 읽기 
f=open(".\\test.csv","w")
for i in range(1,20):
    a= "%d 번째 줄입니다. \n" %i
    f.write(a)
f.close()

f=open(".\\test.csv", "r")
while True:
    line=f.readline()
    if not line: break
    print(line)
f.close()

c=[]
for i in range(1,30):
    b= "%d 번째 줄입니다.\n" %i
    c+=b
    
with open(".\\test2.csv","w") as f:
    f.writelines(c)
with open(".\\test2.csv","r") as f:
    data=f.read()
    print(data)
    