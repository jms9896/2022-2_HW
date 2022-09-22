# 2015251165 정민성 HW1-2

import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
rc('font', family="D2Coding")#한글 폰트 지정

import csv

f = open('Seoul.csv', 'r', encoding='cp949')
reader = csv.reader(f)

high_temp_1 = [] # 1월
high_temp_8 = [] # 8월
for line in reader:
    if "2022.1" in line[2]:
        high_temp_1.append(line[4]) # 1월 최고기온 모음집
    if "2022.8" in line[2]:
        high_temp_8.append(line[4]) # 8월 최고기온 모음집


print(high_temp_1)
print(high_temp_8)
for i in range(len(high_temp_1)):
    high_temp_1[i] = float(high_temp_1[i])
    high_temp_8[i] = float(high_temp_8[i])

plt.hist(high_temp_1, color='b', bins = len(high_temp_1))
plt.hist(high_temp_8, color='r', bins = len(high_temp_8))


x_val_jan_day = []
x_val_aug_day = []
plt.ylabel('num of days')
plt.xlabel('temperature')
plt.title('January and August')
plt.show()

f.close()