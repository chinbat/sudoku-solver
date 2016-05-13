"""
python-ii pulp gedeg library ashiglan Sudoku bodoh
Chinbat Chindegsuren
"""

from pulp import *

digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

Vals = digits
Rows = digits
Cols = digits

Boxes =[]
for i in range(3):
    for j in range(3):
        Boxes += [[(Rows[3*i+k], Cols[3*j+l]) for k in range(3) for l in range(3)]]

# objective function neh hamagui uchraas, minimize, maximize ali ni ch bolno
prob = LpProblem("Sudoku Bodoy", LpMinimize)
prob += 0, "Arbitrary Objective Function"

# huvisagchid
choices = LpVariable.dicts("Choice", (Vals, Rows, Cols), 0, 1, LpInteger)

# nuhtsuluud
for r in Rows:
    for c in Cols:
        prob += lpSum([choices[v][r][c] for v in Vals]) == 1, ""

for v in Vals:
    for r in Rows:
        prob += lpSum([choices[v][r][c] for c in Cols]) == 1, ""
        
    for c in Cols:
        prob += lpSum([choices[v][r][c] for r in Rows]) == 1, ""

    for b in Boxes:
        prob += lpSum([choices[v][r][c] for (r, c) in b]) == 1, ""

with open("prob.txt", "r") as f:
    for i, row in enumerate(f.readlines()):
        for j, val in enumerate(list(row.rstrip('\n'))):
            if val != '0':
                prob += choices[str(val)][str(i+1)][str(j+1)] == 1, ""

# problem nuhtsuluudee file-ru yu ch gsn bichih
prob.writeLP("Sudoku.lp")

# answer-aa hadgalah file
sudokuout = open('ans.txt', 'w')

while True:
    # pulp dotorh cbc solver-g ashiglan bodoh
    prob.solve()
    # bodoj chadsan esehiig hevleh
    print("Status:", LpStatus[prob.status])
    # optimal hariu baihgui boltol haih
    if LpStatus[prob.status] == "Optimal":
        # hariugaa file-ruu hevleh
        for r in Rows:
            if r == "1" or r == "4" or r == "7":
                sudokuout.write("+-------+-------+-------+\n")
            for c in Cols:
                for v in Vals:
                    if value(choices[v][r][c]) == 1:
                        if c == "1" or c == "4" or c == "7":
                            sudokuout.write("| ")
                        sudokuout.write(v + " ")
                        if c == "9":
                            sudokuout.write("|\n")
        sudokuout.write("+-------+-------+-------+")

        prob += lpSum(
            [choices[v][r][c] for v in Vals for r in Rows for c in Cols if value(choices[v][r][c]) == 1]
        ) <= 80
    # dahij optimal hariu baihgui bol loop-s garah
    else:
        break
sudokuout.close()

print("harilut: ans.txt")
