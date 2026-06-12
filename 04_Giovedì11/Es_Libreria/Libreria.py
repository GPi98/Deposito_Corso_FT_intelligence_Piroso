import Libro

class Libreria:
    
    def __init__(self, catalogo = []):
        self.catalogo = catalogo

    def aggiungi_libro(self):
        titolo = ""
        autore = ""
        isbn = ""
        nuovo_libro = []
        
        print("Quanti libri vuoi aggiungere?")
        n = input()
        
        for c in range(n):      #crea delle sotto-liste dentro catalogo(catalogo lista di liste)
            titolo = input("nome titolo: ")
            autore = input("inserire autore: ")
            isbn = input("inserire codice isbn: ")
            nuovo_libro = Libro.Libro(titolo, autore, isbn)
            self.catalogo.append(nuovo_libro)
    
            
    def rimuovi_libro(self):
        isbn = ""
        trovato = False
        
        print ("quanti libri vuoi rimuovere?")
        n = input
        
        for c in range(n):      
            isbn = input("inserire codice isbn: ")
            for libro in self.catalogo: #psosizione 2 della sotto_lista isbn
                if libro[2].lower() == isbn.lower():
                    self.catalogo.remove(libro)
                    print("Il libro con", isbn, " isbn è stato rimosso")
                    trovato = True
                    
            if trovato == False:
                print("Errore l' isbn inserito non presente")

        pass
    def cerca_per_titolo():
        pass
    def mostra_catalogo():
        pass