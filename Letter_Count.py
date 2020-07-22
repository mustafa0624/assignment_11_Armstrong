def char_frequency(a):
    a = input("gir")
    b = {}
    
    for i in a:
        count = 0
        for j in a:
            if i == j:
                count += 1
                
        b[i] = count 
    print(b)       
char_frequency(a)    