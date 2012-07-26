# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# takes no input and RETURNS two grids. The
# first grid, value, should contain the computed
# value of each cell as shown in the video. The
# second grid, policy, should contain the optimum
# policy for each cell.
#
# Stay tuned for a homework help video! This should
# be available by Thursday and will be visible
# in the course content tab.
#
# Good luck! Keep learning!
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.
#
# NOTE: Please do not modify the values of grid,
# success_prob, collision_cost, or cost_step inside
# your function. Doing so could result in your
# submission being inappropriately marked as incorrect.

# -------------
# GLOBAL VARIABLES
#
# You may modify these variables for testing
# purposes, but you should only modify them here.
# Do NOT modify them inside your stochastic_value
# function.

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
       
goal = [0, len(grid[0])-1] # Goal is in top right corner


delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

success_prob = 0.5                      
failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
collision_cost = 100                    
cost_step = 1        
                     

############## INSERT/MODIFY YOUR CODE BELOW ##################
#
# You may modify the code below if you want, but remember that
# your function must...
#
# 1) ...be called stochastic_value().
# 2) ...NOT take any arguments.
# 3) ...return two grids: FIRST value and THEN policy.

def stochastic_value():
    value = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True
    while change:
      change = False
      for x in range(len(grid)):
        for y in range(len(grid[0])):
          for d in range(len(delta)):
            cost = 1
            if goal[0] == x and goal[1] == y:
              if(value[x][y] > 0):
                value[x][y] = 0
                policy[x][y] = '*'
                change = True
            elif grid[x][y] == 0:
                dr = d-1
                dl = d+1
                dlen = len(delta)
                fail_right = delta[dr % dlen]
                fail_left = delta[dl % dlen]
                success = delta[d]
                x_success = x+success[0]
                y_success = y+success[1]
                x_failright = x+fail_right[0]
                y_failright = y+fail_right[1]
                x_failleft = x+fail_left[0]
                y_failleft = y+fail_left[1]
  
                if x_success >= 0 and x_success < len(grid) and y_success >= 0 and y_success < len(grid[0]) and grid[x_success][y_success] == 0:
                  cost += value[x_success][y_success] * success_prob
                else:
                  #collision
                  cost += success_prob * collision_cost
  
                if x_failright >= 0 and x_failright < len(grid) and y_failright >= 0 and y_failright < len(grid[0]) and grid[x_failright][y_failright] == 0:
                  cost += failure_prob * value[x_failright][y_failright]
                else:
                  
                  #collision
                  cost += failure_prob * collision_cost
  
                if x_failleft >= 0 and x_failleft < len(grid) and y_failleft >= 0 and y_failleft < len(grid[0]) and grid[x_failleft][y_failleft] == 0:
                  cost += failure_prob * value[x_failleft][y_failleft]
                  
                else:
                  #collision
                  cost += failure_prob * collision_cost
                  
                if cost < value[x][y]:
                  value[x][y] = cost
                  policy[x][y] = delta_name[d]
                  change = True

    return value, policy

