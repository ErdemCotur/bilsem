from cryptography.fernet import Fernet
def keyUret():
    key=Fernet.generef_key()
    with open("key.txt","wb") as keyDosyasi:
        keyDosyasi.write(key)
okunanKey=keyOku()

mesaj=input("Mesajınız")

print(mesaj)

f=Fernet(keyOku)

sifrelimesaj=f.encrypt(mesaj)

# 1 key ürettik
# 2 keyi unutmamak için bir dosyaya kayıt ettik
# 3 keyi daha sonra kullanmak için keyoku fonksiyonu yazdık
# 4 kullanıcıdan mesaj aldık
# 5 Mesajı ekrana yazdırdık
# 6 Mesaji şifreledik
# 7 Şifreli mesaji ekrana yazdırdık