import matplotlib.pyplot as plt

products = ["2022-01-01","2022-01-02","2022-01-03","2022-01-04","2022-01-05","2022-01-06","2022-01-07","2022-01-08","2022-01-09","2022-01-10","2022-01-11","2022-01-12"]

sales = [45.67, 46.12,45.89,45.55,44.92,45.28, 44.76,45.28,44.76,45.13,45.21,45.49,45.75,46.02]

plt.bar(products, sales, color = ["red","blue","green","orange"])
plt.xlabel("Date")
plt.ylabel("Closing Price($)")
plt.title("Sales Data")
plt.legend(["Sales"])
plt.show()
