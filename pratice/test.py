# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
f = open("음음.csv", 'r')  # 날짜 파일 입력
output = ""
oh = []
while True:
    line = f.readline()
    if not line:
        break
    if len(str(line).split(',')[9])>1:
        print(str(line).split(',')[9])
        output+=str(line).split(',')[2]
        output+="\n"
f.close()
f = open("음음_output.csv", 'w')
f.write(output)
f.close()
# print(output)