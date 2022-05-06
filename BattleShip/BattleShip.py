import random
OyunAlani = []

boyut = int(input("oyun alanı AxA, A="))

def generate_board():
    for i in range(0,boyut):
        OyunAlani.append([])
        for j in range(0,boyut):
            OyunAlani[i].append(["?",0])

def display_board(sayi):
    print("\n")
    if sayi == 0:
        for Row in range(0, boyut):
            for Column in range(0, boyut):
                print(" {} ".format(OyunAlani[Row][Column][0]), end='  ')
            print("\n")
    else:
        for Row in range(0, boyut):
            for Column in range(0, boyut):
                print(" {} ".format(OyunAlani[Row][Column][1]), end='  ')
            print("\n")

def randomGemi():
    # 4 uzunluklu gemi oluşturma
    gemi4 = random.sample(range(0, boyut - 4), 2)
    OyunAlani[gemi4[0]][gemi4[1]][1] = 4
    duzmu = random.randint(0, 1)  # gemi yatay mı dikey mi
    if duzmu:
        OyunAlani[gemi4[0] + 1][gemi4[1]][1] = 4
        OyunAlani[gemi4[0] + 2][gemi4[1]][1] = 4
        OyunAlani[gemi4[0] + 3][gemi4[1]][1] = 4
    else:
        OyunAlani[gemi4[0]][gemi4[1] + 1][1] = 4
        OyunAlani[gemi4[0]][gemi4[1] + 2][1] = 4
        OyunAlani[gemi4[0]][gemi4[1] + 3][1] = 4

    control = 0
    control2 = 0
    control3 = 0

    # 3 uzunluklu gemi oluşturma diğer gemilerle çakışma kontrol
    while (control == 0):
        gemi3 = random.sample(range(0, boyut - 3), 2)
        duzmu = random.randint(0, 1)

        if duzmu == 1 and OyunAlani[gemi3[0] + 1][gemi3[1]][1] == 0 and OyunAlani[gemi3[0] + 2][gemi3[1]][1] == 0 and OyunAlani[gemi3[0]][gemi3[1]][1] == 0:
            OyunAlani[gemi3[0]][gemi3[1]][1] = 3
            OyunAlani[gemi3[0] + 1][gemi3[1]][1] = 3
            OyunAlani[gemi3[0] + 2][gemi3[1]][1] = 3
            control = 1

        elif duzmu == 0 and OyunAlani[gemi3[0]][gemi3[1] + 1][1] == 0 and OyunAlani[gemi3[0]][gemi3[1] + 2][1] == 0 and OyunAlani[gemi3[0]][gemi3[1]][1] == 0:
            OyunAlani[gemi3[0]][gemi3[1]][1] = 3
            OyunAlani[gemi3[0]][gemi3[1] + 1][1] = 3
            OyunAlani[gemi3[0]][gemi3[1] + 2][1] = 3
            control = 1

    # 2 uzunluklu gemi oluşturma diğer gemilerle çakışma kontrol
    while(control2 == 0):
        gemi2 = random.sample(range(0, boyut - 2), 2)
        duzmu = random.randint(0, 1)

        if duzmu == 1 and OyunAlani[gemi2[0] + 1][gemi2[1]][1] == 0 and OyunAlani[gemi2[0]][gemi2[1]][1] == 0:
            OyunAlani[gemi2[0]][gemi2[1]][1] = 2
            OyunAlani[gemi2[0] + 1][gemi2[1]][1] = 2
            control2 = 1
        elif duzmu == 0 and OyunAlani[gemi2[0]][gemi2[1] + 1][1] == 0 and OyunAlani[gemi2[0]][gemi2[1]][1] == 0:
            OyunAlani[gemi2[0]][gemi2[1]][1] = 2
            OyunAlani[gemi2[0]][gemi2[1] + 1][1] = 2
            control2 = 1

    # 1 uzunluklu gemi oluşturma diğer gemilerle çakışma kontrol
    while(control3 == 0):
        gemi1 = random.sample(range(0, boyut - 1), 2)
        if OyunAlani[gemi1[0]][gemi1[1]][1] == 0:
            OyunAlani[gemi1[0]][gemi1[1]][1] = 1
            control3 = 1

#Oyun

hak=(boyut**2)//3
denk=0
restart = 1

while (restart == 1):
    generate_board()
    randomGemi()
    count = 0
    count2 = 0
    count3 = 0
    count4 = 0
    sayi = int(input("Gizli mod(0) mu açık mod(1) mu:"))
    while (hak > 0):
        display_board(sayi)
        print("kalan hak saiyiniz {} dir".format(hak))
        print("vurduğunuz sayi {} dir".format(count+count2+count3+count4))

        i = int(input("Give me sütun (0 - " + (boyut - 1).__str__() + ") : "))
        j = int(input("Give me satır (0 - " + (boyut - 1).__str__() + ") : "))

        if (OyunAlani[i][j][1] > 0):
            if (OyunAlani[i][j][1] == 1):
                print("gemiyi batırdınız")
                OyunAlani[i][j][0] = "X"
                count = 1
            elif(OyunAlani[i][j][1] == 2):
                count2 +=1
                print("gemiyi vurdunuz")
                OyunAlani[i][j][0] = "*"
                if(count2 == 2):
                    print("gemiyi batırdınız")
                    OyunAlani[i][j][0] = "X"
            elif (OyunAlani[i][j][1] == 3):
                count3 += 1
                print("gemiyi vurdunuz")
                OyunAlani[i][j][0] = "*"
                if (count3 == 3):
                    print("gemiyi batırdınız")
                    OyunAlani[i][j][0] = "X"
            elif (OyunAlani[i][j][1] == 4):
                count4 += 1
                print("gemiyi vurdunuz")
                OyunAlani[i][j][0] = "*"
                if (count4 == 4):
                    print("gemiyi batırdınız")
                    OyunAlani[i][j][0] = "X"
        else:
            print("maalesef vuramadınız")
            OyunAlani[i][j][0] = "0"


        hak -=1
        if(hak == 0):
            print("oyun hakkınız kalmadı oyun bitti")
            break
        elif( count+count2+count3+count4)==10:
            print("oyunu kazandınz oyun bitti")
            restart = int(input("oyunu tekrar oynamak isterseniz 1 e basınız kapatmak için herhangi bi tuş yeterli:"))
            break





