matrix = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

res = [[0,1],[0,0]]

print(matrix[:2])

i_start = 0
i_end = 2
j_start = 0
j_end = 2

res = [row[j_start: j_end] for row in matrix[i_start: i_end]]
print(res)