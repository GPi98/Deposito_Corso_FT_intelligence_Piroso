"""Esercizio 4 (Difficile):
Crea una classe chiamata Garage. Questa classe dovrebbe avere:
Un attributo di istanza capienza (numero massimo di auto)
passato al costruttore.
Un attributo di istanza auto_presenti (lista di stringhe con le
targhe), inizialmente vuota.
Un metodo parcheggia che accetti una targa e aggiunga l'auto
alla lista. Se il garage è pieno, stampa un messaggio di errore.
Se la targa è già presente, avvisa che l'auto è già in garage.
Un metodo rimuovi che accetti una targa e rimuova l'auto        -----------
corrispondente. Se la targa non è presente, stampa un messaggio
di errore.
Un metodo posti_liberi che restituisca il numero di posti ancora    ------------
disponibili.
#extra
Un metodo statico formato_targa_valido che accetti una stringa e
restituisca True se la targa rispetta il formato italiano (2
lettere, 3 numeri, 2 lettere — es. "AB123CD"), False altrimenti.
Suggerimento: si può usare il metodo .isalpha() e .isdigit()
sulle sottostringhe.
Il metodo parcheggia deve usare formato_targa_valido per
rifiutare targhe non valide prima di aggiungerle.
"""
    
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
        return self.capieza - len(self.targhe)       
    
    def parcheggia(self):
        
        print("Inserire una targa") #blocco codice per input di targa maiuscolo e controllo
        targa = input().upper()
        if Garage.formato_targa_valido(targa):
        
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
            
            for t in self.targhe:
                if targa == t:          #controlla se esiste la targa
                    self.targhe.remove(targa)
                    print("targa: ", targa, " rimossa")
                else:
                    print("ERRORE targa non presente")        


contatore = False
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
        case "0":
            contatore = False
        case _:
            print("ERRORE Digitazione")
 
    