<<<<<<< HEAD
=======
# 2015251165 정민성 HW1-1

>>>>>>> aa7fadecc158b5cb762ad18bec2fd554d0ce9717
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
rc('font', family="D2Coding")#한글 폰트 지정

import csv

f = open('Seoul.csv', 'r', encoding='cp949')
reader = csv.reader(f)

high_temp_8 = []
low_temp_8 = []
for line in reader:
<<<<<<< HEAD
    if "2022-08" in line[2]:
=======
    if "2022.8" in line[2]:
>>>>>>> aa7fadecc158b5cb762ad18bec2fd554d0ce9717
        high_temp_8.append(line[4])
        low_temp_8.append(line[6])

print(high_temp_8)
print(low_temp_8)
x_val_day = []

<<<<<<< HEAD
for i in range(1, len(high_temp_8)): #1부터 31까지니까 31개
    x_val_day.append(i + 1)
    if '' not in high_temp_8:
        high_temp_8[i-1] = float(high_temp_8[i-1])
    if '' not in low_temp_8:
        low_temp_8[i-1] = float(low_temp_8[i-1])
=======
for i in range(1, len(high_temp_8)+1): # 1부터 31까지니까 31개
    x_val_day.append(i)
    if '' != high_temp_8[i-1]: # 실수로 변경
        high_temp_8[i-1] = float(high_temp_8[i-1])
    elif i==1:
        high_temp_8[i - 1] = float(high_temp_8[i])
    elif i==len((high_temp_8)+1):
        high_temp_8[i - 1] = float(high_temp_8[i-2])
    else:
        high_temp_8[i - 1] = (float(high_temp_8[i])+float(high_temp_8[i-2]))/2


    if '' != low_temp_8[i-1]:
        low_temp_8[i-1] = float(low_temp_8[i-1])
    elif i == 1:
        low_temp_8[i - 1] = float(low_temp_8[i])
    elif i == (len(high_temp_8) + 1):
        low_temp_8[i - 1] = float(low_temp_8[i - 2])
    else:
        low_temp_8[i - 1] = (float(low_temp_8[i]) + float(low_temp_8[i - 2])) / 2

>>>>>>> aa7fadecc158b5cb762ad18bec2fd554d0ce9717
print(high_temp_8)
print(low_temp_8)


<<<<<<< HEAD
plt.plot(x_val_day, high_temp_8, color='b', label="8월고온")
plt.plot(x_val_day, low_temp_8, color='r', label="8월저온")
=======
plt.plot(x_val_day, high_temp_8, color='r', label="8월고온")
plt.plot(x_val_day, low_temp_8, color='b', label="8월저온")
>>>>>>> aa7fadecc158b5cb762ad18bec2fd554d0ce9717
plt.xlabel('day')
plt.ylabel('temperature')
#plt.ylim(5, 50)
plt.title('August')
plt.legend()
plt.show()

f.close()