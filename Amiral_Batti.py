import random
from random import randint

while True:

    alan = int(input("Oyun alani: "))
    oyunAlani = []

    if (alan<10):
        print("Lütfen tekrar deneyiniz.")

    else:
        for i in range(alan):
            oyunAlani.append(["?"] * alan)

    hak = (alan * alan) // 3
    p1, p2, p3, p4 = 0, 0, 0, 0

    def haritayiYazdir(oyunalani):
        for satir in oyunalani:
            print(" ".join(satir))

    #gemileri oluşturmak

    def koordinatlar(oyunAlani):
        return random.randint(0, len(oyunAlani) - 1)

    g1 = [koordinatlar(oyunAlani), koordinatlar(oyunAlani)]
    g2 = [koordinatlar(oyunAlani), koordinatlar(oyunAlani)]
    g3 = [koordinatlar(oyunAlani), koordinatlar(oyunAlani)]
    g4 = [koordinatlar(oyunAlani), koordinatlar(oyunAlani)]

    #koordinatların çakışma durumu

    if g1 in g2:
        g1 = [koordinatlar(oyunAlani), koordinatlar(oyunAlani)]
    elif g1 in g3:
        g1 = [koordinatlar(oyunAlani), koordinatlar(oyunAlani)]
    elif g1 in g4:
        g1 = [koordinatlar(oyunAlani), koordinatlar(oyunAlani)]
    elif g2 in g3:
        g2 = [koordinatlar(oyunAlani), koordinatlar(oyunAlani)]
    elif g2 in g4:
        g2 = [koordinatlar(oyunAlani), koordinatlar(oyunAlani)]
    elif g3 in g4:
        g3 = [koordinatlar(oyunAlani), koordinatlar(oyunAlani)]

    gemiYeri = [[g2, [g2[0], g2[1] + 1]], [g2, [g2[0], g2[1] - 1]], [g2, [g2[0] + 1], g2[1]], [g2, [g2[0] - 1], g2[1]]]
    gemiYeri = random.choice(gemiYeri)

    gemiYeri2 = [[g3, [g3[0], g3[1] + 1]], [g3, [g3[0], g3[1] - 1]], [g3, [g3[0] + 1], g3[1]], [g3, [g3[0] - 1], g3[1]]]
    gemiYeri2 = random.choice(gemiYeri2)

    gemiYeri3 = [[g4, [g4[0], g4[1] + 1]], [g4, [g4[0], g4[1] - 1]], [g4, [g4[0] + 1], g4[1]], [g4, [g4[0] - 1], g4[1]]]
    gemiYeri3 = random.choice(gemiYeri3)

    gemiler = [g1,gemiYeri,gemiYeri2,gemiYeri3]

    #tekrar çakışma durumu

    if gemiler[0] in gemiler[1]:
        g1 = [koordinatlar(oyunAlani), koordinatlar(oyunAlani)]
    elif gemiler[0] in gemiler[2]:
        g1 = [koordinatlar(oyunAlani), koordinatlar(oyunAlani)]
    elif gemiler[0] in gemiler[3]:
        g1 = [koordinatlar(oyunAlani), koordinatlar(oyunAlani)]
    elif gemiler[1] in gemiler[2]:
        gemiler[1] = [koordinatlar(oyunAlani), koordinatlar(oyunAlani)]
    elif gemiler[1] in gemiler[3]:
        gemiler[1] = [koordinatlar(oyunAlani), koordinatlar(oyunAlani)]
    elif gemiler[2] in gemiler[3]:
        gemiler[2] = [koordinatlar(oyunAlani), koordinatlar(oyunAlani)]

    haritayiYazdir(oyunAlani)

    print("Oyunu hangi modda oynamak istersiniz: \n1 -> Açık Mod \n2 -> Gizli Mod")
    secim = input("Secim: ")

    if secim == "1":  # Açık Mod
        oyunAlani[g1[0]][g1[1]] = "G"
        oyunAlani[gemiYeri[0][0]][gemiYeri[0][1]] = "G"
        oyunAlani[gemiYeri[1][0]][gemiYeri[1][1]] = "G"
        oyunAlani[gemiYeri2[0][0]][gemiYeri2[0][1]] = "G"
        oyunAlani[gemiYeri2[1][0]][gemiYeri2[1][1]] = "G"
        oyunAlani[gemiYeri3[0][0]][gemiYeri3[0][1]] = "G"
        oyunAlani[gemiYeri3[1][0]][gemiYeri3[1][1]] = "G"

        haritayiYazdir(oyunAlani)

        while True:
            satir = int(input("Kaçıncı Satır: "))
            sutun = int(input("Kaöıncı Sütun: "))

            tahmin = [satir, sutun]

            if oyunAlani[satir - 1][sutun - 1] == "G" or tahmin in gemiler:
                if oyunAlani[satir - 1][sutun - 1] == "X":
                    hak -=1
                    print(f"Önceden vurmuştunuz.Kalan hakkın: {hak}")
                    haritayiYazdir(oyunAlani)
                else:
                    hak -=1
                    oyunAlani[satir - 1][sutun - 1] = "X"
                    print(f"Tebrikler bir gemi vurdunuz. Kalan hakkın: {hak}")
                    haritayiYazdir(oyunAlani)

                    if oyunAlani[g1[0]][g1[1]] == "X":
                        print(f"Tebrikler 1. gemiyi batırdıınız. Kalan hakkın: {hak}")
                        p1 +=1
                        haritayiYazdir(oyunAlani)

                    elif oyunAlani[gemiYeri[0][0]][gemiYeri[0][1]] == "X" and oyunAlani[gemiYeri[1][0]][gemiYeri[1][1]] == "X":
                        print(f"Tebrikler 2. gemiyi vurdunuz. Kalan hakkın: {hak}")
                        p2 +=1
                        haritayiYazdir(oyunAlani)

                    elif oyunAlani[gemiYeri2[0][0]][gemiYeri2[0][1]] == "X" and oyunAlani[gemiYeri2[1][0]][gemiYeri2[1][1]] == "X" and oyunAlani[gemiYeri2[2][0]][gemiYeri2[2][1]] == "X":
                        print(f"Tebrikler 3. gemiyi vurdunuz. Kalan hakkın: {hak}")
                        p3 +=1
                        haritayiYazdir(oyunAlani)

                    elif oyunAlani[gemiYeri3[0][0]][gemiYeri3[0][1]] == "X" and oyunAlani[gemiYeri3[1][0]][gemiYeri3[1][1]] == "X" and oyunAlani[gemiYeri3[2][0]][gemiYeri3[2][1]] == "X" and oyunAlani[gemiYeri3[3][0]][gemiYeri3[3][1]] == "X":
                        print(f"Tebrikler 4. gemiyi vurdunuz. Kalan hakkın: {hak}")
                        p4 +=1
                        haritayiYazdir(oyunAlani)
            else:
                if tahmin[0] < 0 or tahmin[1] < 0 or tahmin[0] > alan or tahmin[1] > alan:
                    hak -=1
                    print(f"Koskoca alanda dışarıyı tamin ettin. Kalan hakkın: {hak}" )
                    haritayiYazdir(oyunAlani)

                elif oyunAlani[satir - 1][sutun - 1] == "*":
                    hak -=1
                    print(f"Önceden vrumuştun. Kalan hakkın: {hak}")
                    haritayiYazdir(oyunAlani)
                else:
                    oyunAlani[satir - 1][sutun - 1] = "*"
                    hak -=1
                    print(f"Tutturamadın beee. KAlan hakkın: {hak}")
                    haritayiYazdir(oyunAlani)
            if hak <= 0:
                print(f"Maalesef verilen hakları kullanırken oyunu bitiremedin. Gemilerin yerleri: \n1.Gemi-> {g1}\n2.Gemi-> {gemiYeri}\n3.Gemi-> {gemiYeri2}\n4.Gemi-> {gemiYeri3}")
                break
            elif p1 ==1 and p2 == 1 and p3 == 1 and p4 == 1 and hak >= 1:
                print(f"Bravo. Verilen haklar dahilinde tüm gemileri vurdunuz ve {hak} puan aldıınız.")

    elif secim =="2": #Gizli Mod
        haritayiYazdir(oyunAlani)

        while True:
            satir = int(input("Kaçıncı Satır: "))
            sutun = int(input("Kaöıncı Sütun: "))

            tahmin = [satir, sutun]

            if tahmin in gemiler :
                if oyunAlani[satir - 1][sutun - 1] == "X":
                    hak -=1
                    print(f"Önceden vurmuştunuz.Kalan hakkın: {hak}")
                    haritayiYazdir(oyunAlani)
                else:
                    hak -=1
                    oyunAlani[satir - 1][sutun - 1] = "X"
                    print(f"Tebrikler bir gemi vurdunuz. Kalan hakkın: {hak}")
                    haritayiYazdir(oyunAlani)

                    if oyunAlani[g1[0]][g1[1]] == "X":
                        print(f"Tebrikler 1. gemiyi batırdıınız. Kalan hakkın: {hak}")
                        p1 +=1
                        haritayiYazdir(oyunAlani)

                    elif oyunAlani[gemiYeri[0][0]][gemiYeri[0][1]] == "X" and oyunAlani[gemiYeri[1][0]][gemiYeri[1][1]] == "X":
                        print(f"Tebrikler 2. gemiyi vurdunuz. Kalan hakkın: {hak}")
                        p2 +=1
                        haritayiYazdir(oyunAlani)

                    elif oyunAlani[gemiYeri2[0][0]][gemiYeri2[0][1]] == "X" and oyunAlani[gemiYeri2[1][0]][gemiYeri2[1][1]] == "X" and oyunAlani[gemiYeri2[2][0]][gemiYeri2[2][1]] == "X":
                        print(f"Tebrikler 3. gemiyi vurdunuz. Kalan hakkın: {hak}")
                        p3 +=1
                        haritayiYazdir(oyunAlani)

                    elif oyunAlani[gemiYeri3[0][0]][gemiYeri3[0][1]] == "X" and oyunAlani[gemiYeri3[1][0]][gemiYeri3[1][1]] == "X" and oyunAlani[gemiYeri3[2][0]][gemiYeri3[2][1]] == "X" and oyunAlani[gemiYeri3[3][0]][gemiYeri3[3][1]] == "X":
                        print(f"Tebrikler 4. gemiyi vurdunuz. Kalan hakkın: {hak}")
                        p4 +=1
                        haritayiYazdir(oyunAlani)
            else:
                if tahmin[0] < 0 or tahmin[1] < 0 or tahmin[0] > alan or tahmin[1] > alan:
                    hak -=1
                    print(f"Koskoca alanda dışarıyı tamin ettin. Kalan hakkın: {hak}" )
                    haritayiYazdir(oyunAlani)

                elif oyunAlani[satir - 1][sutun - 1] == "*":
                    hak -=1
                    print(f"Önceden vrumuştun. Kalan hakkın: {hak}")
                    haritayiYazdir(oyunAlani)
                else:
                    oyunAlani[satir - 1][sutun - 1] = "*"
                    hak -=1
                    print(f"Tutturamadın beee. KAlan hakkın: {hak}")
                    haritayiYazdir(oyunAlani)
            if hak <= 0:
                print(f"Maalesef verilen hakları kullanırken oyunu bitiremedin. Gemilerin yerleri: \n1.Gemi-> {g1}\n2.Gemi-> {gemiYeri}\n3.Gemi-> {gemiYeri2}\n4.Gemi-> {gemiYeri3}")
                break
            elif p1 ==1 and p2 == 1 and p3 == 1 and p4 == 1 and hak >= 1:
                print(f"Bravo. Verilen haklar dahilinde tüm gemileri vurdunuz ve {hak} puan aldıınız.")
    print("FİNİSH")
    print("Oyuna baştan başlamak isterseniz 1'i, Bitirmek isterseniz 2'yi seçiniz.")
    secim2 = int(input("Seciminiz: "))

    if secim2 == "2":
        break

    else:
        print("Yanlış seçenek.")