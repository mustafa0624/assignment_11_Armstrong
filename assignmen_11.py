girdi = str(input("lütfen pozitif integer sayi degeri giriniz")) 
girdi_list =list(girdi)
girdi_set = set(girdi)
sayilar = set("1234567890")
rakamlar = set("qwertzuiopüäölkjhgfdsayxcvbnm")
toplam = 0
y = 0
if (girdi_set - sayilar == {"-"}) or (girdi_set - sayilar == {"."}) or (len(girdi_set & rakamlar) > 0):
  print("lütfen sadece pozitif integer deger giriniz")

else:



  while y < len(girdi):
    yeni = int(girdi_list[y]) ** len(girdi_list)
    toplam += yeni
    y += 1
  
  if int(girdi) == toplam:
    print("bu bir armstrong sayidir")  
  else:
    print("armstrong sayi degildir")

