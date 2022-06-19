import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

import matplotlib.font_manager as fm
import re
import collections
import os

os.system('pip install -r requirements.txt')

def data_create(width=0, hight=0, user=None):
    url = f'https://www.google.com/search?q={user}'
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    text = soup.text

    # wordcloud excute code
    wc1 = WordCloud(max_font_size=200, font_path='./font/malgun.ttf',
                    background_color='white', width=width, height=hight)

    wc1.generate(text)

def image_show():
    # image create and show to window
    plt.figure(figsize=(10,8))
    plt.imshow(wc1)
    plt.tight_layout(pad=0)
    plt.axis('off')
    plt.show()