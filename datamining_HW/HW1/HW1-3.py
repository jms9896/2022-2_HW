# 2015251165 정민성 HW1-3

import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
rc('font', family="D2Coding")#한글 폰트 지정

import csv

f = open('Seoul.csv', 'r', encoding='cp949')
reader = csv.reader(f)

avg_temp = [] # 1월부터 8월까지 다 때려넣을 전체리스트 생성
for i in range(8):
    avg_temp.append([]) # 1~8월 빈 리스트 생성
print(avg_temp)
for line in reader:
    '''for i in range(1, 9): # 안 해 에러 너무많음
        # print(f"2022.{i}")
        # print(line[2])
        if (f"2022-{i}") in line[2]: # 날짜는 2번째, 평균기온은 3번째
            #print(f"2022.{i}")
            print(line[3])
            avg_temp[i-1].append(line[3]) # 1~8월 평균기온 모음집
    '''
    for i in range(8):
        if f"2022.{i+1}" in line[2]:
            avg_temp[i].append(line[3])

print(avg_temp)
for i in range(8):
    for j in range(len(avg_temp[i])):
        avg_temp[i][j] = float(avg_temp[i][j])
print(avg_temp)
plt.boxplot([avg_temp[0],avg_temp[1],avg_temp[2],avg_temp[3],avg_temp[4],avg_temp[5],avg_temp[6],avg_temp[7]])

plt.xlabel('month')
plt.ylabel('temperature')
plt.title('January and August')
plt.show()

f.close()