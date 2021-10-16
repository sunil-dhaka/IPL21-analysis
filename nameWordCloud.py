from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np

data=pd.read_csv('datasets/playerdata.csv')
nameData=' '.join(list(data['fullName']))
# print(nameData)

'''
create tropper mask used PIL.Image
create word cloud with mask
image show
'''
tropperMask=np.array(Image.open('plots/stormtrooper_mask.png')) 
wordCloud=WordCloud(collocations=False,max_font_size=40,min_word_length=3,background_color='white',mask=tropperMask).generate(nameData)
# print(wordCloud)

plt.imshow(wordCloud,interpolation='bilinear')
plt.axis('off')
plt.savefig('plots/nameCloud.png')
plt.show()