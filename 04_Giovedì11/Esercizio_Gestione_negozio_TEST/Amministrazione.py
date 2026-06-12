"""  Amministrazione:
Gli amministratori possono visualizzare un rapporto delle vendite.
Gli amministratori possono visualizzare lo stato corrente dell'inventario.
Il sistema tiene traccia dei guadagni totali."""

#registrazione utente insieme ad aggiungi utenti, aggiunto registra utente
import Prodotto

class Amministratori:
    def __init__(self):
        self.amministratori =[]
        
    def aggiungi_amministratori(self):
        n = int(input("quanti amministratori vuoi inserire? :"))
        for i in range(n):
            nome = input("Nome: ")
            eta = input("Età: ")
            email = input("Quantità: ")
            password = input("Password: ")
            nuovo_utente = {"Nome": nome, "Eta": eta, "Email": email, "Password": password}
            self.amministratori.append(nuovo_utente)        

    def registra_amministratore(self):
#tecnicamente aggiungi amministratori è sbagliato, ma può servire allo staff, registra amministratore così ha più senso 
            nome = input("Nome: ")
            eta = input("Età: ")
            email = input("Quantità: ")
            password = input("Password: ")
            nuovo_utente = {"Nome": nome, "Eta": eta, "Email": email, "Password": password}
            self.amministratori.append(nuovo_utente)    
    
    
    def login_a(self, email, password): # restituisce true se riesce a fare il login false il contrario
        email = input("Inserire email: ")
        password = input("password: ")
        login_effettuato = False
   

        for amministratore in self.amministratori:
                
            if email == amministratore["Email"] and password == amministratore["Password"]:
                login_effettuato = True
                print("Login effettuato")
                return True    
            if not login_effettuato:
                print("Errore hai sbagliato email o password")
                return False
            
    def logout_a(self, login): # restituisce true se riesce a fare il login false il contrario

        print("Logout effettuato")  
        
    def stampa_guadagni_a():
        Prodotto.stampa_guadagni()          