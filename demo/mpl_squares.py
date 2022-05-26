# encoding:utf-8
import matplotlib.pyplot as plt

# 需要绘图的数据
squares = [1, 4, 9, 16, 25]
# 通用方法获取整张图片fig 和 数据 ax
fig, ax = plt.subplots()
# 把数据填充进去
ax.plot(squares)
# 展示
plt.show()

