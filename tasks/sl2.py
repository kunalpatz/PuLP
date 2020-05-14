"""
PROBLEM:
You need to buy some filing cabinets. You know that Cabinet X costs $10 per unit, requires six square feet of floor
space, and holds eight cubic feet of files. Cabinet Y costs $20 per unit, requires eight square feet of floor space, and
holds twelve cubic feet of files. You have been given $140 for this purchase, though you don't have to spend that much.
The office has room for no more than 72 square feet of cabinets. How many of which model should you buy, in order to
maximize storage volume?
"""

"""
SOLUTION:
x: cabinets costing $10
y: cabinets costing $20

Constraint1: 10x + 20y <= 140 --> x + 2y <= 14 --> y <= -x/2 + 7 

Constraint2: 6x + 8y <= 72

Obj function: Volume: V= 8x + 12y 
"""
# PROGRAM:

import pulp

x = pulp.LpVariable('Cabinet costing $10', lowBound=0)

y = pulp.LpVariable('Cabinet costing $20', lowBound=0)

z = pulp.LpProblem('Volume maximization of storage', pulp.LpMaximize)

z += 8*x + 12*y, 'Objective function of Volume'

z += 10*x + 20*y <= 140, 'Constraint1 for cost'
z += 6*x + 8*y <= 72, 'Constraint2 for space'

if z.solve() == 1:
    for var in z.variables():
        print(str(var.name) + '=' + str(var.varValue))
else:
    print('Error')

"""
OUTPUT:
Cabinet_costing_$10=8.0
Cabinet_costing_$20=3.0

"""