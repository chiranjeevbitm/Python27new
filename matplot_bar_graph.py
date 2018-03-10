from matplotlib import pyplot as plt
plt.bar([1,3,5,7,9],[5,7,2,8,2],label='line one')

plt.bar([2,4,6,8,10],[8,6,2,5,4],label='line one',color='b')

plt.title('Epic info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.legend()
#plt.grid(True,color='g')
plt.show()