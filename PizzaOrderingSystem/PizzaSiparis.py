import datetime
import csv

# Menü dosyası oluşturuluyor
with open("menü.txt", 'w', encoding='utf-8') as menü_file:
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

# Temel Pizza Sınıfı
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description

# Alt Pizza Sınıfları
class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__("Pizza sosu, mozerella, sosis, sucuk, mantar, mısır içerir.", 150)

class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__("Pizza sosu, mozerella, domates, fesleğen içerir.", 130)

class TürkPizza(Pizza):
    def __init__(self):
        super().__init__("Pizza sosu, kaşar peyniri, sucuk, mantar, biber, soğan içerir.", 180)

class SadePizza(Pizza):
    def __init__(self):
        super().__init__("Pizza sosu, mozerella içerir.", 120)

# Decorator Sınıfı
class Decorator(Pizza):
    def __init__(self, component, description, cost):
        self.component = component
        self.description = description
        self.cost = cost

    def get_cost(self):
        return self.component.get_cost() + self.cost

    def get_description(self):
        return self.component.get_description() + " + " + self.description

# Sos Sınıfları
class Zeytin(Decorator):
    def __init__(self, component):
        super().__init__(component, "Zeytin", 5)

class Mantar(Decorator):
    def __init__(self, component):
        super().__init__(component, "Mantar", 20)

class KeçiPeyniri(Decorator):
    def __init__(self, component):
        super().__init__(component, "Keçi Peyniri", 40)

class Et(Decorator):
    def __init__(self, component):
        super().__init__(component, "Et", 60)

class Soğan(Decorator):
    def __init__(self, component):
        super().__init__(component, "Soğan", 5)

class Mısır(Decorator):
    def __init__(self, component):
        super().__init__(component, "Mısır", 10)

# Ana Fonksiyon
def main():
    # Menü gösterimi
    with open("menü.txt", "r", encoding="utf-8") as f:
        print(f.read())

    # Pizza seçimi
    pizza_num = int(input("Menüden pizza numarasını giriniz: "))
    if pizza_num == 1:
        choice = KlasikPizza()
    elif pizza_num == 2:
        choice = MargaritaPizza()
    elif pizza_num == 3:
        choice = TürkPizza()
    elif pizza_num == 4:
        choice = SadePizza()
    else:
        print("Geçersiz seçim, program sonlandırıldı.")
        return

    # Sos seçimi
    sos_num = int(input("Menüden sos numarasını giriniz: "))
    if sos_num == 11:
        choice = Zeytin(choice)
    elif sos_num == 12:
        choice = Mantar(choice)
    elif sos_num == 13:
        choice = KeçiPeyniri(choice)
    elif sos_num == 14:
        choice = Et(choice)
    elif sos_num == 15:
        choice = Soğan(choice)
    elif sos_num == 16:
        choice = Mısır(choice)
    else:
        print("Geçersiz sos seçimi, program sonlandırıldı.")
        return

    # Sipariş özeti
    description = choice.get_description()
    total_cost = choice.get_cost()
    print("\nSiparişiniz:", description)
    print("Toplam Tutar: ₺", total_cost)

    # Ödeme bilgileri
    isim = input("\nLütfen adınızı girin: ")
    tckn = input("Lütfen 11 haneli TCKN girin: ")
    while len(tckn) != 11 or not tckn.isdigit():
        tckn = input("Geçerli bir TCKN girin (11 haneli): ")

    kart_no = input("Kredi kartı numaranızı girin (16 haneli): ")
    while len(kart_no) != 16 or not kart_no.isdigit():
        kart_no = input("Geçerli bir kart numarası girin (16 haneli): ")

    sifre = input("Kart şifrenizi girin: ")

    tarih = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # CSV'ye yazma
    with open("Orders_Database.csv", "a", newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["İsim", "TCKN", "KartNo", "Şifre", "Sipariş", "Tarih"])
        writer.writerow({
            "İsim": isim,
            "TCKN": tckn,
            "KartNo": kart_no,
            "Şifre": sifre,
            "Sipariş": description,
            "Tarih": tarih
        })

    print("\nSiparişiniz başarıyla alınmıştır, teşekkür ederiz!")

# Programı çalıştır
main()



             


