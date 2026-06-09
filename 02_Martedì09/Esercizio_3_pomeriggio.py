import random

def ins_controllo():
    while True:
        print("Inserire un numero intero positivo:")
        n = int(input())
        
        if n > 0:
            return n
        else:
            print("ERRORE nell'inserimento")
            
def gen_c (n):       
    a = 0
    while a < n:
        yield random.randint(1, n)
        a = a + 1      

def somma_numeri_pari(lista_da_controllare):
    somma_p = 0
    
    # Usiamo len() per sapere quanti elementi ci sono nella lista senza scriverlo a mano
    n = len(lista_da_controllare) 
    
    for i in range(n):
        if (lista_da_controllare[i] % 2) == 0:
            somma_p = somma_p + lista_da_controllare[i]
            
    # restituisce la somma
    return somma_p

def numeri_dispari(lista_n):

    lista_dispari = []  # La lista in cui salveremo i numeri dispari
    
    for nu in lista_n:
        # controlliamo sia dispari
        if nu % 2 != 0:  
            lista_dispari.append(nu)  
            
    return lista_dispari  # Restituiamo la lista

def is_primo(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        # Controlla solo i divisori dispari fino alla radice quadrata di n
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

def lista_primi(lista_c):
    primi_trovati = []
    
    for numero in lista_c:
        if is_primo(numero):       # Usa la tua funzione per controllare il numero
            primi_trovati.append(numero)  # Se è vero, lo salva nella nuova lista
            
    return primi_trovati

def somma(lista_c):
    somma = 0
    
    for numero in lista_c:
        somma = somma + numero
        
    return somma


lista_c = []
lista_d = []
lista_p = []
s = 0
while True:
    print("Che operazioni vuoi effettuare: 0(per uscire) 1(somma numeri pari), 2(numer dispari), 3(è primo), 4(lista primi):")
    scelta = int(input())
    if scelta == 0:
        break
        
    n = ins_controllo()

    lista_c = list(gen_c(n))
            
    if scelta == 1:
        somma_p = somma_numeri_pari(lista_c)
        print("la somma è: ", somma_p)
        
    elif scelta== 2:
        lista_d = numeri_dispari(lista_c)
        print("i numeri dispari sono:", lista_d)   
         
    elif scelta == 3:
        print(n, " è o non è un numero primo")
        print(is_primo(n))
        
    elif scelta== 4:
        lista_p = lista_primi(lista_c)
        print(lista_p) 
          
    else:
        print("ERRORE NELLA SCELTA")
        
    s = somma(lista_c)    
    if is_primo(s) == True:
        print("la somma della lista è un numero primo:", s)
    else:
        print("La somma della lista non è un numero primo:", s)
    