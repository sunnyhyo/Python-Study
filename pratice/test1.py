# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os 


os.chdir("C:\\Users\\HS\\Documents\\GitHub\\analysing-super-heros-data")
os.getcwd()

#1. readline() 함수 이용하기
#1.1 첫 줄 읽기
f=open(".\\data\\heroes_information.csv", "r")
line= f.readline()
print(line)
f.close

#1.2 모든 라인 읽어서 화면에 출력
f=open(".\\data\\heroes_information.csv", "r")
while True:             #무한 루프 안에서
    line=f.readline()   #f.readline() 이용하여 파일을 계속 한 줄씩 읽어들임
    if not line:        #만약 더이상 읽을 라인이 없으면 break 수행
        break
    print(line)
f.close


#2. readlines() 함수 이용하기
#2.1

f=open(".\\data\\heroes_information.csv", "r")
lines = f.readlines()       
#파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 리스트로 리턴
for line in lines:      #lines는 줄을 리스트 요소로 갖는다.
    print(line)
f.close()

print(lines)

#3. read() 함수 이용하기
f=open(".\\data\\heroes_information.csv", "r")
data = f.read()     #f.read()는 파일의 내용 전체를 문자열로 리턴한다
print(data)         #data는 파일의 전체 내용이다
f.close()


#파일에 새로운 내용 추가하기
f=open(".\\data\\heroes_information.csv", "a")
for i in range(1,10):
    data="%d번째 줄입니다. \n"%i
    f.write(data)
f.close()

with open(".\\data\\heroes_information.csv", "a") as f:
    f.write("life is too short")

f=open(".\\data\\heroes_information.csv", "r")
while True:
    line= f.readline()
    if not line: 
        break
    print(line)
f.close()

a=[str(k) for k in range(1,6)]
with open(".\\data\\new.csv","w") as f :
    for i in range(1,20):
        data="%d번째 줄입니다. \n" %i
    f.write(data)
    f.writelines(a)   #리스트 추가하기

with open('.\\data\\new.csv','r') as f:
    wholefile=f.read()
    print(wholefile)



