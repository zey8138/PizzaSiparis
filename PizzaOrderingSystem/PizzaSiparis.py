
import datetime
import csv


# menü dosyası oluşturma

menü_file = open("menü.txt", 'w', encoding='utf-8')
menü_file.write("* Lütfen Bir Pizza Tabanı Seçiniz:" +
                 "\n1: Klasik" +
                 "\n2: Margarita" +
                 "\n3: TürkPizza" +
                 "\n4: Sade Pizza" +
                 "\n* ve seçeceğiniz sos:" +
                 "\n11: Zeytin" +
                 "\n12: Mantarlar" +
                 "\n13: Keçi Peyniri" +
                 "\n14: Et" +
                 "\n15: Soğan" +
                 "\n16: Mısır" +
                 "\n* Teşekkür ederiz!")


class Pizza:
    def __init__(self,description,cost):
        self.description =description
        self.cost = cost
    
    def get_cost(self):
        return self.cost
    
    def get_description(self):
        return self.description
    


# pizzaların bilgileri burada olacak

class KlasikPizza(Pizza):
    def __init__(self):
      Pizza.__init__(self,"Pizza sosu, mozerella, sosis, sucuk, mantar, mısır içerir.", 150)
    
class MargaritaPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self,"Pizza sosu, mozerella, domates, fesleğen içerir.", 130)
        
class TürkPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self,"Pizza sosu, kaşar peyniri, sucuk, mantar, biber, soğan içerir.", 180)

class SadePizza(Pizza):
    def __init__(self):
        Pizza.__init__(self,"Pizza sosu, mozerella içerir.", 120)



#sos başlangıcı
class Decorator(Pizza):
    def __init__(self,component,description,cost):
      self.component = component
      self.cost = cost
      self.description = description
        
    def get_cost(self):
       return self.get_cost(self.component) + \
         Pizza.get_cost(self)


    def get_description(self):
       return self.get_description(self.component) + \
         ' ' + Pizza.get_description(self)
    
    class Zeytin(Decorator):
    def __init__(self, component):
      Decorator.__init__(self,component,"Zeytin",5)

class Mantar(Decorator):
    def __init__(self, component):
        Decorator.__init__(self,component,"Mantar",20)

class KeçiPeyniri(Decorator):
    def __init__(self, component):
        Decorator.__init__(self,component,"Ekstra Mozzarella",40)

class Et(Decorator):
    def __init__(self, component):
        Decorator.__init__(self,component,"Et",60)

class Soğan(Decorator):
    def __init__(self, component):
        Decorator.__init__(self,component,"Soğan",5)

class Mısır(Decorator):
    def __init__(self, component):
        Decorator.__init__(self,component,"Mısır",10)



def main():
  

    with open("menü.txt", "r",encoding="utf-8") as f:
     menü_file = f.read()
     print(menü_file)


# Pizza seç:
   
    order = int(input("Menüden sipariş etmek istediğiniz pizza numarasını girin.: "))
    while order in [1,2,3,4]:
      if order == 1:
        choice = KlasikPizza()
      elif order == 2:
        choice = MargaritaPizza()
      elif order == 3:
        choice = TürkPizza()
      elif order == 4:
        choice = SadePizza()
      else:
        print("Böyle bir ürün kodu sistemimizde bulunmuyor, tekrar deneyiniz.")


toplamTutar = 0
    sosSeçimi = int(input("Menüden eklemek istediğiniz pizza sosu numarasını girin.: "))
    while sosSeçimi in [11,12,13,14,15,16]:
        if sosSeçimi == 11:
          description = Zeytin(choice).get_description()
          toplamTutar += Zeytin(choice).get_cost()
        elif sosSeçimi == 12:
          description = Mantar(choice).get_description()
          toplamTutar += Mantar(choice).get_cost()
        elif sosSeçimi == 13:
          description = KeçiPeyniri(choice).get_description()
          toplamTutar += KeçiPeyniri(choice).get_cost()
        elif sosSeçimi == 14:
          description = Et(choice).get_description()
          toplamTutar += Et(choice).get_cost()
        elif sosSeçimi == 15:
          description = Soğan(choice).get_description()
          toplamTutar += Soğan(choice).get_cost()
        elif sosSeçimi == 16:
          description = Mısır(choice).get_description()
          toplamTutar += Mısır(choice).get_cost()
        else:
          print("Böyle bir ürün kodu bulunmuyor, tekrar deneyiniz.")
    
    print("Sipariş bilgileri: ",toplamTutar,"TL",description)
   
    time = datetime.datetime.now()
    date = datetime.datetime.strftime(time, '%c')
  
  # Ödeme Kısmı

    MüşteriAd = input("Lütfen isminizi girin.: ")
    
    TCKN = input("Lütfen TC kimlik numaranızı girin.: ")
    while len(TCKN) != 11:
        TCKN = input("Lütfen geçerli bir TC kimlik numarası girin.: ")

    KartNo=input("Ödeme için lütfen kredi kartı numaranızı girin.: ")
    while len(KartNo) != 16:
        KartNo = input("Lütfen geçerli bir kredi kartı numarası girin.: ")

    Şifre = input("Lütfen kredi kartı şifrenizi girin: ")
  
    print("Sipariş Detayları ")

# database
  
    data = [{'İsim':MüşteriAd,'TCKN':TCKN,'CardNo':KartNo,'Şifre':Şifre,'Sipariş':description,'Tarih':date}]
  
    with open("Orders_Database.csv", "a") as file:  
        writer = csv.DictWriter(file, fieldnames=['İsim','TCKN','KartNo','Şifre','Sipariş','Tarih'])
        writer.writerows(data)
        file.close()
        
main()


             


