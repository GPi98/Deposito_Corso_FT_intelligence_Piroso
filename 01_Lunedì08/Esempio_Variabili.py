nome = "Alice"
eta = 25
#funzione integrata per stampare
print("il mio nome è:", nome, "e ho ", eta, "anni")

#funzione integrata input
nome = input("Inserisci il tuo nome: ")
#con int abbiamo castatato(convertito) la stringa in ingresso in un intero
eta = int( input("Inserisci la tua età: "))
print("Ciao "+ nome + "! Benvenuto in Python!") 
# + solo tra stringhe, se mettiamo un numero non va, (deve sommare)

#usare la variabile invece di mettere gli spazi nelle stringhe in print
spazio = " "
print("Ciao"+ spazio + nome +"! Benvenuto in Python!") 

print(1 + 2)
print(10 - 5)

print(1 + 5) #somma
print(6 - 5) #sottrazione
print(3 * 2) #moltiplicazione
print(4 / 2) #divisione
print(3 ** 2) #potenza

x = 10  #es variabile valore int
x = -5  #es variabile valore int
x = 3.14    #es variabile valore float
b = - 1.0   #es variabile valore float
nome = "Alice"  #"" o '' meglio il primo es variabile valore stringa
msg = "Ciao!"   #es valore str

s = "Python"
print(s[0]) #scrive P
print(s[1]) #scrive y

saluto = "Ciao"
nome = "Alice"
messaggio = saluto + " " + nome
print(messaggio) #Output 'Ciao Alice'

s = "Ciao, Mondo!"
print(len(s)) #funzione intrinseca da lunghezza stringa Output: 12
print(s.upper()) #Output: 'CIAO, MONDO!'
print(s.split(',')) #Output: '[CIAO]', '[MONDO!]'
print(s.replace('mondo', 'universo')) #Output: 'Ciao, Universo!'

booleano = True #rappresenta un booleano con valore false diverso da 0
booleano = False #rappresenta un booleano con valore false

x = 5
y = 10
print( x == y ) #Output: False condizione uguale
print( x != y ) #Outpu: True    condizione diverso
print( x < y )  #Output: True   condizione minore

x = 5
y = 10
z =7
print(x < y and y > z)  #Output: True   se prima_condizione e seconda_cond sono vere True
print(x < y or z > y)   #Output: True   se prima_condizione o seconda_cond sono vere True
print(not(x < y))   #Output: False  restituisce l'opposto della condizione

numeri = [1, 2, 3, 4, 5]    
nomi = ["Alice", "Bob", "Charlie"]
misto = [1, "due", True, 4.5] #lista eterogenea (di diversi tipi di dato)

numeri = [3, 1, 4, 2, 5]

print(numeri[0]) #Output: 3  da in output lista numeri il primo valore
print(numeri[2]) #Output: 4 da in output lista numeri il terzo valore
print(len(numeri))  #lunghezza Output: 5
numeri.append(6)    #aggiunge un valore 
print(numeri)   #Output:[3, 1, 4, 2, 5, 6]
numeri.insert(2,10) #aggiunge il numero 10 alla posizione 2(parte da 0)
print(numeri)   #Output:[3, 1, 10, 4, 2, 5, 6]
numeri.remove(4) #rimuove il valore 4 
print(numeri)   #Output:[3, 1, 10, 2, 5, 6]
numeri.sort() #ordina la lista 
print(numeri)   #Output:[ 1, 2, 3, 5, 6, 10]

punto = (3, 4) #esempi dichiarazioni tuple
colore_rgb = (255, 128, 0)
informazioni_personali = ("Alice", 25, "Femmina")
punto = 3, 4    #tuple unpacking dichiarare senza parentesi
x, y = punto    #tuple unpackind dichiarare x e y spacchettando la tupla


print(punto[0]) #output della tupla quando si dichiara con le parentesi [] anche
print(punto[1]) # se quando si definisce si usano le ()
print(x, y) #print dell'unpacking
