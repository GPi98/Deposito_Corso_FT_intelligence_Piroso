"""Gestione dell'Inventario:
Gli articoli in magazzino sono elencati con il nome, il prezzo e la quantità.
È possibile aggiungere nuovi articoli all'inventario.
Gli articoli possono essere rimossi o aggiornati (ad es., cambiare prezzo o
quantità)."""

class Prodotti:
    
    guadagni_totali = 0
    
    def __init__(self):
        self.prodotti = []
        
    def aggiungi_prodotti(self):
        n = int(input("quanti oggetti vuoi inserire? :"))
        for i in range(n):
            nome = input("Nome:")
            prezzo = float(input("Prezzo:"))
            quantita = int(input("Quantità:"))
            nuovo_prodotto = {"Nome": nome, "Prezzo": prezzo, "Quantità": quantita }
            self.prodotti.append(nuovo_prodotto)
    
    def stampa_prodotti(self):  
        for p in self.prodotti:
            print(p)  
    
    def cambio_prezzo(self):
        prod = input("Inserire prodotto a cui cambiare il prezzo: ")
        prezzo_n = float(input("Inserire prezzo: "))
        prodotto_trovato = False
        
        for prodotto in self.prodotti:
            
            if prod == prodotto["Nome"]:
                prodotto["Prezzo"] = prezzo_n 
                print("Prezzo aggiornato con successo!")
                prodotto_trovato = True
                break # usciamo dal ciclo perché l'abbiamo trovato                
        if not prodotto_trovato:
            print("ERRORE, il prodotto non è presente")
          
    def cambio_quantita(self):
        prod = input("Inserire prodotto a cui cambiare la quantita: ")
        quantita_n = int(input("Inserire quantita: "))
        prodotto_trovato = False
        
        for prodotto in self.prodotti:
            
            if prod == prodotto["Nome"]:
                prodotto["Quantita"] = quantita_n 
                print("Quantita aggiornato con successo!")
                prodotto_trovato = True
                break # usciamo dal ciclo perché l'abbiamo trovato                
        if not prodotto_trovato:
            print("ERRORE, il prodotto non è presente")
            
    def rimuovi(self):
        prod = input("Inserire prodotto da rimuovere: ")
        prodotto_trovato = False
        
        for prodotto in self.prodotti:
            
            if prod == prodotto["Nome"]:
                self.prodotti.remove(prodotto)
                print("Prodotto rimosso con successo!")
                prodotto_trovato = True
                break # usciamo dal ciclo perché l'abbiamo trovato                
        if not prodotto_trovato:
            print("ERRORE, il prodotto non è presente")  

    def check(self, prod):    #controlla se esiste prod in nome prodotto ritorna True o Flse
        prodotto_trovato = False
        
        for prodotto in self.prodotti:
            
            if prod == prodotto["Nome"]:
                prodotto_trovato = True
                return True
                break # usciamo dal ciclo perché l'abbiamo trovato                
        if not prodotto_trovato:
            print("ERRORE, il prodotto non è presente")
            return False 
              
    @classmethod
    def guadagni(cls, prodotti, prod):   #aggiunge i soldi nel'attributo classe
        
        for prodotto in prodotti:
            
            if prod == prodotto["Nome"]:
                cls.guadagni_totali += prodotto["Prezzo"]

        
    @classmethod
    def stampa_guadagni(cls):
        print("guadagni totali: ",cls.guadagni_totali)
        
    def __str__(self):
        return  f"Nome :('{self.prodotti["Nome"]}'), prezzo: ('{self.prodotti["Prezzo"]}', quantita: ('{self.prodotti["Quantita"]}')" 
    
#negozio = Prodotti()
#negozio.aggiungi_prodotti()
#negozio.stampa_prodotti()
#negozio.cambio_prezzo()
#negozio.cambio_quantita()
#negozio.stampa_prodotti()
#negozio.rimuovi() 
    
    
    