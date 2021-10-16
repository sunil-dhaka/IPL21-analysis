# APIs used in project

**`general points`**
- for all APIs that `has` multiple pages tweak these parameters
    - pageSize (max is 100 in all cases)
    - page (starts from 0)
**`API desc`**
- to get tornament IDs:
```
https://cricketapi.platform.iplt20.com/tournaments
```
- to get teams info in a tornament: tour id changes
```
https://cricketapi.platform.iplt20.com/teams?teamIds=1&tournamentIds=22399&scope=TOURNAMENT&pageSize=30
```
- to get teams stats in a tour: team id changes
```
https://cricketapi.platform.iplt20.com/stats/players?teamIds=1&tournamentIds=22399&scope=TOURNAMENT&pageSize=30
```
- to get simple player info
    - add teamid to get info about players from particular team
```
https://cricketapi.platform.iplt20.com/players?tournamentIds=22399&scope=TOURNAMENT&pageSize=30
```
- get scorecard and all kinds of data using matchid
    - here 32241 is the match id
```
https://cricketapi.platform.iplt20.com/fixtures/32241/scoring
```
- live commentary by matchID
    - feeds can be changed from 1(1 to 10 most of the time)
        -  can stop when don't get any response content
    - also this can be done for any match with its ID
```
https://cricketapi.platform.iplt20.com//fixtures/32242/commentary/feeds/4?customer=bcci
```
- to get player bios from all seasaons
```
https://api.platform.iplt20.com/content/ipl/bios/EN/?
```