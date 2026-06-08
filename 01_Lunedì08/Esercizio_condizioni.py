#PRIMO ESERCIZIO

livello = 4         #definisce a quale livello sei arrivato

if livello > 1:
    print("Hai superato il 1 livello ")
    if livello > 2:
        print("Hai superato il 2 livello ")
        if livello > 3:
            print("Hai superato il 3 livello ") #esce qui perchè mag di 3 e min 5
            if livello > 4:
                print("Hai superato il 4 livello ")

#SECONDO ESERCIZIO

lista_caso = ["Rosso", 4, 7.32, True, "Verde"]
scelta = int(input("1 = aggiungi in fondo il numero 3, 2 rimuovi il numero 4, 3 aggiunge True nel 3 posto: "))
#variabile per scegliere che crud fare

if scelta == 1:
    lista_caso.append(3)    #aggiunge 3 alla fine della lista
    print("aggiunto 3")
    print(lista_caso)
elif scelta == 2:
    lista_caso.remove(4)    #rimuove il valore 4 dalla lista
    print("rimosso 4")  
    print(lista_caso)
elif scelta == 3:
    lista_caso.insert(2,True)       #aggiunge alla 3 posizione il valore True
    print("aggiunto True alla 3 posizione")
    print(lista_caso)
else:
    print("ERRRORE NON HAI DIGITATO 1 O 2 O 3")
    
#TERZO ESERCIZIO

utenti = 1  #numero utenti nel sistema
utente_sys = [1, 2 , 3, 4]  #definisco la lista o da errore
#utente_sys = ["default", "password", 1, 1] #test secondo if

if utenti == 0:     
    print("creo un account standard")   
    utente_sys = ["default", "password", 1, 1]
else:
    print("esiste uno o più utenti")
    if utente_sys[3] == 1:
        print("account predefinito con id 1 già inserito")



    

    


                