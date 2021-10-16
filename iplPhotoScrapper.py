import requests
import os

if os.path.isdir('imagesIPL'):
    os.chdir('imagesIPL')
else:
    os.makedirs('imagesIPL')
    os.chdir('imagesIPL')

pages=int(input('how many pages to scrape? per page has 100 images >'))
imageData=list()
for page in range(pages):
    url='https://api.platform.iplt20.com/content/ipl/video/EN/?pageSize=100&page='+str(page)
    r=requests.get(url)
    print('statuscode for page',str(page+1),'is >>> ',r.status_code)
    data=r.json()['content']
    if len(data)>0:
        for image in data:
            item={
                'title':image.get('title','noTitle'),
                'desc':image.get('description','noDescription'),
                'thumbURL':image.get('thumbnailUrl','noThumbnail'),
                'thumbCaption':image.get('titleUrlSegment','noCaption')
            }
            imageData.append(item)

            # store data into imagesIPL
            if item['thumbURL']!='noThumbnail':
                with open(item['thumbCaption']+'.jpg','wb') as image:
                    r=requests.get(item['thumbURL'])
                    image.write(r.content)


