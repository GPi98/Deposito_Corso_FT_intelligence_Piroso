"""
1.Gestione Clienti:
I clienti possono visualizzare gli articoli disponibili in inventario.
I clienti possono selezionare e acquistare articoli dall'inventario.
Il sistema tiene traccia degli acquisti dei clienti.    
"""
#registrazione utente insieme ad aggiungi utenti, aggiunto registra utente
import Prodotto

class Clienti:
    def __init__(self):
        self.utenti =[]
        
    def aggiungi_utenti(self):
        n = int(input("quanti utenti vuoi inserire? :"))
        for i in range(n):
            nome = input("Nome: ")
            eta = input("Età: ")
            email = input("Email: ")
            password = input("Password: ")
            nuovo_utente = {"Nome": nome, "Eta": eta, "Email": email, "Password": password}
            self.utenti.append(nuovo_utente)        

    def registra_utente(self):
#tecnicamente aggiungi utenti è sbagliato, ma può servire allo staff, registra utente così ha più senso 
            nome = input("Nome: ")
            eta = input("Età: ")
            email = input("Quantità: ")
            password = input("Password: ")
            nuovo_utente = {"Nome": nome, "Eta": eta, "Email": email, "Password": password}
            self.utenti.append(nuovo_utente)    
    
    
    def login_u(self): # restituisce true se riesce a fare il login false il contrario
        email = input("Inserire email: ")
        password = input("password: ")
        login_effettuato = False
   

        for utente in self.utenti:
                
            if email == utente["Email"] and password == utente["Password"]:
                login_effettuato = True
                print("Login effettuato")
                return True    
            if not login_effettuato:
                print("Errore hai sbagliato email o password")
                return False
            
    def logout_u(self): # restituisce true se riesce a fare il login false il contrario

        print("Logout effettuato")
    
    def acquisto(self, prodotti): 
        Prodotto.prodotti.stampa_prodotti()
        print("Quanti prodotti vuoi acquistare:")
        nu = int(input())
        

        if nu > 0:
            for n in range(nu):
                p_acquisto = input("nome prodotto: ")
                if Prodotto.prodotti.check(p_acquisto) == True:
                    Prodotto.prodotti.guadagni(p_acquisto)
                else:
                    print("ERRORE prodotto inserito non presente")
                    break
        

           

        


        