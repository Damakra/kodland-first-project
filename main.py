kelime_dict = {
    "NAPİM" : "ne yapayım?",
    "EZ" : "kolaydı",
    "BANE" : "banane",
    "TİLT" : "Uyuz Oldum, Sinir Oldum",
    "AFK" : "Bilgisayar başında olmayan",
    "BOOMER" : "belirli yaştan büyük kişi türkçesi ‘moruk’ anlamına gelen sözcük"
    }

kelime = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if kelime in kelime_dict.keys():
    print(kelime_dict[kelime])
else:
    print("aradığın kelimenin sözlükte bulunamadı")
    
    
 
