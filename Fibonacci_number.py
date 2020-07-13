list = []
for i in range(-2,8):
    if i < 0:
        list.append(1)
    else:
        list.append(list[i] + list[i+1])
print(list)        