# NBA_Offensive_Movement
 Determining the releationship between offensive movement and offensive production in the NBA.

I was reading an article about proving whether or not Andrew Wiggins *Does Andrew Wiggins Have an Effort Problem?*
https://towardsdatascience.com/does-andrew-wiggins-have-an-effort-problem-a6a13c0337bb
Judging effort on scoring efficiency seems somewhat flawed, so I considered other methods of quantifying effort: Distance traveled. The NBA has tracked it since The 13-14 season--a year before Wiggins entered the league. However, I realized that distance traveled can be skewed by the playstyle of a particular team. Teams such as the Rockets often prioritize spacing over movement. They spread across the court to open up driving lanes or isolate defenders for their stars (particularly James Harden) to attack.

Judging ball movement solely using offensive distance traveled does punish teams that to run the fastbreak or quick offense as less time on offense results in less distance traveled. Using average speed fixes this issue... while creating new problems. It conflates fastbreak-heavy teams (this years' Lakers) and ball movement-heavy teams. While the Lakers run a static, pick and roll / isolation offense in the halfcourt, they had one of the (best fastbreak offenses in the league)[https://stats.nba.com/teams/transition/?SeasonType=Regular%20Season&sort=PPP&dir=1].
