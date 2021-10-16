import requests
import json

'''
pageSize changed to 50 so that teams that might have players more than 30 also can be covered
'''
def teamPlayerStats(id):
    baseURL='https://cricketapi.platform.iplt20.com/stats/players?teamIds='+str(id)+'&tournamentIds=22399&pageSize=50'
    r=requests.get(baseURL)
    print('status code for team ',id,'is >>> ',r.status_code)

    data=r.json()['stats']['content']
    modifiedData=list()
    '''
    list ompressions modifiedData=[player for player in data player['teamID]=id]
    '''
    for player in data:
        player['teamID']=id
        modifiedData.append(player)

    return modifiedData

'''
get teams data
ipl221 tournament id is >>> 22399
'''

teamsURL='https://cricketapi.platform.iplt20.com/teams?&tournamentIds=22399'

teamReaponse=requests.get(teamsURL)
print('teams response status >>> ',teamReaponse.status_code)
teamsData=teamReaponse.json()['content'] #< -- list of dicts

# teamIDs=[team['id'] for team in teamsData]

'''
for future identification I am going to add a teamId key-value to each player
so each player now will have two ids: teamId and playerId
'''
playerData=list()

# also can be used list compressions
for team in teamsData:
    id = team['id']
    statsData=teamPlayerStats(id)
    team['playerCount']=len(statsData) #  <-- adds new keys that shows total no of players in each team in 2021 season
    playerData.extend(statsData)
    # print(team['playerCount'])
print('Total players playing in IPL2021 are ',len(playerData))

with open('playerStats.json','w') as file1,open('teamsData.json','w') as file2:
    json.dump(playerData,file1)
    json.dump(teamsData,file2)

'''
dump for lists
dumps for strings
'''