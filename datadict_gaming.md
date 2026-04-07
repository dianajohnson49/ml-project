# Gaming and mental health dataset
27 features, 1000 datapoints   
10 Categorical features to convert to discrete  
4 Binary categorical features to convert to binary numerical  

Sleep disruption, Mood swing frequency both use N/R/S/O/A scale
Four binary features all use T/F for 1/0 

### features
__RECORD_ID__
* Unique identifiers for each datapoint  
  

__Age__
* discrete
* numerical
* range: 13-35
  
  
__Gender__
* Categorical
* ```"Male", "Female", "Other"```
* Convert to -> M:0, F:1, O:2  
  
  
__Daily gaming hours__ 
* Continuous
* Range: 0.5-15.1
  
  
__Game genre__
* Categorical
* ```"Mobile Games", "MOBA", "FPS", "Battle Royale", "MMO", "RPG", "Strategy"```
* Convert to -> MG:0, MOBA:1, FPS:2, BR:3, MMO:4, RPG:5, S:6  
  
  
__Primary Game__
* Categorical
* 24 possible values
``` 
"Age of Empires", "Apex Legends", "CS:GO", "Call of Duty", "Candy Crush", "Civilization VI", "Clash of Clans"
"Cyberpunk 2077", "Dota 2", "Elden Ring", "Elder Scrolls Online", "Final Fantasy XIV", "Fortnite"
"Genshin Impact", "League of Legends", "Mobile Legends", "Overwatch", "PUBG", "PUBG Mobile", "Skyrim",
"StarCraft II", "Valorant", "Warzone", "World of Warcraft" 
```
  
  
__Gaming platform__
* Categorical
* ```"PC", "Multi-platform", "Console", "Mobile"```
* Convert to -> PC:0, MP:1, C:2, M:3  
  
  
__Sleep hours__
* Continuous
* Range: 3.0-9.0
  
  
__Sleep quality__  
* Categorical
* Ordinal
* ```"Insomnia", "Very Poor", "Poor", "Fair", "Good",``` 
* Convert to -> I:0, VP:1, P:2, F:3, G:4  
  
  
__Sleep disruption__
* Categorical
* Ordinal
* ```"Never", "Rarely", "Sometimes", "Often", "Always"```
* Convert to -> N:0, R:1, S:2, O:4, A:5  
  
  
__Academic work performance__
* Categorical
* Ordinal
* ```"Failing", "Poor", "Below Average", "Average", "Good", "Excellent"```
* Convert to -> F:0, P:1, BA:2, A:3, G:4, E:5
  
  
__Grades GPA__
* Continuous
* Range: 1.01-4.0 
* MISSING 246/1000 values
   
  
__Work Productivity score__
* Discrete
* Range: 1-10
* MISSING 326/1000 values
  
  
__Mood State__
* Categorical
* ```"Depressed", "Anxious", "Angry", "Irritable", "Withdrawn", "Restless", "Normal", "Excited", "Euphoric"```
* Convert to ->  D:0, Ax:1, Ag:2, I:3, W:4, R:5, N:6, Ex:7, Eu:8 
  
  
__Mood swing frequency__
* Categorical
* Ordinal
* ```"Never", "Rarely", "Sometimes", "Often", "Daily"```
* Convert to -> N:0, R:1, S:2, O:3, D:4  
  
  
__Withdrawal symptoms__
* Binary, T/F
* Convert -> 0/1
  
  
__Loss of other interests__  
* Binary, T/F
* Convert -> 0/1
  
  
__Continued despite problems__  
* Binary, T/F
* Convert -> 0/1
  
  
__Eye strain__ 
* Binary, T/F
* Convert -> 0/1 
  
__Back neck pain__  
* Binary, T/F
* Convert -> 0/1
  
  
__Weight change (kg)__
* Continuous
* Range: 0.0-8.9
  
  
__Exercise hours weekly__ 
* Continuous
* Range: 0.7-11.5
  
  
__Social isolation score__
* Discrete
* Range: 1-10
  
  
__Face to face social hours weekly__
* Continuous
* Range: 0.0-16.7  
  
  
__Monthly game spending (usd)__
* Continuous
* Range: 0.1-499.27
  
  
__Years gaming__
* Continuous
* Integer
* Range: 1-20
  
  
__Gaming addiction risk level (target)__
* Categorical
* Ordinal
* ```"Low", "Moderate", "High", "Severe"```
* Convert to -> L:0, M:1, H:2, S:3


