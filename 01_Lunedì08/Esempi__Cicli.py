conteggio = 0

while conteggio < 5:    #condizione del ciclo
    print("conteggio")
    conteggio += 1      #incremento del contatore
    
controllore = True      # valore bool per continuare il ciclo

while controllore:      #ciclo booleano, continua finchè true
    print("ciao")

    scelta = input("vuoi continuare?")
    if scelta == "no":      #controlla la scelta data in input
        controllore = False #cambia il valore di controllo e termina il ciclo
        
numeri = [1, 2, 3, 4, 5]

for numero in numeri:
    print(numero)

for i in range(5):  #arriva al numero-1 passato in parametro
    print(i)
    
for i in range(2, 5):   #parametro start parte da 2 
    print(i)
    
for i in range(1, 10, 2):   #parte da 1(start) 10(stop) aumenta di 2(step)
    print(i)