defarabamarkası=["BMW 3.18","BMW 5.20","W","Mercedes"]


while(True):
    arabamarkası=input("araba modeli giriniz:")
    arabakiralamagünsayısı=int(input("Kaç günlük kiralamak istediğinizi giriniz:"))

    if(arabamarkası == defarabamarkası[0]):
        print("BMW"+str(3.18),"year:"+str(2018),"amount:"+ str(8),"daily_price:"+str(140))
        price = 140
        print("Toplam ücret:",arabakiralamagünsayısı*price)

        break
    elif(arabamarkası == defarabamarkası[1]):
        print("BMW"+str(5.20),"year:"+str(2017),"amount:"+ str(3),"daily_price:"+str(210))
        price=150
        print("Toplam ücret:",arabakiralamagünsayısı*price)
        break
    elif(arabamarkası == defarabamarkası[2]):
        print("W Passat", "year:"+str(2014),"amount:"+ str(3),"daily_price:"+ str(120))
        price=200
        print("Toplam ücret:",arabakiralamagünsayısı*price)
        break
    elif(arabamarkası == defarabamarkası[3]):
        print("Mercedes A 180"+str(3.18),"year:"+str(2019),"amount:"+ str(4),"daily_price:"+str(120))
        price=190
        print("Toplam ücret:",arabakiralamagünsayısı*price)
        break
    else:
        print("not found")

        