def simalista(filepath: str) -> list:
    lista = []
    try:
        f = open(filepath, "r", encoding="UTF-8")

        for sor in f:
            sor = sor.strip()
            lista.append(sor)

        return lista

        f.close()
    except FileNotFoundError:
        print("Hiba!")

def feladat_1(sima_lista: list) -> list:
    rendezett_lista = []
    kicsikosar = []


    for i in range(len(sima_lista)):
        if sima_lista[i] != "F":
            kicsikosar.append(sima_lista[i])
        if sima_lista[i] == "F":
            rendezett_lista.append(kicsikosar)
            kicsikosar = []

    print("1. feladat: A kosar.txt beolvasása.")

    return  rendezett_lista

def feladat_2(lst: list) -> int:
    print(f"2. feladat: {len(lst)} alkalommal fizettek a pénztárnál.")

def feladat_3(lst: list):

    try:
        sorszam = int(input("3. feladat: Adja meg a vásárlás sorszámát: "))

        if sorszam > len(lst):
            print("Nem volt ilyen sorszámmal vásárlás.")
        else:
            print(f"{len(lst[sorszam - 1])} termék volt a kosárban.")
            print("A kosár tartalma: ")
            # for i in lst[sorszam-1]:
            #     print("\t",i)
            kicsi_lista = lst[sorszam - 1]
            # print(kicsi_lista)
            kisebb_lista = list(dict.fromkeys(kicsi_lista))
            # print(kisebb_lista)
            kisebb_db = []
            for i in kisebb_lista:
                kisebb_db.append(0)
            ures = kisebb_db
            for j in range(len(kisebb_lista)):
                for i in kicsi_lista:
                    if i == kisebb_lista[j]:
                        kisebb_db[j] += 1

            # print(kisebb_db)

            for i in range(len(kisebb_lista)):
                print("\t", kisebb_db[i], kisebb_lista[i])
            osszeg = 0

            # elso
            for i in range(len(kisebb_db)):
                if kisebb_db[i] > 0:
                    kisebb_db[i] -= 1
                    osszeg += 1000

            for i in range(len(kisebb_db)):
                if kisebb_db[i] > 0:
                    kisebb_db[i] -= 1
                    osszeg += 900

            for i in range(len(kisebb_db)):
                if kisebb_db[i] > 0:
                    kisebb_db[i] -= 1
                    osszeg += 800

            while kisebb_db != ures:
                for i in range(len(kisebb_db)):
                    if kisebb_db[i] > 0:
                        kisebb_db[i] -= 1
                        osszeg += 800

            print(f"A vásárlás összege: {osszeg} Ft")
    except ValueError:
        print("Nem volt ilyen sorszámmal vásárlás.")

def feladat_4(lst: list):
    keres = input("4. feladat: Adja meg az árucikk nevét: ")
    vane = []
    van = []
    for i in lst:
        vane.append(0)
    for i in lst:
        van.append(i.count(keres))
    print(van)
    sum = 0
    for i in van:
        if i != 0:
            sum += 1


    if sum != 0:
        k = 0
        maxos = 0
        while van[k] == 0:
            k += 1
        print(f"Első vásárlás sorszáma: {k + 1}")
        for i in range(len(van)):
            if van[i] > 0:
                maxos = i
        print(f"Utolsó vásárlás sorszáma: {maxos + 1}")
    else:
        print("Nem vásároltak ebből a termékből.")

def feladat_5(lst: list):

    print("5. feladat: A vásárlások összegének mentése az osszeg.txt fájlba.")