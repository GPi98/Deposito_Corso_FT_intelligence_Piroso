class Automobile:                   #dichiaro la classe
    
    numero_ruote = 4                #attributo di classe
    
    def __init__(self, marca, modello):     #metodo costruttore
        
        self.marca = marca                  #attributo di istanza
        
        self.modello = modello              #attributo di istanza
        
    def stampa_info(self):                  #metodo di istanza
        
        print("l'automobile è una ", self.marca, self.modello )

auto1 = Automobile("Fiat", "500")       #crea un oggetto di Automobile
auto2 = Automobile("BMW", "X3")

auto1.stampa_info()                     #stampa L'Automobile è una Fiat 500
auto2.stampa_info()                     #stampa L'Automobile è una BMW X3

class Persona:
    def __init__(self, nome, eta):
        self.nome = nome                #attributo di istanza
        self.eta = eta
#creazione di p tipo Persona        
p = Persona("Pippo",   30)

print(p.nome)       #scrive Pippo
print(p.eta)        #Scrive 30

class Calcolatrice:
    
    @staticmethod
    def somma(a,b):
        return a + b
    
#uso del metodo statico senza creare istanza
risultato = Calcolatrice.somma(5, 3)

print(risultato)
#output 8

class Contatore:
    numero_istanze = 0  #attributo di classe
    
    def __init__(self):
        Contatore.numero_istanza += 1
    
    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")
#creazioni di alcune istanze        
c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanze()
#Sono state create 2 istanze

