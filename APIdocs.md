- to get tornament IDs: can change page size(max 100) to get more in one go, to get more pages change page(starts from 0); basically changes entries in pageInfo
```
https://cricketapi.platform.iplt20.com/tournaments
```

- to get teams info in a tornament: mainly tour ID changes
```
https://cricketapi.platform.iplt20.com/teams?teamIds=1&tournamentIds=22399&scope=TOURNAMENT&pageSize=30
```
- to get teams stats in a tour: team id changes
```
https://cricketapi.platform.iplt20.com/stats/players?teamIds=1&tournamentIds=22399&scope=TOURNAMENT&pageSize=30
```
- to get simple player info; add teamid to get info about playes only from that team
```
https://cricketapi.platform.iplt20.com/players?tournamentIds=22399&scope=TOURNAMENT&pageSize=30
```
- get scorecard and all kinds of data using matchid; here 32241 is the match id
```
https://cricketapi.platform.iplt20.com//fixtures/32241/scoring
or 
https://cricketapi.platform.iplt20.com/fixtures/32241/scoring
```
- live commentary by matchID; feeds can be changed from 1(1 to 10 most of the time can stop don't get any response content) to get fragments of the commeantry; as it is in fragments; also this can be get for any math with its ID
```
https://cricketapi.platform.iplt20.com//fixtures/32242/commentary/feeds/4?customer=bcci
another url for same
https://cricketapi.platform.iplt20.com//fixtures/32242/commentary/feeds/4?customer=bcci
```
