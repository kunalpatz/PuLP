import pulp

x1 = pulp.LpVariable('Number of jackets', lowBound=0)
x2 = pulp.LpVariable('Number of pair of pants', lowBound=0)
z = pulp.LpProblem('Minimum_cost', pulp.LpMinimize)

z += 3*x1 + x2, 'objective function'
z += x1 + x2 >= 2, 'Min production of the day'
z.solve() # resp 1 means done

for var in z.variables():
    print(var.name, '=', var.varValue)

print(pulp.value(z.objective))




