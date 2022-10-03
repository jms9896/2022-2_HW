from random import randint
import matplotlib.pyplot as plt

data1 = []
data2 = []
for i in range(30):
    data1.append(randint(1, 100))
    data2.append(randint(1, 50))

plt.boxplot([data1, data2])
plt.show()