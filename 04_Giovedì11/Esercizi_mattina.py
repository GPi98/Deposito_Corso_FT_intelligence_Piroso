"""Esercizio 5 (Facile) @staticmethod:
Crea una classe chiamata Convertitore. Questa classe dovrebbe
avere:
Un metodo statico euro_in_dollari che accetti un importo in euro
e restituisca il valore convertito in dollari, usando un tasso
fisso di 1.08.
Un metodo statico km_in_miglia che accetti una distanza in
chilometri e restituisca il valore convertito in miglia, usando
un fattore fisso di 0.621371.
Testa la classe chiamando entrambi i metodi direttamente dalla
classe, senza creare alcun oggetto.
"""

class Convertitore:

    
    def __call__(self, valore, tipo):       #funzione call 
        if tipo == "soldi":         #legge tipo e richiama la funzione necessaria in base al caso
            return Convertitore.euro_in_dollari(valore)
        elif tipo == "distanza":
            return Convertitore.km_in_miglia(valore)
        else:
            print("ERRORE inserimento tipo conversione")
            
    @staticmethod           #metodo statito collegato alla classe ma non all'oggetto
    def euro_in_dollari(euro):  ##prende in input un valore e lo restituisce moltiplicato per 1.08
        return euro * 1.08
    
    @staticmethod           #metodo statito collegato alla classe ma non all'oggetto
    def km_in_miglia(km):   #prende in input un valore e lo restituisce moltiplicato per 0.621371
        return km * 0.621371
    
#test
print("Dollari:", Convertitore.euro_in_dollari(3))
print("Miglia:", Convertitore.km_in_miglia(5))    

c = Convertitore()      #costruiamo un oggetto vuot
print(c(3, "soldi"))    #richiamiamo la funzione call tramite nome oggetto

"""
Esercizio 6 (Facile) @classmethod:
Crea una classe chiamata Animale. Questa classe deve avere:
Un attributo di classe numero_animali, inizializzato a 0.
Due attributi di istanza: nome e specie, passati al costruttore.
Il costruttore deve incrementare numero_animali di 1 ogni volta
che viene creato un nuovo animale.
Un metodo di classe quanti_animali che stampi una stringa del
tipo "Numero di animali creati: 'numero_animali'".
Crea almeno 3 oggetti Animale e poi chiama quanti_animali
direttamente dalla classe, senza usare nessuna delle istanze
create.
"""
class Animale:
    
    numero_animali = 0      #attributo di classe
    
    def __init__(self, nome, specie):       #costruttore
        self.nome = nome
        self.specie = specie
        Animale.numero_animali += 1         #aumento del contatore in base al numero di oggetti
    
    @classmethod
    def numero_animalif(cls):           #metodo di classe con parametro la classe
        print("numero animali:", Animale.numero_animali)    #stampa il l'attributo di classe
        
pecora1 = Animale("pecora1", "pecora")      #serie di creazioni di oggetti Animele
conglio1 = Animale("coniglio1", "coniglio")
maiale1 = Animale("maiale1", "maiale")  

Animale.numero_animalif()       #richiamo la funzione numero_animalif 


"""
Esercizio 7
Obiettivo: Creare una classe Ristorante che permetta di gestire alcune funzionalità di base .
Requisiti:
1.Definizione della Classe:
Creare una classe chiamata Ristorante.
La classe dovrebbe avere un costruttore __init__ che accetta due parametri: nome (nome del
ristorante) e tipo_cucina (tipo di cucina offerta).
Definire un attributo aperto che indica se il ristorante è aperto o chiuso. Questo attributo
deve essere impostato su False di default (cioè, il ristorante è chiuso).
Un Lista o + menu dove dentro ci sono i piatti e prezzi che ha il ristorante        ------
2.Metodi della Classe:
descrivi_ristorante(): Un metodo che stampa una frase descrivendo il ristorante, includendo ----
il nome e il tipo di cucina.
stato_apertura(): Un metodo che stampa se il ristorante è aperto o chiuso.  ---
apri_ristorante(): Un metodo che imposta l'attributo aperto su True e stampa un messaggio ----
che indica che il ristorante è ora aperto.
chiudi_ristorante(): Un metodo che imposta l'attributo aperto su False e stampa un messaggio -----
che indica che il ristorante è ora chiuso.
aggiungi_al_menu(): Un metodo per aggiungere piatti al menu
togli_dal_menu(): Un metodo per togliere piatti al menu
stampa_menu(): Un metodo per stampare il menu
3.Testare la Classe:
Creare un'istanza della classe Ristorante, passando i valori appropriati al costruttore.
Testare tutti i metodi creati per assicurarsi che funzionino come previsto.
Fare 2 o più classi 
"""

