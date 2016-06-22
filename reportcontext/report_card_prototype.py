# -*- coding: utf-8 -*-
"""
Created on Wed May 25 16:02:11 2016

@author: johnofmars
"""

import time

#---------------HEADER----------------------

header = """---
layout: post
title: {Title}
excerpt: "{Excerpt}"
modified: {Date}
categories: articles
tags: [pvp,trials,data]
image:
  feature: header.png
comments: true
share: true
---
"""

header_context = {
 "Title":'Report Card', 
 "Excerpt":"Test",
 "Date":time.strftime("%Y-%m-%d")
 } 
 
with  open('report_card.txt','w') as myfile:
    myfile.write(header.format(**header_context))

#---------------TEAM SUMMARY-----------

summary = """
##Trials Report Card

###Team Summary

1. {Player1} - The {Player1_weapon}-wielding {Player1_class}
2. {Player2} - The {Player2_weapon}-wielding {Player2_class}
3. {Player3} - The {Player3_weapon}-wielding {Player3_class}

"""

summary_context = {
 "Player1":'Player 1', 
 "Player1_weapon":"Weapon",
 "Player1_class":"Character Class",
 "Player2":'Player 2', 
 "Player2_weapon":"Weapon",
 "Player2_class":"Character Class",
 "Player3":'Player 3', 
 "Player3_weapon":"Weapon",
 "Player3_class":"Character Class",
 } 
 
with  open('report_card.txt','a') as myfile:
    myfile.write(summary.format(**summary_context))
    
#---------------TEAM PERFORMANCE-----------

teamperf = """
### Overall Team Performance

![](http://johnofmars.github.io/images/{map_path})

Playing on {Map} for {Time}
Spawn Side: % Alpha, % Bravo

Kill Method Distribtuion:
% primary
% secondary
% Heavy
% Ability (melee/grenade) 
% Super
	
Round Scores by Game
![](http://johnofmars.github.io/images/{graph_path})

- Team K/D
- % Matches we had First Kill	
- {N_aces} Aces vs {N_aces} times Aced
- {N_annil} Annihilations vs {N_annil} times Annihilated
- {N_rez} Resurrections vs {N_rez} Enemy Resurrections Allowed
- {N_orbs} Orbs Missed

"""

teamperf_context = {
 "map_path":"headers/trials2.jpg",
 "Map":"Map",
 "Time":"Time",
 "graph_path":"headers/trials2.jpg",
 "N_aces":"N",
 "N_annil":"N",
 "N_rez":"N",
 "N_orbs":"N",
 } 
 
with  open('report_card.txt','a') as myfile:
    myfile.write(teamperf.format(**teamperf_context))

#---------------INDIV PERFORMANCE-----------

indiv = """

### Detailed Individual Performance

| General Summary            | {Player1} | {Player2} | {Player3} |
|----------------------------|-----------|-----------|-----------|
| Kills                      |           |           |           |
| Assists                    |           |           |           |
| Deaths                     |           |           |           |
| K/D                        |           |           |           |
| Sweaty K/D                 |           |           |           |
| % Contribution             |           |           |           |
| Score Contribution         |           |           |           |
| Last Guardian Actions*     |           |           |           |
| Wrecking Balls             |           |           |           |
| Longest Kill Streak        |           |           |           |
| Longest Life               |           |           |           |
| Close Calls                |           |           |           |

Last Guardian Actions are:

'Never Say Die' = Kill an enemy as the last guardian standing
'From the Brink' = Revive a teammate as the last guardian standing

| Kill Method Breakdown      | {Player1} | {Player2} | {Player3} |
|----------------------------|-----------|-----------|-----------|
| % Primary vs Secondary     |           |           |           |
| Sniper Headshots / Kills   |           |           |           |
| Shotgun Kills              |           |           |           |
| Other Special Weapon Kills |           |           |           |
| Heavy Weapon Kills         |           |           |           |
| Grenade Kills              |           |           |           |
| Melee Kills                |           |           |           |
| Super Kills                |           |           |           |

| Resurrections & Orbs       | {Player1} | {Player2} | {Player3} |
|----------------------------|-----------|-----------|-----------|
| Resurrections Performed    |           |           |           |
| Resurrection Received      |           |           |           |
| Deaths Un-Rezzed           |           |           |           |
| Orbs Generated             |           |           |           |
| Orbs Missed                |           |           |           |
"""

indiv_context = {
 "Player1":'Player 1', 
 "Player2":'Player 2', 
 "Player3":'Player 3'
 } 
 
with  open('report_card.txt','a') as myfile:
    myfile.write(indiv.format(**indiv_context))