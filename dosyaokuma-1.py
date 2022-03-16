file=open("bilgiler.txt","w",encoding="utf-8")
#w: dosya oluşturma modu. dosya var ise silip tekrar oluşturur
#encoding: türkçe karakterleri okuyabilmesi için
#nereye oluşturulur?: phyton file dosyası neredeyse oraya
file.write("Merhaba metin belgesi....\n\n")
file.write("Bugün txt dosyalarına yazı yazmayı öğreniyorum\n")
file.close() #açılan herşeyi kapamak zorundayım