# # creating a 1-D array
# n = 5
# arr = [0]*n
# print(arr)

# create a 2-D matrix
rows, cols = (5, 5)
# arr = [[0]*cols]*rows
arr = [[0 for i in range(cols)] for j in range(rows)]
print(arr)