class Punto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def modifica_punto(self, n_x, n_y):
        self.x = n_x
        self.y = n_y
        
    def distanza_da_origine(self):
        
        distanza_x =  self.x
        distanza_y =  self.y
        
        return distanza_x, distanza_y
    

    
punto1 = Punto(1,2)         #creazione oggetto

print(punto1.distanza_da_origine())

class Libro:
    
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    
    def descrizione(self):
        return "Il libro ", self.titolo," è stato scritto da", self.autore," e ha ", self.pagine, "pagine"
        
    
libro1 = Libro("Il Signore degli Anell", "J. R. R. Tolkien", 1380)
print(libro1.descrizione())

libro_l = []

print("quanti libri vuoi inserire:")
numeri = int(input())
for i in range(numeri):
    titolo = input("Titolo: ")
    autore = input("Autore: ")
    pagine = input("Numero pagine:")
    l = Libro(titolo, autore, pagine)
    libro_l.append(l)
for i in range(numeri):
    print(libro_l[i].descrizione())
#for l in lista_l:          consigliata dal prof
#l.descrizione   
    
    