deger = int(input("please enter a number"))



if deger > 1:
    for i in range(2,deger):
        if deger % i == 0:
            print("sayi asal degildir")
            break
        else:
            print("sayiniz asaldir")
            break
else:
     print("lütfen 1 den büyük deger giriniz")        
