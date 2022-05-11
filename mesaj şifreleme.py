from cryptography.fernet import Fernet
def keyUret():

okunanKey=keyOku()

mesaj=input("Mesajınız")

print(mesaj)

f=Fernet(okunanKey)

sifrelimesaj=f.encrypt(mesaj)