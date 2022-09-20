import matplotlib.pyplot as plt

x = [1,2,3,4,5]
squares = [-1, 4, 9, 16, 25]

plt.plot(x, squares, "rd-.", linewidth = 3)    #r红,d菱形,  -.点划线
plt.title("picture", fontsize=20)
plt.xlabel("value", fontsize=15)
plt.ylabel("square", fontsize=15)
plt.xlim(-1, 10)            ######设置x范围
plt.yscale("linear")
# plt.xticks(fontsize = 10)
# plt.yticks(fontsize = 10)
# plt.yscale('log')  对数

#设置刻度标记的大小
plt.tick_params(axis='both', labelsize=10)
plt.show()