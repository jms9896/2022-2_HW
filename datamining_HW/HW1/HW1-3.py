import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
rc('font', family="D2Coding")#한글 폰트 지정

import csv

f = open('Seoul.csv', 'r', encoding='cp949')
reader = csv.reader(f)

avg_temp = [] # 1월부터 8월까지 다 때려넣을 전체리스트 생성
for i in range(9):
    avg_temp[i]=[] #0번째 비워두기, 1~8월 리스트 생성

for line in reader:
    for i in range(1, 9):
        if f"2022-0{i}" in line[2]: # 평균기온은 3번째
            avg_temp[i].append(line[3]) # 1~8월 평균기온 모음집
print(avg_temp)
plt.boxplot(avg_temp)

plt.xlabel('month')
plt.ylabel('temperature')
plt.title('January and August')
plt.show()

f.close()