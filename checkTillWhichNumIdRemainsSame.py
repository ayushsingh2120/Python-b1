i = 0
j = 0
while (id(i) == id(j)):
    print(i, j , id(i), id(j))
    i += 1
    j += 1
print(f"i is: {i} with id {id(i)} and j is: {j} with id {id(j)}")

