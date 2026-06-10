""""Esercizio 3 (Medio):
Crea una classe chiamata ContoCorrente. Questa classe dovrebbe
avere:
Due attributi di istanza: intestatario e saldo (il saldo
iniziale deve essere passato al costruttore, con valore di
default 0).
Un metodo deposita che accetti un importo e lo aggiunga al
saldo. Se l'importo è negativo o zero, stampa un messaggio di
errore senza modificare il saldo.
Un metodo preleva che accetti un importo e lo sottragga dal
saldo. Se il saldo non è sufficiente, stampa un messaggio di
errore senza modificare il saldo.
Un metodo stampa_saldo che stampi una stringa del tipo "Il
saldo di 'intestatario' è: 'saldo' €"
.
"""
class ContoCorrente:
    
    def __init__(self, intestatario, saldo = 0):    #metodo creatore
        self.intestatario = intestatario
        self.saldo = saldo
    
    def deposita(self, importo):   #controlla l'importo passato e in caso true lo aggiunge
        
        if importo <= 0:
            print("ERRORE l'importo digitato non è positivo")
        else:
            self.saldo += importo
    
    def preleva(self, importo): #controlla l'importo passato e in caso true lo sottrae
        if self.saldo - importo:
            print("ERRORE SALDO NON SUFFICIENTE")
        else:
            self.saldo -= importo

    def stampa_saldo(self):     #stampa intestatario e saldo
        print("Il saldo di ", self.intestatario, " è: ", self.saldo," €")           

    @staticmethod      #static perchè se no non sapevo come richiamarla 
    def aggiungi_conti(conti_corrente):   #aggiunge i conti in una lista
        print("quanti conti vuole aprire:")
        numeri = int(input())
        for i in range(numeri):
            intestatario = input("Intestatario: ")
            importo = input("Importo: ")
            
            c = ContoCorrente(intestatario, importo)
            conti_corrente.append(c)     
    
    def stampa_conti(conti_corrente):   #stampa i conti in una lista però funziona anche richiamandolo tramite classe
        for c in conti_corrente: 
            c.stampa_saldo()   
 
    def deposita_lista(conti_corrente):
        for c in conti_corrente:
            c.stampa_saldo
            print("inserisci importo da depositare:")
            c.deposita(input())

    def preleva_lista(conti_corrente):
        for c in conti_corrente:
            c.stampa_saldo
            print("inserisci importo da prelevare:")
            c.preleva(input())
            
conti_corrente = []
contatore = True

"""
#test
conto01 = ContoCorrente("Gino", 1000)
conto01.deposita(100)
conto01.preleva(300)
conto01.stampa_saldo()
            
ContoCorrente.aggiungi_conti(conti_corrente)   
ContoCorrente.stampa_conti(conti_corrente)  
ContoCorrente.deposita_lista(conti_corrente)  
ContoCorrente.preleva_lista(conti_corrente)
"""
while contatore:
    print("scegli operazione")
    scelta = input()
    
    match scelta:
        case "1":
            ContoCorrente.aggiungi_conti(conti_corrente)
        case "2":
            ContoCorrente.stampa_conti(conti_corrente)
        case "3":
            ContoCorrente.deposita_lista(conti_corrente)  
        case "4":
            ContoCorrente.preleva_lista(conti_corrente)
        case "0":
            contatore = False
        case _:
            print("ERRORE Digitazione")
        