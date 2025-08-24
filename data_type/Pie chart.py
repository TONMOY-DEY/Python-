import matplotlib.pyplot as plt

sizes=[30,25,20,25]
labels=['catagory A','catagory B','catagory c','catagory D']

plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.show()