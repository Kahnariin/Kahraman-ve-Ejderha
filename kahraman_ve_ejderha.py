name = input("Ad giriniz: \n\n")
print("Hoş geldin", name, ". Maceraya hazır ol!\n\n")
wrong = "Geçersiz cevap! Oyunu kaybettiniz!"

story = {
    1:f"{name} cesur bir Kuzey savaşçısıydı.\n Bir gün Şefi, {name}'dan köylerini tehdit eden şeytani bir ejderhayı öldürmesini istedi.\n Şefi 'Dağ geçidinden geç {name}' dedi. 'Ejderhayı diğer tarafta bulacaksın.'\n\n",
    2:f"{name} en sevdiği baltasını ve kalkanını alıp geçide doğru yürüdü;\n burada soğuk bir mağara, rüzgarlı bir mağara ve dar bir patika buldu.\n\n",
    3:f"{name} kayalık bir tepeye adım attı.\n Aşağıda uyuyan ejderhayı ve yakındaki bir yolun kenarındaki bir meyhaneyi görebiliyordu.\n\n",
    4:f"Kokunun ardından {name} pis bir ork buldu!\n Ork hırladı ve çivili sopasıyla {name}'a saldırdı.\n\n",
    5:f"Bataklıkta yürürken {name},\n ağlayan bir hayaletin yolunu kapattığını fark etti.\n\n",
    6:f"Baltanın başı canavarın sert, pullu boynuna saplandı.\n Hayvan feryat etti ve çırpındı ama {name} dayandı\n ve sonunda canavarın boynunu keserek öldürdü.\n {name} eve zaferle döndü ve köyü bir daha asla ejderha tarafından rahatsız edilmedi.\n\n",
    7:f"Bataklığı arkasında bırakan {name}, yakındaki ejderhanın ininin\n yanı sıra küçük, davetkar bir tavernayı da görebiliyordu.\n\n",
    8:f"Kuvvetli bir rüzgar {name}'un meşalesini patlattı ve onu bir çukura düşürdü,\n orada kafasını yardı ve öldü.\n SON\n\n",
    9:f"Sopası {name}'un kalkanını parçalayıp yüzüne çarptığında ork kıkırdadı.\n Orada {name} öldü ve ork kemiklerinden çorba içti.\n SON\n\n",
    10:f"{name}, büyükannesinin ona anlattığı bir hikayeyi hatırladı ve hayalete iki altın attı.\n Hayalet, onun geçmesine izin vererek kayboldu.\n\n",
    11:f"{name} canavarın karnına doğru süründü ama gözlerini canavarın kafasından ayırır ayırmaz hayvan onu kaptı ve baltasıyla birlikte bütünüyle yedi.\n SON\n\n",
    12:f"{name} yukarı tırmanırken bir kamp buldu.\n Tanıştığı avcı yemeğini paylaştı ve ona ejderhanın inine giden iki ayrı yol gösterdi.\n Biri tepelerden, diğeri bataklıktan geçiyordu.\n\n",
    13:f"Ork saldırmadan önce {name} güçlü baltasını savurdu.\n Orkun kafası ve sopası faydasız bir şekilde yere düştü.\n\n",
    14:f"{name}, ejderhayla savaşmadan önce dinlenmek için meyhanede durdu. Ancak meyhaneyi Yüce Elfler yönetiyor ve altınını çalabilmek için bal likörünü zehirliyorlardı.\n SON\n\n",
    15:f"{name} baltasını elinden geldiğince sert bir şekilde savurdu ama hayalet bunu pek fark etmemiş gibiydi.\n Hayalet {name}'a doğru sürüklendi ve onu bir daha asla uyanmadığı derin bir uykuya teslim etti.\n SON\n\n",
    16:f"{name}, burun deliklerinden dumanlar çıkan ejderhanın uyuduğu sığınağı buldu.\n Hava, {name}'un gözlerini yaktı ve neredeyse adamların kemiklerinin üzerinden kayıyordu, temizlenmişti.\n Canavar yan yatmıştı, hem boğazı hem de karnı hedef bekliyordu.\n\n",
    17:f"{name} donmuş mağaraya adım attı ama Kuzeyli kanı onu sıcak tuttu.\n Pis kokulu bir tünel tepesine tırmandı ve solundaki bir başka tünelden rüzgar uğulduyordu.\n Yakında bir merdiven de vardı.\n\n"
}


print(story.get(1))
print(story.get(2))
answer = input("\n(a) Soğuk mağaraya gir. \n(b) Rüzgarlı mağaraya gir. \n(c) Dar patikayı takip et.\n\n").lower()
if answer == "a":
    print(story.get(17))
    answer = input("\n(a) Kokulu tünele gir. \n(b) Rüzgarlı tünele gir. \n(c) Merdivene tırman. \n\n")
    if answer == "a":
        print(story.get(4))
        answer = input("\n(a) Kalkanı kaldır. \n(b) Baltayı savur. \n\n")
        if answer == "a":
            print(story.get(9))
        elif answer == "b":
            print(story.get(13))
            print(story.get(3))
            answer = input("\n(a) Aşağı in. \n(b) Tavernaya gir. \n\n")
            if answer == "a":
                print(story.get(16))
                answer = input("\n(a) Boynuna saldır. \n(b) Karnına saldır.\n\n")
                if answer == "a":
                    print(story.get(6))
                elif answer == "b":
                    print(story.get(11))
                else:
                    print(wrong)
            elif answer == "b":
                print(story.get(14))
        else:
            print(wrong)
    elif answer == "b":
        print(story.get(8))
    elif answer == "c":
        print(story.get(12))
    else:
        print(wrong)
elif answer == "b":
    print(story.get(8))
elif answer == "c":
    print(story.get(12))
    answer = input("\n(a) Tepelerden geç. \n(b) Bataklıktan geç. \n\n")
    if answer == "a":
        print(story.get(3))
        answer = input("\n(a) Aşağı in. \n(b) Tavernaya gir. \n\n")
        if answer == "a":
            print(story.get(16))
            answer = input("\n(a) Boynuna saldır. \n(b) Karnına saldır.\n\n")
            if answer == "a":
                print(story.get(6))
            elif answer == "b":
                print(story.get(11))
            else:
                print(wrong)
        elif answer == "b":
            print(story.get(14))
        else:
            print(wrong)
    elif answer == "b":
        print(story.get(5))
        answer = input("\n(a) Hayalete saldır. \n(b) Altın ver. \n\n")
        if answer == "a":
            print(story.get(15))
        elif answer == "b":
            print(story.get(10))
            print(story.get(7))
            answer = input("\n(a) Yuvaya git. \n(b) Tavernaya git. \n\n")
            if answer == "a":
                print(story.get(16))
                answer = input("\n(a) Boynuna saldır. \n(b) Karnına saldır.\n\n")
                if answer == "a":
                    print(story.get(6))
                elif answer == "b":
                    print(story.get(11))
                else:
                    print(wrong)
            elif answer == "b":
                print(story.get(14))
            else:
                print(wrong)
        else:
            print(wrong)
    else:
        print(wrong)
else:
    print(wrong)