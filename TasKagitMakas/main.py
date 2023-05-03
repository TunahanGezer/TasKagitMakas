import random
print("Tas-Kagit-Makas Oyununa Hoşgeldin !!!\n-----------------------")
def kullanici_sec():
    secim = input("Tas mı, Kagit mı, Makas mı? ").lower()
    while secim not in ["tas", "kagit", "makas"]:
        secim = input("Lütfen geçerli bir seçim yapın. Tas-Kagit-Makas").lower()
    return secim

def pc_sec():
    secenekler=["tas","kagit","makas"]
    return random.choice(secenekler)

def sonuc(kullanci_sec,pc_sec):
    if pc_sec==kullanci_sec:
        return "Berabere!"
    elif kullanci_sec=="tas":
        if pc_sec=="kagit":
            return "Kaybettin!"
        if pc_sec=="makas":
            return "Kazandın!"
    elif kullanci_sec=="kagit":
        if pc_sec=="makas":
            return "Kaybettin!"
        else:
            return "Kazandın!"

while True:
    kullanici = kullanici_sec()
    bilgisayar = pc_sec()
    print("Senin Seçimin:", kullanici)
    print("Bilgisayarın Beçimi:", bilgisayar)
    print(sonuc(kullanici, bilgisayar))
    print("---------------------------")
    tekrar= input("Tekrar oynamak istiyor musun? (Evet/Hayir)").lower()
    if tekrar=="Evet".lower():
        continue
    else:
        break