import matplotlib.pyplot as plt

label=['category A','category B','category c','category D']
values=[25,40,25,10]

plt.bar(label,values)
plt.title('Bar chart')
plt.xlabel(label)
plt.ylabel(values)
plt.show()