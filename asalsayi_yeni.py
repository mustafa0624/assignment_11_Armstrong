deger = int(input("deger giriniz"))
liste = []

for i in range(1,deger+1):
    counter = 0
    for j in range(1,i+1):
        if i % j == 0:
            counter += 1  
        
            
    if counter == 2:
        liste.append(i)
print(liste)        