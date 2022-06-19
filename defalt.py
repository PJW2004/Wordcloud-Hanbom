import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

import matplotlib.font_manager as fm
import re
import collections
import os

os.system('pip install -r requirements.txt')