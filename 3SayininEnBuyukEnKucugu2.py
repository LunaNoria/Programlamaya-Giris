i=1
enbuyuk=0
while(i<=3):
    sayi=int(input("i. sayıyı giriniz:"))
    if(i==1): #En küçük sayıyı belirken en büyükteki gibi bir taktik uygulayamadığımız için döngünün başında en küçük sayının bir değer almasını sağlıyoruz.
        enkucuk=sayi
    if(sayi>enbuyuk):
        enbuyuk=sayi
    if(sayi<enkucuk):
        enkucuk=sayi
    i+=1

print("En büyük sayı:",enbuyuk,"\nEn küçük sayı:",enkucuk)

