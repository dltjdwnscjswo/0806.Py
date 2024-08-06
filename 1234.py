import matplotlib.pyplot as plt
data = [65,70,70,75,80,85,85]
data2 = [17,18,19,20,21,22,23]

plt.plot(data2,data,marker="*",linestyle="-",color="red",label="temp")
plt.title("금일 습도 표시")
plt.xlabel("시간 (h)")
plt.ylabel("습도 (%)")
plt.show()