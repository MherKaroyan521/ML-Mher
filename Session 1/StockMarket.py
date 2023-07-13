import matplotlib.pyplot as plt
import numpy
products = ["2022-01-01","2022-01-02","2022-01-03","2022-01-04","2022-01-05","2022-01-06","2022-01-07","2022-01-08","2022-01-09","2022-01-10","2022-01-11","2022-01-12"]

sales = [45.67, 46.12,45.89,45.55,44.92,45.28, 44.76,45.13,45.21,45.49,45.75,46.02]
ret = []
deviation = []
print(numpy.average(sales))

for i in range(1, len(sales)):
  ret.append(sales[i] - sales[i-1])
print(numpy.average(ret))

for i in sales:
  deviation.append(numpy.average(sales) - i)

print(deviation)

plt.plot(products, sales, marker = "o", linestyle = "dotted", color = "green")

plt.xlabel("Data")
plt.ylabel("Price")
plt.title("Price")
plt.show()

plt.plot(products, deviation, marker = "o", linestyle = "dotted", color = "green")

plt.xlabel("Data")
plt.ylabel("Deviation")
plt.title("Deviation Growth")
plt.show()

