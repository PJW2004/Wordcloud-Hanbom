import os
import numpy as np
from PIL import Image

user = input()
img = Image.open('img.jpg')
img_array = np.array(img)
try:
    import defalt
    wc = defalt.data_create(width=800, hight=800, user=user, mask=img_array)

    defalt.image_show(wc=wc)

except ModuleNotFoundError:
    os.system('pip install -r requirements.txt')