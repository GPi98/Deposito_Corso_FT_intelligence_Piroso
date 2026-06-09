import random

def r_input():  #gestisce l'input
    while True:
            print("Inserisci il tuo tentativo se vuoi uscire scrivi 0: ")
            scelta = int(input())
            
            if scelta == 0 :   # Se l'utente vuole uscire, restituiamo 0
                return int(scelta)
            
            # Controllo del numero
            if  1 <= scelta <= 100:
                return int(scelta)
            else:
                print("ERRORE Inserisci un numero tra 1 e 100 o 0 per uscire.") 
            
            
               
def gioco():
    print("Indovina un numero tra 1 e 100")
    
    numero_casuale = random.randint(1, 100) #genera il numero casuale
    n_tentativi = 0   
    
    while True:
        tentativo = r_input()
        
        if tentativo == 0:
            break
    
        n_tentativi = n_tentativi + 1    #aumentiamo il contatore    
    
        if tentativo == numero_casuale:     #check numero e tentativo
            print("Hai indovinato il numero: ", numero_casuale)
            print(" hai impiegato:", n_tentativi," tentativi.")
            break
            
        elif tentativo < numero_casuale:
            print("Riprova Il numero è più alto")
        else:
            print("Riprova Il numero è più basso")
            
gioco()