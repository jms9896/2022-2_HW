import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
rc('font', family="D2Coding")#한글 폰트 지정

import csv

f = open('Seoul.csv', 'r', encoding='cp949')
reader = csv.reader(f)
total = []
for line in reader:
    total.append(line[3])
total.remove(total[0])
y_val = []
x_val = []
for i in range(0, 30):
    y_val = total[i]
    x_val.append(i+1)



plt.plot(x_val, y_val)
plt.xlabel('날짜')
plt.ylabel('평균기온')
plt.title('날짜별 평균기온')
#plt.legend()
plt.show()

f.close()