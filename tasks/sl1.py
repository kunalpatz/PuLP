"""
PROBLEM: A calculator company produces a scientific calculator and a graphing calculator. Long-term projections indicate
an expected demand of at least 100 scientific and 80 graphing calculators each day. Because of limitations on production
capacity, no more than 200 scientific and 170 graphing calculators can be made daily. To satisfy a shipping contract,
a total of at least 200 calculators much be shipped each day.
If each scientific calculator sold results in a $2 loss, but each graphing calculator produces a $5 profit,
how many of each type should be made daily to maximize net profits?
"""
"""
SOLUTION
x, y >= 0
x + y >= 200 --> y >= -x + 200 

100 <= x <= 200
80 <= y <= 170

Objective function
Profit: P = -2x + 5y

"""
# PROGRAM

import pulp

x = pulp.LpVariable('Number of Scientific calculators', lowBound=100, upBound=200, cat='Integer')

y = pulp.LpVariable('Number of Graphical calculators', lowBound=80, upBound=170, cat='Integer')

z = pulp.LpProblem('Profit maximization', pulp.LpMaximize)

z += -2*x + 5*y, 'Objective Function for net Profit'

z += x + y >= 200, 'Total contracts for each day'

if z.solve() == 1:
    for var in z.variables():
        print(str(var.name) + '=' + str(var.varValue))
else:
    print('Error')


"""
OUTPUT:
Number_of_Graphical_calculators=170.0
Number_of_Scientific_calculators=100.0

"""


