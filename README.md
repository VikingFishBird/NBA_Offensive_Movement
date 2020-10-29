# How does offensive movement influence the production of NBA offenses?
 Determining the relationship between offensive movement and offensive production in the NBA.

I was reading an article about proving whether or not Andrew Wiggins is lazy, which argued that he only tried his hardest against his former team, the Cleveland Cavaliers. With the low sample size of eight games against the Cavs and a debatable method of quantifying laziness--Judging effort on scoring efficiency seems somewhat flawed--so I wondered how else you could use data to argue this: Distance traveled. The NBA has tracked it since The 13-14 season, a year before Wiggins entered the league. However, I realized that distance traveled can be skewed by the playstyle of a particular team. Teams such as the Rockets often prioritize spacing over movement. They spread across the court to open up driving lanes or isolate defenders for their stars (particularly James Harden) to attack.

[*Does Andrew Wiggins Have an Effort Problem*](https://towardsdatascience.com/does-andrew-wiggins-have-an-effort-problem-a6a13c0337bb)

Judging ball movement solely using offensive distance traveled does punish teams that to run the fastbreak or quick offense as less time on offense results in less distance traveled. Using average speed fixes this issue... while creating new problems. It conflates fastbreak-heavy teams (this years' Lakers) and ball movement-heavy teams. While the Lakers run a static, pick and roll / isolation offense in the halfcourt, they had one of the [best fastbreak offenses in the league](https://stats.nba.com/teams/transition/?SeasonType=Regular%20Season&sort=PPP&dir=1). Considering both distance traveled and average player speed helps us determine which teams fostered more offensive movement.

![Figure 1](/figures/19-20_f1_ORAT_vs_Distance.png)
![Figure 2](/figures/19-20_f2_ORAT_vs_Speed.png)

The data didn't indicate whether offenses that prioritized spacing or movement were better, but did present the tools required to execute each offensive style. Teams that had success with an spacing-oriented offense each had great individual scoring talent that could bear the offensive load. Houston has Harden (ranked 2nd in offensive box plus-minus). Lakers have LeBron (6th) and the ideal pick 'n roll partner in Anthony Davis (10th). Portland has Damian Lillard (1st). On the other hand, teams such as Utah and (especially) San Antonio have been able replicate the same offensive production with offenses that favor movement. Neither Utah or San Antonio have players ranked within the top thirty. Teams have won championships employing both styles such as San Antonio in 2014 [without a single player in the top 20 by OBPM](https://www.basketball-reference.com/leagues/NBA_2014_advanced.html). The pre-Kevin Durant Warriors also prioritized ball movement, although they featured several offensive stars... and the only unanimous MVP in NBA history. After adding KD, one of the best isolation scorers in NBA history, was added to the roster, the Warriors offensive style became more balanced. On the other hand, ~~the LeBron James Heat, LeBron James Cavaliers, and the LeBron James Lakers~~ wherever LeBron goes, his team finds success with the ball in his hands in isolation or pick and roll. Teams can succeed with either playstyle, however certain talent is required to employ each strategy. Teams that prioritize spacing need efficient isolation scorers that can handle the ball/find the open man, while teams with movement-based offenses rely on (often role) players that can create shots without the ball in their hands.

```
                   Player Pos  Age   Tm    TS%   3PAr    FTr  USG%  OBPM▼
Rk                                                                       
1          Damian Lillard  PG   29  POR  0.627  0.500  0.384  30.3    8.3
2            James Harden  SG   30  HOU  0.626  0.557  0.528  36.3    8.1
3   Giannis Antetokounmpo  PF   25  MIL  0.613  0.237  0.508  37.5    7.4
4             Luka Dončić  PG   20  DAL  0.585  0.431  0.448  36.8    7.4
5      Karl-Anthony Towns   C   24  MIN  0.642  0.445  0.363  28.8    7.0
6            LeBron James  PG   35  LAL  0.577  0.326  0.292  31.5    6.6
7           Kawhi Leonard  SF   28  LAC  0.589  0.287  0.355  33.0    6.5
8              Trae Young  PG   21  ATL  0.595  0.455  0.448  34.9    6.2
9            Nikola Jokić   C   24  DEN  0.605  0.238  0.281  26.6    5.5
10          Anthony Davis  PF   26  LAL  0.610  0.199  0.479  29.3    5.4
11           Bradley Beal  SG   26  WAS  0.579  0.369  0.351  34.4    5.3
12           Kemba Walker  PG   29  BOS  0.575  0.532  0.272  27.2    4.9
13       Danilo Gallinari  PF   31  OKC  0.612  0.537  0.365  24.6    4.1
14           Jimmy Butler  SF   30  MIA  0.585  0.157  0.693  25.1    4.0
15           Derrick Rose  PG   31  DET  0.555  0.195  0.185  31.6    3.9
16            Paul George  SF   29  LAC  0.589  0.487  0.277  29.6    3.8
17       D'Angelo Russell  PG   23  TOT  0.556  0.509  0.235  31.5    3.8
18           John Collins  PF   22  ATL  0.659  0.243  0.248  22.7    3.7
19            Joel Embiid   C   25  PHI  0.590  0.215  0.543  32.9    3.7
20         Nikola Vučević   C   29  ORL  0.549  0.280  0.162  25.8    3.7
21           Jayson Tatum  PF   21  BOS  0.567  0.383  0.255  28.6    3.5
22         Christian Wood  PF   24  DET  0.659  0.276  0.476  23.0    3.5
23           Devin Booker  SG   23  PHO  0.618  0.310  0.397  30.0    3.4
24        Khris Middleton  SF   28  MIL  0.619  0.374  0.240  26.4    3.4
25            Zach LaVine  SG   24  CHI  0.568  0.404  0.279  31.7    3.2
26             Chris Paul  PG   34  OKC  0.610  0.343  0.315  23.3    3.0
27          Dāvis Bertāns  PF   27  WAS  0.628  0.774  0.200  19.0    2.7
28      Spencer Dinwiddie  SG   26  BRK  0.541  0.392  0.437  29.2    2.7
29         Gordon Hayward  SF   29  BOS  0.595  0.317  0.207  21.1    2.6
30             Kevin Love  PF   31  CLE  0.599  0.536  0.301  23.1    2.6
```
[Exported CSV from basketball-reference.](https://www.basketball-reference.com/leagues/NBA_2020_advanced.html)

Below is my examination of differences between average speed and traveled distance and how they each might inaccurately represent offensive movement:
I compared each team's pace (determined by the amount of possessions a team has in a game) and the deviation from the linear regression line of the graph below, which reveals the differences when using average speed and traveled distance to represent movement. While each team's pace and deviation are correlated, they aren't identical. The deviation appears to emphasize fast break scoring (due to the involvement of player speed) so that teams like the Lakers, which run a slow-paced\* halfcourt offense, but love to run in transition are ranked highly, while the Hawks's fast-paced\* halfcourt offense is obscured.

*\*Note: Slow-paced and fast-paced refer to how quickly each team's plays develop, not the speed of the players in the offense.*

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



Response to anonymous piazza poster: *I feel like it would also be interesting to see this analysis done on the top 20 NBA players today. Would they deviate far from the regression line relating player speed and distance traveled?*

Here's the graphs by player speed and distance traveled:

![Figure 6](/figures/19-20_f6_Player_VORP_vs_Distance.png)
![Figure 7](/figures/19-20_f7_Player_VORP_vs_Player_Speed.png)

As expected, graphs have very different representations of movement. A player like Giannis has a relatively low distance traveled, but his average speed tops the league as the best fastbreak finisher in the NBA. Another interesting note is the difference between Harden and Lillard. While both the Rockets and Trailblazers run iso-heavy offenses, Harden is often stagnant, lulling defenders asleep with repetitive still dribbles and Lillard is often using high ball screens to attack the opposing bigs resulting in drastically different average speeds despite each offense prioritizing spacing.


[NBA Stats API](https://github.com/swar/nba_api/tree/master/docs/nba_api)

