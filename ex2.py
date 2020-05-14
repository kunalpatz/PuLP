import pulp

x = pulp.LpVariable('Nb of tables', lowBound=10, upBound=20, cat='Integer')

z = pulp.LpProblem('My maximization pb', pulp.LpMaximize)

z += 5*x, 'Net Profit'
z += x <= 15, 'max of daily production'
z.solve()

for var in z.variables():
    print(var.name+'='+ str(var.varValue))

print('value of Obj function:' + str(pulp.value(z.objective)))
