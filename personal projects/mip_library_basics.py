from mip import *

# --- GOAL: ---
# maximize 2x + y + 3z
# with constraints:
# x + 2y + z <= 4
# 2z + y <= 5
# x + y >= 1
# x E {0,1}
# y,z >= 0
# z E ZZ

# CREATE A MODEL
m = Model()
# Model(sense='MAXIMIZE', solver_name='CBC')
# default sense = minimize
# solver GRB = gurobi (free to install)

# ADD VARIABLES
x = m.add_var(name='x', var_type='BINARY') # fits 4th constraint
y = m.add_var(name='y', var_type='CONTINUOUS', lb=0)
z = m.add_var(name='z', var_type='INTEGER', lb=0) # fits last constraint
# lb = lower bound
# up = upper bound
# can also add variables like this...
# n = 10
# y = [ m.add_var(var_type=BINARY) for i in range(n) ]

# ADD CONSTRAINTS
c1 = m.add_constr(x+2*y+z <= 4, name='c1')
c2 = m.add_constr(2*z+y <= 5, name='c2')
c3 = m.add_constr(x+y >= 1, name='c3')

# DEFINE OBJECTIVE FUNCTION
m.objective = maximize(2*x+y+3*z)

# OPTIMIZE
m.optimize()

# PRINT SOLUTION
if m.num_solutions:
    print("Optimal Solution:")
    print("x =", x.x)
    print("y =", y.x)
    print("z =", z.x)
    print("Objective Value (maximized) =", m.objective_value)
else:
    print("No solution found.")
