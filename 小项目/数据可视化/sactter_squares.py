import matplotlib.pyplot as plt

# plt.scatter(2, 4, s=200)  #s调点大小
x=[1,2,3,4,5]
y=[1,4,9,16,25]
x1=list(range(1,11))
y1=[x**2 for x in x1]


# plt.scatter(x1, y1, c="red", edgecolor="none", s=10)   #或者c = (0,0,0.8) 从0-1
plt.scatter(x1, y1, c=y1, cmap=plt.cm.Blues, edgecolor="none", s=10)  #######################颜色映射:  数值越大,颜色越深 参数c设置成了一个依赖值列表 colormap==>cmap
plt.title("picture", fontsize=20)
plt.xlabel("value", fontsize=15)
plt.ylabel("square", fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.axis([0,11,0,101])          ##########设置x,y轴范围

plt.show()

plt.savefig("wwww.png")    ######, bbox_inches="tight"去除多余空白