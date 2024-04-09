from pulp import LpMaximize, LpProblem, LpVariable

# Define problem
problem = LpProblem("Maximize_Profits", LpMaximize)

# Define decision variables
white = LpVariable('White', lowBound=0, cat='Integer')  # Number of white shirts
blue = LpVariable('Blue', lowBound=0, cat='Integer')    # Number of blue shirts
yellow = LpVariable('Yellow', lowBound=0, cat='Integer')  # Number of yellow shirts
red = LpVariable('Red', lowBound=0, cat='Integer')      # Number of red shirts

# Define objective function
profit_white = 7  # Profit per white shirt
profit_blue = 8   # Profit per blue shirt
profit_yellow = 8  # Profit per yellow shirt
profit_red = 6    # Profit per red shirt

problem += (profit_white * white + profit_blue * blue +
            profit_yellow * yellow + profit_red * red), "Total_Profit"

# Define constraints
time_to_dye_white = 0
time_to_dye_blue = 20
time_to_dye_yellow = 20
time_to_dye_red = 40

problem += (time_to_dye_white * white + time_to_dye_blue * blue +
            time_to_dye_yellow * yellow + time_to_dye_red * red) <= 480, "Total_Time_Constraint"

problem += white <= 50, "White_Supply_Constraint"
problem += blue <= 15, "Blue_Supply_Constraint"
problem += yellow <= 10, "Yellow_Supply_Constraint"
problem += red <= 12, "Red_Supply_Constraint"

# Solve the problem
problem.solve()

# Print the optimal solution
print("Optimal Solution:")
print("Number of White Shirts:", int(white.varValue))
print("Number of Blue Shirts:", int(blue.varValue))
print("Number of Yellow Shirts:", int(yellow.varValue))
print("Number of Red Shirts:", int(red.varValue))
print("Total Profit: $", round(problem.objective.value(), 2))
