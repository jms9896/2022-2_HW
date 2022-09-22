import matplotlib.pyplot as plt

x_val = [1,2,3,4]
y_val = [1,4,9,16]

plt.plot(x_val, x_val, color='b', label='y=x')
plt.plot(x_val, y_val, color='r', label='y=x**2')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('graph')
plt.legend()
plt.show()
