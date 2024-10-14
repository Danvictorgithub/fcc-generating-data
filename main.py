import matplotlib.pyplot as plt

input_values = [1,2,3,4,69420]
squares = [1,4,9,16,25]

plt.style.use('bmh')
fig, ax = plt.subplots()
ax.scatter(input_values,squares,s=100)
# ax.plot(input_values,squares, linewidth=10)
# ax.set_title("Square Numbers",fontsize=24)
# ax.set_xlabel("Value",fontsize=14)
# ax.set_ylabel("Square of Value",fontsize=14)

plt.show()