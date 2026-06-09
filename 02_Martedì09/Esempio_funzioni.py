#def nome_funzione(parametri):	#definizione
#blocco di codice

#nome_funzione(argomenti)  	#richiamo

def saluta(nome):   #passa nome
    print("Ciao,", nome)

def somma(a, b):    #passa a e b 
    risultato = a + b   #possiamo avere anche variabili non passate
    print("La somma è :", risultato)
 
def saluta2(nome:str, messaggio="Ciao"):    #passa nome controlla che sia str e messaggio da un default
    print(f"{messaggio} {nome}!")   #meglio non usare questo modo

def quadrato(numero):
    return numero * numero  #generalmente implicito null può esserci o no
    
saluta("Alice")
somma(5, 3)
saluta2("Mario")
saluta2("Luigi", messaggio="Buongiorno")
risultato = quadrato(4)
print("quadrato di 4 =", risultato)
