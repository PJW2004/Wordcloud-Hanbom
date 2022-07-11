import os

user = input()
try:
    import numpy as np
    from PIL import Image
    import defalt
    wc = defalt.data_create(width=800, hight=800, user=user, mask=img_array)
    img = Image.open('./sampleImage/img.jpg')
    img_array = np.array(img)
    defalt.image_show(wc=wc)

except ModuleNotFoundError:
    os.system('pip install -r requirements.txt')
