#generatori
def fibonacci(n):       #funzione presa dalle slide
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
        
coll = [*fibonacci(100)] 
coll2 = list(fibonacci(100))
coll3 = []

for numero in fibonacci(100): 
    print(numero)
    coll3.append(numero)
  
print(coll) 
#decoratori

def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione della funzione")
        funzione()
        print("Dopo l'esecuzione della funzione")
    return wrapper

@decoratore
def saluta():
    print("Ciao!")
        
saluta()        

def decoratore_con_argomenti(funzione):
    def wrapper(*args, **kwargs):
        print("Prima")
        risultato = funzione(*args, **kwargs)
        print("Dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma(a, b):
    print(a+b)
    return a + b

print("risultato è ", somma(3, 4))

import time

def calcola_tempo(funzione):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        risultato = funzione(*args, **kwargs)
        end_time = time.time()
        print(f"Tempo di esecuzione:{end_time - start_time} secondi")
        return risultato
    return wrapper

@calcola_tempo
def calcolo_lento():
    time.sleep(2)
    print("Calcolo completato")
    
#chiamata alla funzione decorata
calcolo_lento()

