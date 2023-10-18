import string
import random

sifreliSozluk = {}

def sifreleme():
    for karakter in string.ascii_letters: 
        harf1 = random.choice(string.ascii_letters)
        rakam = random.choice(string.digits)
        harf2 = random.choice(string.ascii_letters)
        rakam2 = random.choice(string.digits)
        geciciDeger=harf1+rakam+harf2+karakter+rakam2 # %100 benzersiz olması için karakterin kendisinide ekledim
        sifreliSozluk[karakter] = geciciDeger

def degerSifrele():
    giris = input("Bir değer şifrele: ")
    sifreliHali = ""
    for karakter in giris:
        if karakter in sifreliSozluk:
            sifreliHali += sifreliSozluk[karakter]
        else:
            sifreliHali += karakter

    print("Şifreli hali: "+giris+ "> " + sifreliHali)
    
def sifreyiCoz():
    sifreliDeger = input("Bir şifre çöz: ")
    # Şifreli değerleri normal değerlere döndüren sözlüğün tersini al
    normalSozluk = {v: k for k, v in sifreliSozluk.items()}

    normalDeger = ""
    for i in range(0, len(sifreliDeger), 5):
        parca = sifreliDeger[i:i+5]
        if parca in normalSozluk:
            normalDeger += normalSozluk[parca]

    print("değerin şifreli ve kendi hali: "+sifreliDeger+ " >>> " + normalDeger)

sifreleme() 
degerSifrele()
sifreyiCoz()
