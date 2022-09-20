import matplotlib.pyplot as plt
from random_walk import Randomwalk



rw = Randomwalk(5000)    #增加点数到5000
rw.fill_walk()

plt.figure(dpi=128, figsize=(10,6))       #窗口大小
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_value, rw.y_value, c=point_numbers,cmap=plt.cm.Blues, edgecolors='none', s=10)    ###颜色映射

plt.scatter(0,0, c='red',s=52)
plt.scatter(rw.x_value[-1],rw.x_value[-1],c="blue",s=52)  #突出起点和终点

# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)             ############隐藏x,y轴

plt.show()


