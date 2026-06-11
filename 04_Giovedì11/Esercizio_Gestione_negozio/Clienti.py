"""
1.Gestione Clienti:
I clienti possono visualizzare gli articoli disponibili in inventario.
I clienti possono selezionare e acquistare articoli dall'inventario.
Il sistema tiene traccia degli acquisti dei clienti.    
"""
#registrazione utente insieme ad aggiungi utenti, aggiunto registra utente
class Clienti:
    def __init__(self):
        self.utenti =[]
    def aggiungi_utenti(self):
        n = int(input("quanti oggetti vuoi inserire? :"))
        for i in range(n):
            nome = input("Nome: ")
            eta = input("Età: ")
            email = input("Quantità: ")
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
    
    @staticmethod    
    def login(self, email, password):
        email = input("Inserire email: ")
        password = input("password: ")
        login_effettuato = False
   

        for utente in self.utenti:
                
            if email == utente["Email"] and password == utente["Password"]:
                login_effettuato = True
                print("Login effettuato")
                    
            if not login_effettuato:
                print("Errore hai sbagliato email o password")