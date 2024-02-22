name = input("Ad giriniz: ")
print("Hoş geldin", name, ". Maceraya hazır ol")

print(name, ", cesur bir savaşçıydı.\n")
print("Bir gün yaşadığı köyün ayanı ondan köylerini tehdit eden bir ejderhayı öldürmesini istedi.\n")
print(f'"Dağ yoluna gada gidive {name}. Ejderhayı öte darafta görcen gari.\n"')
print(name, ', en sevdiği baltasını ve kalkanını aldı ve geçide gitti.\n')

answer = input("Karşısına buz tutmuş bir mağara, içerisinden rüzgar esen bir mağara ve dar bir patika çıktı.\n Buzlu mağaraya gir. (buzlu)\n Rüzgarlı mağaraya gir. (rüzgarlı)\n Patikayı takip et. (patika)\n").lower()
if answer == "buzlu":
    
    print(name,"buzlu mağaraya girdi. İçerisi çok soğuktu ama cesur yüreği onu sıcak tutmaya yetti.\n ")
    answer = input("Karşısına kokuşmuş bir tünel, rüzgarlı bir tünel ve dayanmış tahta bir merdiven gördü.\n Kokuşmuş tünele gir. (kokuşmuş)\n Rüzgarlı tünele gir. (rüzgarlı)\n Merdivene tırman. (merdiven)\n").lower()
    if answer == "merdiven":
        print()
    elif answer == "rüzgarlı":
        print()
    elif answer == "kokuşmuş":
        answer = input(f"Kokuyu takip ederken karşısına pis bir ork çıktı.\n Ork {name}'i görünce dikenli sopasıyla saldırıya geçti.\n Baltayı savur. (saldır)\n Kalkanı kaldır. (savun)\n").lower()
elif answer == "rüzgarlı":
    print()
elif answer == "patika":
    print()
else:
    print("Geçersiz seçenek! Macera sona erdi!")