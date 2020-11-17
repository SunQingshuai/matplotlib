import numpy as np
import matplotlib.pyplot as plt

# plt.rcParams['font.size'] = 15
# plt.rcParams['font.family'] = "serif"tdir = 'in'
# major = 5.0
# minor = 3.0
# plt.rcParams['xtick.direction'] = tdir
# plt.rcParams['ytick.direction'] = tdirplt.rcParams['xtick.major.size'] = major
# plt.rcParams['xtick.minor.size'] = minor
# plt.rcParams['ytick.major.size'] = major
# plt.rcParams['ytick.minor.size'] = minor
# plt.rcParams['text.usetex'] = True

# 绘制散点图

N = 50

x = np.linspace(0., 10., N)  # 绘制从零到10的50个数据的数组
y = np.sin(x)**2 + np.cos(x)

plt.figure()
plt.scatter(x, y, s=15, label=r'$y = sin^2(x) + cos(x)$', color='r', marker='x')
plt.axis('equal')  # 使轴比例尺相同


plt.legend()  # 显示图例
plt.xlabel(r'$x$ (rad)')  # 给x、y设置标签
plt.ylabel(r'$y$')
plt.figure(figsize=(7, 7))  # 修改图形尺寸

# 保存图形
# plt.savefig('name.png', dpi=300, bbox_inches='tight', facecolor='w')
plt.show()




