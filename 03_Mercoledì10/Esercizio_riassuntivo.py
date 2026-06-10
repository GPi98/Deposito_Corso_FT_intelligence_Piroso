"""
LISTA SPESA
dato in input numero prodtti, funzione inserire i prodotti nella lista
funzione rimuovi prodotto, funzione stampa lista
modificare con un generatore?, aggiungengere operazione in corso con un decoratore?
funzione per chiudere
"""
def decoratore(funzione): 
    #aggiunge un print all'inizio e alla fine
    def wrapper(*args, **kwargs):
        print("-----OPERAZIONE-IN-CORSO--------")
        risultato = funzione(*args, **kwargs)
        print("-----OPERAZIONE-TERMINATA--------")
        return risultato
    return wrapper

def decoratore_maiuscolo(funzione):
    def wrapper(*args, **kwargs):
        #chiama la funzione aggiungi_prodotti salva in lista_originale
        lista_originale = funzione(*args, **kwargs)
        
        #chiama prodotti_in_maiuscolo e converte la lista
        lista_convertita = list(prodotti_in_maiuscolo(lista_originale))
        
        # ridà la lista con i caratteri tutti in maiuscolo
        return lista_convertita
    return wrapper

def prodotti_in_maiuscolo(lista):

    for prodotto in lista:
        # yield mette in pausa la funzione e restituisce il valore corrente
        yield prodotto.upper()
        
   
@decoratore
@decoratore_maiuscolo
def aggiungi_prodotti(lista):
    #chiede quanti e quali prodotti vuoi aggiungere 
    print("quanti prodotti vuoi aggiungere?")
    n = int(input())
    
    for i in range(n):
        print("nome prodotto:")
        lista.append(input())
    #potevo fare direttamente .upper()

    return lista

@decoratore
def stampa_lista(lista):
    for l in lista:
        print(l)
        
@decoratore
def rimuovi_prodotti(lista):
    #chiede quanti e quali prodotti vuoi rimuovere
    print("quanti prodotti vuoi rimuovere?")
    n = int(input())
    
    for i in range(n):
        print("quale prodotto vuoi rimuovere?")
        da_rimuovere = input().upper() 
        
        if da_rimuovere in lista:
            lista.remove(da_rimuovere)
            print("Rimosso:", da_rimuovere)
        else:
            print(da_rimuovere, "non è in lista!")
    stampa_lista(lista)        
            
    return lista    

def chiusura(contatore):
    #ritorna False e chiude il contatore
    print("------CHIUSURA--PROGRAMMA-------")
    return False

def menu():   
    lista = []
    contatore = True

    while contatore:
            #menù con match
        print("scegli l'operazione che vuoi fare:")
        print("vuoi aggiungere prodotti alla tua lista, scrivi 1")
        print("vuoi leggere la tua lista della spesa, scrivi 2")
        print("vuoi cancellare un prodotto dalla tua lista della spesa, scrivi 3")
        print("vuoi chiudere il programma, scrivi 0:")
        scelta = input()
            
        match scelta:
                
            case "1":
                    
                lista = aggiungi_prodotti(lista)
                    
            case "2":
                    
                stampa_lista(lista)
                    
            case "3":
                    
                lista = rimuovi_prodotti(lista)
                    
            case "0":
                    
                contatore = chiusura(contatore)
            case _:
                print("ERRORE digitazione")

menu()
