# #extra farlo lavorare su una lista
# def is_primo(n):
#     if n <= 1:
#         return False
#     elif n == 2:
#         return True
#     elif n % 2 == 0:
#         return False
#     else:
#         # Controlla solo i divisori dispari fino alla radice quadrata di n
#       """  """  for i in range(3, int(n**0.5) + 1, 2):
#             if n % i == 0:
#                 return False
#         return True

# contatore = True

# while contatore:
#     print("Inserisci un numero intero positivo: ")
#     numero = int(input())
    
#     match numero:
#         case 0:
#             print("Errore hai inserito 0 inserire un numero intero positivo")
#         case _ if numero < 0:
#             print("Errore hai inserito 0 inserire un numero intero positivo")
#         case _:
#             somma = 0
#             for i in range(numero+1):
#                 if i % 2 == 0:
#                     somma = somma + i
#             print(somma)
#             for i in range(numero+1):
#                 if i % 2 == 1:
#                     print(i)

#             if is_primo(numero):
#                 print(f"{numero} è un numero primo")
#             else:
#                 print(f"{numero} non è un numero primo")
            
#             contatore = False

#extra farlo lavorare su una lista
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



while True:
    print("Inserisci un numero intero positivo: ")
    numero = int(input())
    
    if numero > 0:
        break           #interrompe il ciclo 
    else:
        print("il numero inserito non è intero e positivo")
    
somma = 0       
for i in range(numero+1):
    if i % 2 == 0:          #controlla il resto nella divisione
        somma = somma + i
print("somma dei numeri pari")
print(somma)
print("numeri dispari fino a: ", numero)
for i in range(numero+1):
    if i % 2 == 1:
        print(i)

if is_primo(numero):
    print(f"{numero} è un numero primo")
else:
    print(f"{numero} non è un numero primo")

                