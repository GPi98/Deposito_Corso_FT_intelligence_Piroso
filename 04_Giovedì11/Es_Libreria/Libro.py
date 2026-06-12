class Libro:
    
    lista_isbn = []
    
    def __init__(self, titolo, autore, isbn):
        if Libro.check_isbn(isbn) == True:
            self.isbn = isbn
            self.titolo = titolo
            self.autore = autore
            Libro.lista_isbn.append(isbn)
        else:
            print("isbn: ", isbn," già presente")
    
    def __str__(self):
        return  f"Titolo :('{self.titolo}'), Autore: ('{self.autore}', isbn: ('{self.isbn}')"   
          
    @classmethod
    def check_isbn(cls, isbn):
    
        for i in Libro.lista_isbn:
            if i == isbn:
                return True
        return False     

#test
lib = Libro("Titolo","Autore","1342342")
#l1 = Libro("B", "B", "1")         
print(lib)            
        
        