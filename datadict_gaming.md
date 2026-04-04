#Gaming and mental health dataset
27 features, 1000 datapoints  

### features
RECORD_ID
* Unique identifiers for each datapoint  
  

Age 
* discrete
* numerical
* range:  
  
  
Gender
* Categorical
* Male, Female, Other
* Convert to -> M:0, F:1, O:2  
  
  
Daily gaming hours 
* Continuous
* Range:  
  
  
Game genre
* Categorical
* "Mobile Games", "MOBA", "FBS", "Battle Royale", "MMO", "RPG", "Strategy",   
  
  
Primary Game
* Categorical
* Idk how many different options there are for this, may be easier to remove
  
  
Gaming platform
* Categorical
* "PC", "Multi-platform", "Console", "Mobile"
* Convert to -> PC:0, MP:1, C:2, M:3  
  
  
Sleep hours
* Continuous
* Range:   
  
  
Sleep quality  
* Categorical
* Ordinal
* "Insomnia", "Very Poor", "Poor", "Fair", "Good", 
* Convert to -> I:0, VP:1, P:2, F:3, G:4  
  
  
Sleep disruption
* Categorical
* Ordinal
* "Never", "Rarely", "Sometimes", "Often", "Always"
* Convert to -> N:0, R:1, S:2, O:4, A:5  
  
  
Academic work performance
* Categorical
* Ordinal
* "Failing", "Poor", "Below Average", "Average", "Good", "Excellent"
* Convert to -> F:0, P:1, BA:2, A:3, G:4, E:5
  
  
Grades GPA
* Continuous
* Range:   
   
  
Work Productivity score
* Discrete
* Range:  
  
  
Mood State
* Categorical
* "Anxious", "Irritable", "Withdrawn", "Angry", "Restless", "Normal", "Euphoric", "Depressed", "Excited"
* Convert to ->  
  
  
Mood swing frequency
* Categorical
* Ordinal
* "Never", "Rarely", "Sometimes", "Often", "Daily"
* Convert to -> N:0, R:1, S:2, O:3, D:4  
  
  
Withdrawal symptoms
* Binary, T/F
* Convert -> 0/1
  
  
Loss of other interests  
* Binary, T/F
* Convert -> 0/1
  
  
Continued despite problems  
* Binary, T/F
* Convert -> 0/1
  
  
Eye strain 
* Binary, T/F
* Convert -> 0/1 
  
  
Back neck pain  
* Binary, T/F
* Convert -> 0/1
  
  
Weight change (kg)
* Continuous
* Range: 
  
  
Exercise hours weekly 
* Continuous
* Range: 
  
  
Social isolation score
* Discrete
* Range:  
  
  
Face to face social hours weekly
* Continuous
* Range:  
  
  
Monthly game spending (usd)
* Continuous
* Range:  
  
  
Years gaming
* Continuous
* Integer
* Range:  
  
  
Gaming addiction risk level (target)
* Categorical
* Ordinal
* "Low", "Moderate", "High", "Severe"
* Convert to -> L:0, M:1, H:2, S:3


