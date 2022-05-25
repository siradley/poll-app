import matplotlib.pyplot as plt

plt.figure()

plt.xlabel("Categories")
plt.ylabel("Amounts")
plt.title("Categories vs. Amounts")

# k is the color for black. o is to plot the graph with a dot. default is a line graph
plt.plot([1, 2, 3, 4], [3, 5, 9, 25])  # , "ko"
# plt.setp(lines, color="#ff5566")
plt.show()
