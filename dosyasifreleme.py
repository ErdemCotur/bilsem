# 1 Metin.txt de adımda bir dosya oluşturunuz içine adınızı yazınız
# 2 key üretiniz
# 3 bu keyi kullanarak metin.txt dosyamızın içeriği değişip şifreli olarak kayıt ediniz

from cryptography.fernet import Fernet
def keyUret():
    key=Fernet.generef_key()
    with open("key.txt","wb") as keyDosyasi:
        keyDosyasi.write(key)