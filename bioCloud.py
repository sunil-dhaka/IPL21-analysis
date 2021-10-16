'''
import modules
'''
from PIL import Image
import matplotlib.pyplot as plt
from requests.api import head
from wordcloud import WordCloud, wordcloud
import numpy as np
import requests
import string
from nltk import corpus

stopwords=corpus.stopwords.words('english')
bioText=[]

'''url = "https://api.platform.iplt20.com/content/ipl/bios/EN/"

querystring = {"pageSize":"700","fullObjectResponse":"true"}
'''
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.iplt20.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Referer": "https://www.iplt20.com/",
    "Connection": "keep-alive",
    "TE": "trailers"
}

# response = requests.request("GET", url,  headers=headers, params=querystring)


for page in range(7):
    url='https://api.platform.iplt20.com/content/ipl/bios/EN/?pageSize=100&page='+str(page)+'&fullObjectResponse=true' #<-- got all bios in one go
    try:
        r=requests.get(url,headers=headers)
        print('status for page ',str(page+1),'is >>>',r.status_code)
        textData=r.json()['content']
        for text in textData:
            bio=text.get('content','').lower()
            if bio != '':
                bio=bio.split(' ')
                bio=[str(foo.strip(string.punctuation)) for foo in bio if (foo not in stopwords) and (len(foo)>1)]
                bioText.extend(bio)
    except:
        print('failed')
        # exit()

def freqCounter(myList):
    countDict={}

    for ele in myList:
        countDict[ele]=countDict.get(ele,0)+1
    return countDict

bioTextDict=freqCounter(bioText)

indiaMask=np.array(Image.open('plots/indiaMask.jpg'))
wordCloud=WordCloud(background_color='white',mask=indiaMask).fit_words(bioTextDict)

plt.imshow(wordCloud) #<-- additional params also can be specified see imshow() docs
plt.axis('off')
plt.savefig('plots/bioCloud.png')
plt.show()

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