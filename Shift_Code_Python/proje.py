def kodlama(mesaj, kaydirma_sayisi):# burada mesajı kodlamak için bir fonksiyon olusturdum.
    kodlanmis_mesaj = "" # en basta kodlanmıs mesajımız yok o yüzden böyle tanımladım.
    for harf in mesaj: # mesajın harflerini sırayla döngüye sokuyorum.
        if harf.isalpha(): #girilen mesajın harflerden olusması gerekiyor burada onu kontrol ediyoruz.
            alfabe = "abcdefghijklmnopqrstuvwxyz" #İngiliz alfabesi kullandım Türk alfabesinde bazı harfler sıkıntılı.
            harf_index = alfabe.index(harf.lower()) # harfi küçük harfe cevirip(büyük harfle yazıldıysa da cıktı kucuk harfle olur) o harfın alfabede kacıncı sırada oldugunu buluyorum
            yeni_index = (harf_index + kaydirma_sayisi) % 26 # harfin indeksiyle kaydirma sayısını topluyorum ve 26 harf içeren alfabedeki yeni konumunu belirliyorum
            yeni_harf = alfabe[yeni_index]
            kodlanmis_mesaj = kodlanmis_mesaj+ yeni_harf
        else:# noktalama işareti, saayılar girildiyse metin aynı kalır, değişmez sadece harflerde çalışır.
            kodlanmis_mesaj= kodlanmis_mesaj + harf

    return kodlanmis_mesaj # kodlanmıs oldugum mesajı geri döndürüyorum.



def kodu_cozme(kodlanmis_mesaj, kaydirma_sayisi): # bu da kodlanmıs mesajı asıl haline(kodlanmamıs) dönüştürüyorum.
    return kodlama(kodlanmis_mesaj, -kaydirma_sayisi) # kaydırma sayisini eksi olarak aldım çünkü o sayı kadar geriye gideceğim.



while True: # bu kosul dogru olduğu süre boyunca çalışır.
    print("Menü:\n 1. Mesajı kodlamak için,\n 2. Mesajı kod çözmek için,\n 3. Programdan çıkmak için")
    secim = input("Lütfen seçiminizi yapınız (1/2/3): ")

    if secim == "1":  # secim 1 ise mesajı kodlarız
        mesaj = input("Kodlama yapmak istediğiniz mesajı giriniz: ")
        try:# kullancıı  kaydırma sayısını yanlıslıkla harf girebilir sayi girmek yerine 
            kaydirma_sayisi = int(input("Kaydırma sayısını giriniz: "))
            kodlanmis_mesaj = kodlama(mesaj, kaydirma_sayisi) # mesajı kodlamak için kodlama fonksiyonunu çağırırız.
            print("Kodlanmış Mesaj:", kodlanmis_mesaj)
        except ValueError: # hatayı kullanıcıya bildiririz.
            print("Hata: Geçersiz bir sayı girişi yapılmıştır.")
    elif secim == "2": # secim 2 ise kodlanmıs mesajın asıl halini buluruz
        kodlanmis_mesaj = input("Kodlanmış mesajı giriniz: ")
        try:
            kaydirma_sayisi = int(input("Kaydırma sayısını giriniz: "))
            orijinal_mesaj = kodu_cozme(kodlanmis_mesaj, kaydirma_sayisi) # kodlanmıs mesajı çözmek için kodu_cozme fonk. cağrılır.
            print("Orijinal Mesaj:", orijinal_mesaj)
        except ValueError:
            print("Hata: Geçersiz bir sayı girişi yapılmıştır.")
    elif secim == "3": # secim 3 ise de programdan çıkılır
        print("Programdan çıkış yapılıyor.")
        break
    else:
        print("Geçersiz seçim yaptınız. Lütfen 1, 2 veya 3 girin.")