class Ristorante:
    
    def __init__(self, nome, tipo_cucina, aperto = False):   #costruttore con nome tipo_c e aperto passati come paametri
        self.nome = nome
        self.tipo_cucina = tipo_cucina      
        self.aperto = aperto
    
    def __repr__(self): #sembra repr chiede descrizione però dubbio se __str__
        return f"Ristorante :('{self.nome}'), tipo cucina: ('{self.tipo_cucina}', aperto: ('{self.aperto}')"

    def stampa_apertura(self):  #controlla aperto se true  stampa è aperto altrimenti è chiuso
        if self.aperto:
            print("il ristorante: ", self.nome," è aperto")
        else:
            print("il ristorante: ", self.nome," è chiuso")

    def apri_ristorante(self):  #controlla se è aperto e in caso lo apre
        if self.aperto:
            print("il ristorante: ", self.nome," è già aperto")
        else:
            self.aperto = True
            print("il ristorante: ", self.nome," è ora aperto")

    def chiudi_ristorante(self):    #controlla se è chiuso e in caso lo chiude
        if self.aperto:
            self.aperto = False
            print("il ristorante: ", self.nome," è ora chiuso")
        else:
            print("il ristorante: ", self.nome," è già chiuso")
class Menu:
    def __init__(self, menu = []):
        self.menu = menu
        
    def aggiungi_al_menu(self):
        n = int(input("quanti piatti vuoi aggiungere: "))
        for i in range(n):
            print("nome del piatto:")
            nome_nuovo = input()
            print("prezzo: ")
            prezzo_nuovo = float(input())
            nuovo_piatto = [nome_nuovo, prezzo_nuovo]
            self.menu.append(nuovo_piatto)
            
    def rimuovi_dal_menu(self):
        piatto_da_rimuovere = input("Quale piatto vuoi rimuovere dal menu? ")
        
        trovato = False
        # Cerchiamo la sotto-lista 
        for piatto in self.menu:
            # piatto[0] è il nome del piatto [nome_piatto, prezzo]
            if piatto[0].lower() == piatto_da_rimuovere.lower(): #formatta il nome del piatto nel menu e quello da rimuovere in minuscolo
                self.menu.remove(piatto)
                print(piatto_da_rimuovere, " è stato rimosso con successo!")
                trovato = True
                break # usciamo dal ciclo appena lo troviamo
        if not trovato:     #controlla se non è stato trovato nel menu
            print(piatto_da_rimuovere ," non è stato trovato nel menu.")
    
    def stampa_dal_menu(self):
        print("--- MENU ATTUALE ---")
            # Se il menu è vuoto, avvisiamo l'utente
        if not self.menu:
            print("Il menu è vuoto!")
        else:
            # Cicliamo nella lista di liste spacchettando nome e prezzo
            for piatto in self.menu:
                nome = piatto[0]
                prezzo = piatto[1]
                print(nome, ": €", prezzo)
    
    class Chef: 
               
        def __init__(self, nome:str , ristorante = ""):
            self.nome = nome
            self.ristorante = ristorante
        
        def stampa_chef(self):
            print("nome chef:", self.nome)
            if self.ristorante != "":
                print("lavora nel ristorante:", self.ristorante)
        
        def cambio_ristorante(self, nuovo_r):
            self.ristorante = nuovo_r
            
            

r = Ristorante("prova", "provola")  
menu_1 = Menu()  
#chef_1 = Chef("Gino", "r")  non gli piace NameError: name 'Chef' is not defined
#print(r.nome, r.tipo_cucina, r.aperto)
#print(repr(r))
r.apri_ristorante()
r.stampa_apertura()
r.chiudi_ristorante()
r.stampa_apertura()
menu_1.aggiungi_al_menu() 
menu_1.stampa_dal_menu()
menu_1.rimuovi_dal_menu()
menu_1.stampa_dal_menu()


