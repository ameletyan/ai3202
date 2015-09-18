# CSCI 3202 Assignment 3
This program is meant to utilize the A* search algorithm

# PRELUDE:
Unfortunately, I was not able to finish this assignment.  My organization and prioritization skills were terrible
this week and I did not allow myself the time to thoroughly tackle the assignment.  That said, I was nearing the
completion of the first A* search heuristic before I ran out of time.  Nonetheless, the rest of this file explains
the second heuristic that I WOULD HAVE used had I not dug my self into a deep hole of time-lacking and regret.

# My Heuristic
The psuedo code would look something like this:

def myHeuristic(graph):

  distance_from_start = 0
  
  while an end of the graph is not reached:
  
    move diagonally towards the goal
    
    add cost_to_move_diagonally to distance_from_start
  
  if the goal is met:
  
    return
    
  else:
  
    if vertical movement is possible:
    
      while goal is not reached:
      
        move vertically
        
        add cost_to_move_vertically to distance_from_start
        
      return
      
    else:
    
      while goal is not reached:
      
        move horizontally
        
        add cost_to_move_horizontally to distance_from_start
        
      return

NOTE: In most cases, cost_to_move_vertically and cost_to_move_horizontally will be the same.

# Motivation for Selecting the Heuristic
I wanted to use this heuristic because it I believe that it would ultimately come up with a result that is more
efficient than the Manhattan distance heuristic.  I noticed that the Manhattan distance heuristic often misses
opportunities to move diagonally and save cost.  The algorithm I would have used should not have missed these
opportunities (at least that is what I believe).  Also, it would have been relatively easy to code because it is
only a little more complex than the Manhattan distance heuristic.

# My Heuristic vs Manhattan Distance Heuristic
I was not able to get far enough to actually test the reliability of my heuristic against that of the Manhattan distance.

# Final Note
I do apologize if my lack of completion of this assignment offended or otherwise inflicted unwanted consequences to
the grader.  I grossly underestimated the time it would take me to finish this assignment.  Live and learn I suppose.
