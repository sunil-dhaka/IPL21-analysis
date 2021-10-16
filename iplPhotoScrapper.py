import requests

# current season ipl data url>> gets json data

url='https://api.platform.iplt20.com/content/ipl/video/EN/?'

r=requests.get(url)

print(r.status_code)
data=r.json()['content']

print(len(data))
print(data)
