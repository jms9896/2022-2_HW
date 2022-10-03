import matplotlib.pyplot as plt


plt.title('August')

with open('Seoul_test.csv', 'r', encoding='cp949') as file:
    file.readline()
    data=[]
    high_C = []
    low_C = []
    for line in file:
        data.append(line.strip().split(','))
    print(data)
    for i in range(len(data)):
        if data[i][2].split('.')[1] == '8':
            print(data[i][4])
            if data[i][4] != '':
                high_C.append(float(data[i][4]))
            if data[i][6] != '':
                low_C.append(float(data[i][6]))
    print(high_C)
    print(low_C)

plt.xlabel('day')
plt.ylabel('temperature')
plt.plot(high_C, 'red', label= 'highest temp')
plt.plot(low_C, 'blue', label= 'lowest temp')
plt.legend()
plt.show()