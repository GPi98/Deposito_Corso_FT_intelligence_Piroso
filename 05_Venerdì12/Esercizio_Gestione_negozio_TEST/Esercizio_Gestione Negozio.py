"""Esercizio: Sistema di Gestione Negozio
Lo scopo di questo esercizio è implementare un sistema di gestione per un negozio che deve
interagire con clienti, gestire l'inventario e permettere agli amministratori di
supervisionare le operazioni. Il sistema sarà strutturato in tre parti principali:
1.Gestione Clienti:
I clienti possono visualizzare gli articoli disponibili in inventario.
I clienti possono selezionare e acquistare articoli dall'inventario.
Il sistema tiene traccia degli acquisti dei clienti.
2.Gestione dell'Inventario:
Gli articoli in magazzino sono elencati con il nome, il prezzo e la quantità.
È possibile aggiungere nuovi articoli all'inventario.
Gli articoli possono essere rimossi o aggiornati (ad es., cambiare prezzo o
quantità).
3.Amministrazione:
Gli amministratori possono visualizzare un rapporto delle vendite.
Gli amministratori possono visualizzare lo stato corrente dell'inventario.
Il sistema tiene traccia dei guadagni totali.
Puoi pre inserire gli amministratori non i clienti
Il sistema dovrebbe permettere di simulare un'interazione base tra il cliente e il negozio
dopo un login e una registrazione, nonché fornire gli strumenti necessari per la
manutenzione e l'analisi del negozio da parte degli amministratori."""
#extra il moio extra è se finisco faccio la classe staff per lo staff inventario con metoti di Prodoto tranne stampa_guadagni
# ma spero di finire quello normale
#moduli gesione clienti, gestione inventario, amministazione, questo
#Prodotto modulo a parte senza import 
#Cliente modulo a parte  import Prodotto
#Amministrazione modulo a parte  import Prodotto
#

import Prodotto
import Cliente
import Amministrazione


inventario = Prodotto.Prodotti()
inventario.aggiungi_prodotti()
clienti = Cliente.Clienti()
clienti.aggiungi_utenti()
amministratori = Amministrazione.Amministratori()
amministratori.aggiungi_amministratori()

cosa_sei = input("scrivi cosa sei, cliente o amministratore: ").lower()

contatore = False

match cosa_sei:
    case "cliente":
        if clienti.login_u() == True:
            contatore = True
            
            while contatore:
                scelta = input("cosa desideri effettuare vuoi acquistare? 1 vuoi fare il logout? 0")
                match scelta:
                    case "1":
                        clienti.acquisto()                        
                    case "0":
                        clienti.logout_u()
                        contatore = False
                    case _:
                        print("ERRORE DIGITAZIONE")

    case "amministratore":
        if amministratori.login_a() == True:
            contatore = True
            
            while contatore:
                scelta = input("cosa desideri effettuare vuoi stampare guadagni? 1 vuoi fare il logout? 0")
                match scelta:
                    case "1":
                        amministratori.stampa_guadagni_a()   
                    case "2":
                        inventario.cambio_prezzo()
                    case "3":
                        inventario.cambio_quantita()   
                    case "4":
                        inventario.rimuovi()                        
                    case "0":
                        amministratori.logout_a()
                        contatore = False
                    case _:
                        print("ERRORE DIGITAZIONE")        
         
    case "staff inventario":
            contatore = True
            
            while contatore:
                scelta = input("cosa desideri effettuare vuoi stampare guadagni? 1 vuoi fare il logout? 0")
                match scelta:
                    case "1":
                        inventario.stampa_guadagni()
                    case "2":
                        inventario.cambio_prezzo()
                    case "3":
                        inventario.cambio_quantita()   
                    case "4":
                        inventario.rimuovi()                     
                    case "0":
                        contatore = False
                    case _:
                        print("ERRORE DIGITAZIONE")           
           
    case _:
        print("ERRORE Insrimento")