numero = 10

if numero > 0:  #se vero esegue il codice successivo
    print("Il numero è positivo")

if (numero == 10): #() non necessarie meglio non usarle
    print("Sono Vero")
    
if numero != 10: #() non necessarie meglio non usarle
    print("Sono Falso")

numero = -3

if numero > 0:                      
    print("Il numero è positivo")
else:                               #altrimenti
    print("il numero è negativo")
    
numero = -3

if numero > 0:                      
    print("Il numero è positivo")
    if numero == 100:       #if annidato
        print("wow")
elif numero < 0:             #aggiunge un altro possibile blocco di codice
    print("il numero è negativo")
else:                               #altrimenti
    print("il numero è zero")
    
    
comando = input("Inserisci un comando: ")

match comando:                             # variabile da controllare
    case "start":                          #condizione comando == "start"
        print("Avvio del programma")
    case "stop":                        #condizione comando == "stop"
        print("Chiusura del programma")
    case "pause":                       #condizione comando == "pause"
        print("Programma in pausa")
    case _:                             #default 
        print("Comando non riconosciuto")