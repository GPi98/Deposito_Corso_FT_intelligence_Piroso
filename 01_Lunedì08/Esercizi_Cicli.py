import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limite = int(math.sqrt(n)) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
    return True

#parte iniziale dove importa math e definisce la funzione is_prime per il secondo es.
#sembrerebbe non contare 1 come numero primo

#ESERCIZIO 1
num = int(input("Inserire un numero"))
controllore = True      # valore bool per continuare il ciclo

while controllore:      #ciclo booleano, continua finchè true

    print(num)
    num -= 1 

    if num <= 0:        #condizione per farlo fermare a 0
        controllore = False    
        
    scelta = input("vuoi continuare?")
    if scelta == "no":      #controlla la scelta data in input
        controllore = False #cambia il valore di controllo e termina il ciclo
        
        
#ESERCIZIO 2
contatore = 0

while contatore <= 4:   #controlla se i numeri primi sono 5
    num = int(input("Inserire un numero da controllare se primo"))
    if is_prime(num):           #controlla se primo
        print("Il numero è primo")
        contatore +=1           #aggiorna il contatore dei numeri primi
    else:
        print("Il numero non è primo")

