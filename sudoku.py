counter = 0
print("-------------------------------")
for i in (sudoku):
    
    
    print(*i[:3],"|",*i[3:6],"|",*i[6:],sep="  ")
    #counter = 0
    counter += 1
    if counter % 3 == 0 :
        print("-------------------------------")
    