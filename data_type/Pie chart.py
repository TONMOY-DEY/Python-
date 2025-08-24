import matplotlib.pyplot as plt

size=[30,45,25]
labels=['category A','category B','category C']

plt.pie(size,labels=labels,autopct='%1.1f%%')
plt.title('pie Chart')
print('........')
plt.show()