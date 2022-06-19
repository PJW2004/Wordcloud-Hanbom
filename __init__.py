import defalt
import os

user = input()
try:
    wc = defalt.data_create(width=800, hight=800, user=user)

    defalt.image_show(wc=wc)

except ModuleNotFoundError:
    os.system('pip install -r requirements.txt')