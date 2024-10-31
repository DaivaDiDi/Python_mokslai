# with open("Saskaitos_apyvarta.pkl", 'wb') as failas:
#     pass
############
import pickle

while True:
    veiksmas = int(input("Pasirinkite: 1 - peržiūrėti t.t. ir balansas, 2 - įrašyti, 3 - išeiti : "))
    if veiksmas == 1:
        try:
            with open("../Saskaitos_apyvarta.pkl", 'rb') as failas:
                saskaita = pickle.load(failas)
                balansas = 0
            for eilute in saskaita:
                balansas += float(eilute)
            print(f" Suvestos sumos : {saskaita} ")
            print(f' -----------------\nĮvestas sąskaitos balansas:  {round(balansas, 1)}')
        except:
            print("Nėra jokių duomenų")
    if veiksmas == 2:
        try:
            with open("../Saskaitos_apyvarta.pkl", 'rb') as failas:
                saskaita = pickle.load(failas)
                print(f" Suvestos sumos : {saskaita}")
                while True:
                    try:
                        suma = input("Įveskite sumą : ")
                        if suma == "":
                            break
                        else:
                            saskaita.append(suma)
                            with open("../Saskaitos_apyvarta.pkl", 'wb') as failas:
                                pickle.dump(saskaita, failas)
                    except  ValueError:
                        break
        except:
            saskaita = []
            print(
                "Pradedamas sąskaitos Pajamų ir Išlaidų suvedimas \n"
                "INCTUKCIJA: Pajamas su ženklu ""+"" arba be jo. Išlaidas su ženklu ""-"" \n"
                "!!! Procesą nutraukti suveskit Enter ")
            while True:
                try:
                    suma = input("Įveskite sumą : ")
                except  ValueError:
                    break
                if suma == "":
                    break
                else:
                    saskaita.append(suma)
                    with open("../Saskaitos_apyvarta.pkl", 'wb') as failas:
                        pickle.dump(saskaita, failas)
    if veiksmas == 3:
        print("Viso gero")
        try:
            with open("../Saskaitos_apyvarta.pkl", 'rb') as failas:
                saskaita = pickle.load(failas)
                balansas = 0
            for eilute in saskaita:
                balansas += float(eilute)
            print(f' -----------------\nĮvestas sąskaitos balansas:  {round(balansas, 1)}')
        except:
            print("Nėra jokių duomenų")
        break
