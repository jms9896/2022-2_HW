import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
rc('font', family="D2Coding")#한글 폰트 지정

import csv

f = open('Seoul.csv', 'r', encoding='cp949')
reader = csv.reader(f)

high_temp_1 = []
high_temp_8 = []
for line in reader:
    if "2022-01" in line[2]:
        high_temp_1.append(line[4])
    if "2022-08" in line[2]:
        high_temp_8.append(line[4])


print(high_temp_1)
print(high_temp_8)
x_val_jan_day = []
x_val_aug_day = []

for i in range(1, len(high_temp_1)+1): # 1부터 31까지니까 31개
    x_val_jan_day.append(i)

    if '' != high_temp_1[i-1]: # 실수로 변경
        high_temp_1[i-1] = float(high_temp_1[i-1])
    elif i==1:
        high_temp_1[i - 1] = float(high_temp_1[i])
    elif i==len((high_temp_1)+1):
        high_temp_1[i - 1] = float(high_temp_1[i-2])
    else:
        high_temp_1[i - 1] = (float(high_temp_1[i])+float(high_temp_1[i-2]))/2

for i in range(1, len(high_temp_8)+1):
    x_val_aug_day.append(i)
    if '' != high_temp_8[i - 1]:
        high_temp_8[i - 1] = float(high_temp_8[i - 1])
    elif i == 1:
        high_temp_8[i - 1] = float(high_temp_8[i])
    elif i == (len(high_temp_8) + 1):
        high_temp_8[i - 1] = float(high_temp_8[i - 2])
    else:
        high_temp_8[i - 1] = (float(high_temp_8[i]) + float(high_temp_8[i - 2])) / 2

print(high_temp_8)
print(high_temp_8)


plt.plot(x_val_day, high_temp_8, color='r', label="8월고온")
plt.plot(x_val_day, high_temp_8, color='b', label="8월저온")
plt.xlabel('day')
plt.ylabel('temperature')
#plt.ylim(5, 50)
plt.title('August')
plt.legend()
plt.show()

f.close()