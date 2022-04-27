import shutil
import os

tane = 0
for kok,altdizin,dosya in os.walk("C:/Users/ogr9/Desktop/fotoğraf2345"):
    for alt in altdizin:
        for dosya in dosyalar:
            try:
                os.mkdir(alt)
            except:
                pass
            print(alt)
            shutil.copy(kok +"/"+ dosya, alt +"/"+dosya)    
            print(kok)
