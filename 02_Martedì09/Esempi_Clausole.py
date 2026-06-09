for i in range (5):
    
    if i == 3:
        pass        #non fa nulla oltre a non dare errori durante la costruzione della struttura
    print(i)
    if i == 4:
        continue    #salta un giro
    if i == 5:
        break       #chiude il ciclo
    
numeri = [*range(1, 11)]    #splat
print(numeri)
