import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [ 10,15,13,18,20]

plt.plot(x,y,marker="*",linestyle="-",color="red",label="temp")
plt.title("Daily temperature trend")
plt.show()