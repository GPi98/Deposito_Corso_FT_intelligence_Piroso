#ESERCIZIO 1

eta = int(input("Inserisci la tua età: "))      

match eta:                          #controlla l'età inserita se >= 18 o se < 18
    case _ if eta >= 18:                          
        print("Puoi vedere il film")
    case _ if eta < 18:                        
        print("Non puoi vedere il film")
    case _:                             
        print("Età non riconosciuta")
        
        
        
#ESERCIZIO 2

numero1 = int(input("Inserisci il primo numero : "))
comando = input("Inserisci un comando + - / *: ")
numero2 = int(input("Inserisci il secondo numero : "))


match comando:                      #controlla l'operatore algebrico + - * /
    case "+":                                             
        print(numero1 + numero2)
    case "-":                        
        print(numero1 - numero2)
    case "*":                       
        print(numero1 * numero2)
    case "/": 
        if numero2 !=0:         #controlla se il numero per cui si divide è 0
            print(numero1 / numero2)
        else:
            print("ERRORE: Divisione per zero")
    case _:                              
        print("Operazione non valida")