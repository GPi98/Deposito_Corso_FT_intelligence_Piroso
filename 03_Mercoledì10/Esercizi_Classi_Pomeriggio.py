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
    
    def __init__(self, intestatario, saldo = 0):
        self.intestatario = intestatario
        self.saldo = saldo
    
    def deposita(self, importo):
        
        if importo <= 0:
            print("ERRORE l'importo digitato non è positivo")
            return
        