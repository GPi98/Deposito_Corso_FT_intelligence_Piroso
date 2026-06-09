#fare un ciclo per far riscegliere 1-2-3
#3 fare un ciclo per riempiere la lista in input

contatore = True

while contatore:
    scelta = int(input("Quale esercizio fare 1 (pari o dispari), 2 (contatore), 3(lista): "))
    
    match scelta:
        case 1:
            numero = int(input("scrivi un numero e ti dirò se pari o dispari: "))
            if numero % 2 == 0:
                print("Il numero inserito è pari.")
            else:
                print("Il numero inserito è dispari.")
            si_no = input("Vuoi uscire? : ")
            if si_no == "si":
                contatore = False
        case 2:
            contatore_int = True
            numero= int(input("Inserisci un numero intero positivo: "))
            while contatore_int:
                
                if numero > 0:
                    for i in range(numero, 0, -1):
                        print(i)
                    contatore_int = False
                else:
                    print("Errore: il numero deve essere positivo.")

                si_no = input("Vuoi uscire? : ")
                if si_no == "si":
                    contatore = False
        case 3:
            n = int(input("Quanti elementi vuoi inserire? "))
            lista = []

            for i in range(n):
                numero = int(input("Inserisci elemento: "))
                lista.append(numero)
            for numero in lista:
                quadrati = lista[n]**2
            print(quadrati)

            si_no = input("Vuoi uscire? : ")
            if si_no == "si":
                contatore = False
        case _:
            print("Errore nella scelta")
            si_no = input("Vuoi uscire? : ")
            if si_no == "si":
                contatore = False
                
