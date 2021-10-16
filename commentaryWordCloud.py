'''
import modules
'''
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, wordcloud
import numpy as np
import requests
import string
from nltk import corpus
'''
collect data
'''
stopwords=corpus.stopwords.words('english')
commText=[]
for feed in range(1,10): #<-- for general case needs condition when feed goes in nothing[no commentary feed no] territory
    url=f'https://cricketapi.platform.iplt20.com/fixtures/32242/commentary/feeds/{feed}?customer=bcci'
    r=requests.get(url)

    comments=r.json()['commentaries']
    for comment in comments:
        '''
        text cleaning:
        1. lower case all words
        2. avoid '' cases
        3. split by whitspaces
        4. list compression words conditions:
            - avoid stopwords
            - avoid letters(len=1)
            - avoid words with '['or ']' in them
            - avoid words with numbers in them <--https://stackoverflow.com/questions/19859282/check-if-a-string-contains-a-number
        5. strip all puctuations from start nd end of words # optional
        6. if word had apostrophy replace that with '' # optional
        7. others possible steps
                Remove URLs
                Remove HTML tags
                Remove emojis
        '''
        text=comment.get('bbcode','').lower()
        if text != '':
            text=text.split(' ') #< this way don't get puctuations
            text=[str(foo.strip(string.punctuation)) for foo in text if (foo not in stopwords) and (len(foo)>1) and (('[' or ']') not in foo) and (not any(c.isdigit() for c in foo))]
            # text=text.strip(string.punctuation)
            commText.extend(text)

# print(commText)

# count frequencies

def freqCounter(myList):
    countDict={}

    for ele in myList:
        countDict[ele]=countDict.get(ele,0)+1
    return countDict

commTextDict=freqCounter(commText)
'''
create tropper mask used PIL.Image
create word cloud with mask
image show
'''

indiaMask=np.array(Image.open('plots/indiaMask.jpg'))
'''
when using generate I am consistently getting this error:
TypeError: expected string or bytes-like object
But as per my knowledge all eles are strings; there is no floats
also did not help<-- https://stackoverflow.com/questions/39469711/typeerror-expected-string-or-bytes-like-object-pandas-variable
wordCloud=WordCloud(background_color='white',mask=indiaMask).generate(commText)
'''

wordCloud=WordCloud(background_color='white',mask=indiaMask).fit_words(commTextDict)
plt.imshow(wordCloud,interpolation='bilinear')
plt.axis('off')
plt.savefig('plots/commentCloud.png')
plt.show()