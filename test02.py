import matplotlib.pyplot as plt
import numpy as np

np.random.seed(100)

N = 15

randx = np.random.random(N)*100
randy = np.random.random(N)*100

plt.scatter(randx, randy,marker=r'$\beta$', s = 150, color='darkorange')
plt.axis('equal')
plt.xlabel('randx')
plt.ylabel('randy')
plt.tight_layout()
plt.show()