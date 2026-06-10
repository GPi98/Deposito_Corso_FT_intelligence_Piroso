class Garage:
    
    def __init__(self, capienza):
        self.capienza = capienza
        self.targhe = []
        
    def ___len__(self):
        return len(self.targhe)

    @staticmethod   
    def formato_targa_valido(targa):
        # Controlliamo prima di tutto che sia lunga esattamente 7 caratteri
        if len(targa) != 7:
            return False
            
        # Spezzettiamo la targa e controlliamo i singoli blocchi
        prime_lettere = targa[0:2].isalpha()  # True se i primi due sono lettere
        numeri_centrali = targa[2:5].isdigit() # True se i tre centrali sono numeri
        ultime_lettere = targa[5:7].isalpha()  # True se gli ultimi due sono lettere
        
        # Se tutte e tre le condizioni sono vere, la targa è valida
        return prime_lettere and numeri_centrali and ultime_lettere

    def posti_liberi(self):                 # ritorna il valore della differenza
        return self.capienza - len(self.targhe)       
    
    def parcheggia(self):
        
        print("Inserire una targa") #blocco codice per input di targa maiuscolo e controllo
        targa = input().upper()
        if Garage.formato_targa_valido(targa):
            print(Garage.formato_targa_valido(targa))
            for t in self.targhe:
                if targa != t:      #controlla se la targa è dentro la lista targhe 
                    if self.posti_liberi() != 0:    #controlla se ci sono posti liberi 
                        self.targhe.append(targa)
                        print("Auto con targa:", targa, " PARCHEGGIATA")
                    else:
                        print("Il parcheggio è pieno")
                else:
                    print("ERRORE targa già presente")
    
    def rimuovi(self):       #
        print("Inserire una targa da rimuovere")
        targa = input()
        if Garage.formato_targa_valido(targa):  #controllo dell'input della targa
            
            for i, t in enumerate(self.targhe):
                if targa == self.targhe[i]:          #controlla se esiste la targa
                    self.targhe.remove(targa)
                    print("targa: ", targa, " rimossa")
                else:
                    print("ERRORE targa non presente")        

    def stampa(self):
        for t in self.targhe:
            print(t)

contatore = True
garage = Garage(15)


while contatore:    
    
    print("Scegli operazioni:")
    scelta = input()
    
    match scelta:
        case "1":
            print("Posti liberi: ", garage.posti_liberi())
        case "2":
            garage.parcheggia()    
        case "3":
            garage.rimuovi()
        case "4":
            garage.stampa()
        case "0":
            contatore = False
        case _:
            print("ERRORE Digitazione")