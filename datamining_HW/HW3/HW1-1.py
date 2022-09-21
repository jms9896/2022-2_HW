import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
rc('font', family="D2Coding")#한글 폰트 지정

import csv

f = open('Seoul.csv', 'r', encoding='cp949')
reader = csv.reader(f)

high_temp_8 = []
low_temp_8 = []
for line in reader:
    if "2022.8" in line[2]:
        high_temp_8.append(line[4])
        low_temp_8.append(line[6])

print(high_temp_8)
print(low_temp_8)

x_val_high = []
y_val_high = []
x_val_low = []
y_val_low = []
for i in range(0, 30):
    y_val_high.append(high_temp_8[i])
    x_val_high.append(i+1)
    y_val_low.append(low_temp_8[i])
    x_val_low.append(i+1)



plt.plot(x_val_high, y_val_high, color='b', label="8월고온")
plt.plot(x_val_low, y_val_low, color='r', label="8월저온")
plt.xlabel('day')
plt.ylabel('temperature')
plt.title('August')
plt.legend()
plt.show()

f.close()