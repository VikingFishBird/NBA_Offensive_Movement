# How important is offensive movement in the NBA?
 Determining the releationship between offensive movement and offensive production in the NBA.

I was reading an article about proving whether or not Andrew Wiggins [*Does Andrew Wiggins Have an Effort Problem*](https://towardsdatascience.com/does-andrew-wiggins-have-an-effort-problem-a6a13c0337bb)

Judging effort on scoring efficiency seems somewhat flawed, so I considered other methods of quantifying effort: Distance traveled. The NBA has tracked it since The 13-14 season--a year before Wiggins entered the league. However, I realized that distance traveled can be skewed by the playstyle of a particular team. Teams such as the Rockets often prioritize spacing over movement. They spread across the court to open up driving lanes or isolate defenders for their stars (particularly James Harden) to attack.

Judging ball movement solely using offensive distance traveled does punish teams that to run the fastbreak or quick offense as less time on offense results in less distance traveled. Using average speed fixes this issue... while creating new problems. It conflates fastbreak-heavy teams (this years' Lakers) and ball movement-heavy teams. While the Lakers run a static, pick and roll / isolation offense in the halfcourt, they had one of the [best fastbreak offenses in the league](https://stats.nba.com/teams/transition/?SeasonType=Regular%20Season&sort=PPP&dir=1).

![Figure 1](/figures/19-20_f1_ORAT_vs_Distance.png)
![Figure 2](/figures/19-20_f2_ORAT_vs_Speed.png)

Below I compared each team's pace (determined by the amount of poessessions a team has in a game) and the deviation from the linear regression line of the graph below, which reveals the differences when using average speed and traveled distance to represent movement.
![Figure 3](/figures/19-20_f3_Distance_vs_Speed.png)

```
                         TEAM_NAME  Pace_Rank  Deviation_Rank  Avg_Rank
TEAM_ID                                                                
1610612745         Houston Rockets          2               1       1.5
1610612749         Milwaukee Bucks          1               3       2.0
1610612740    New Orleans Pelicans          3               6       4.5
1610612764      Washington Wizards          7               5       6.0
1610612747      Los Angeles Lakers         11               2       6.5
1610612761         Toronto Raptors         12               4       8.0
1610612746             LA Clippers          9               7       8.0
1610612763       Memphis Grizzlies          6              12       9.0
1610612750  Minnesota Timberwolves          4              16      10.0
1610612751           Brooklyn Nets          8              15      11.5
1610612741           Chicago Bulls         16               8      12.0
1610612744   Golden State Warriors         14              11      12.5
1610612737           Atlanta Hawks          5              20      12.5
1610612738          Boston Celtics         17               9      13.0
1610612756            Phoenix Suns         10              17      13.5
1610612757  Portland Trail Blazers         13              18      15.5
1610612754          Indiana Pacers         20              13      16.5
1610612752         New York Knicks         24              10      17.0
1610612760   Oklahoma City Thunder         22              14      18.0
1610612759       San Antonio Spurs         15              21      18.0
1610612758        Sacramento Kings         21              22      21.5
1610612753           Orlando Magic         25              19      22.0
1610612755      Philadelphia 76ers         19              26      22.5
1610612742        Dallas Mavericks         18              28      23.0
1610612762               Utah Jazz         26              25      25.5
1610612766       Charlotte Hornets         30              23      26.5
1610612743          Denver Nuggets         29              24      26.5
1610612739     Cleveland Cavaliers         23              30      26.5
1610612765         Detroit Pistons         28              27      27.5
1610612748              Miami Heat         27              29      28.0
```

![Figure 4](/figures/19-20_f4_Deviation_from_line.png)
![Figure 5](/figures/19-20_f5_Pace.png)




[NBA Stats API](https://github.com/swar/nba_api/tree/master/docs/nba_api)

