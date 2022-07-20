import abel
import numpy as np
from PIL import Image

original = Image.open('gg1.bmp')
nporiginal = np.asarray(original)
forward_abel = abel.Transform(nporiginal, origin='com', direction='forward', method='hansenlaw').transform
inverse_abel = abel.Transform(nporiginal, origin='com', direction='inverse', method='three_point').transform


import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2, figsize=(6, 3))

axs[0].imshow(forward_abel, clim=(0, None), cmap='ocean_r')
axs[1].imshow(inverse_abel, clim=(0, None), cmap='ocean_r')

axs[0].set_title('Forward Abel transform')
axs[1].set_title('Inverse Abel transform')

plt.tight_layout()
plt.show()