#più utilizzate 2   liste e dizionari

punto = (3, 4)
colore_rgb = (255, 128, 0)
informazioni_persona = ("Alice", 25, "Femmina")

punto = (3, 4)
print(punto[0])
print(punto[1])

#punto = (3, 4)
#punto[0] = 5 # Genera un errore: TypeError

punto = 3, 4 # Tuple packing
x, y = punto # Tuple unpacking
print(x, y) # Output: 3 4

set1 = set([1, 2, 3, 4, 5])
set2 = {4, 5, 6, 7, 8}

set3 = {1, 2, 3, 3, 4, 4, 5}
print(set3) # Output: {1, 2, 3, 4, 5}

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) # Output: {4, 5}
print(set1.difference(set2)) # Output: {1, 2, 3}
print(set1.symmetric_difference(set2)) # Output: {1, 2, 3, 6, 7, 8}


studente = {"nome": "Alice", "età": 20, "sesso": "Femmina"}
print(studente["nome"]) # Output: "Alice"
print(studente["età"]) # Output: 20

#per valorizzare gli elementi 
x = studente["nome"]
print(x)

studente["età"] = 21
print(studente)

# output {'nome': 'Alice', 'età': 21, 'sesso':'Femmina'}

studente["città"] = "Roma"
print(studente)
# Output:{'nome': 'Alice','età': 21, 'sesso':'Femmina', 'città': 'Roma'}

print(studente.keys()) # Output: dict_keys(['nome','età','sesso'])
print(studente.values()) # Output: dict_values(['Alice', 20,'Femmina'])

for x,y in studente.items():
    print(x,y)


########## ESEMPI DEL PROF

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DIZIONARI, SET E TUPLE IN PYTHON

- Tuple
- Set
- Dizionari
- Dizionari annidati
- Dizionari con liste
- Cicli su dizionari
- Operazioni comuni
"""

# ==============================================================
# 1. TUPLE
# ==============================================================

print("=== 1. Tuple ===")

coordinate = (10, 20)

print(coordinate)
print("X =", coordinate[0])
print("Y =", coordinate[1])

print()


# ==============================================================
# 2. UNPACKING DI TUPLE
# ==============================================================

print("=== 2. Unpacking ===")

nome, eta = ("Mario", 25)

print(nome)
print(eta)

print()


# ==============================================================
# 3. TUPLE IMMUTABILI
# ==============================================================

print("=== 3. Tuple immutabili ===")

giorni = ("Lun", "Mar", "Mer")

print(giorni)
print(len(giorni))

print()


# ==============================================================
# 4. SET BASE
# ==============================================================

print("=== 4. Set ===")

numeri = {1, 2, 3, 4}

print(numeri)

numeri.add(5)

print(numeri)

print()


# ==============================================================
# 5. RIMOZIONE DUPLICATI
# ==============================================================

print("=== 5. Rimozione duplicati ===")

lista = [1, 2, 2, 3, 3, 3, 4]

unici = set(lista)

print(unici)

print()


# ==============================================================
# 6. OPERAZIONI TRA SET
# ==============================================================

print("=== 6. Operazioni tra set ===")

A = {1, 2, 3}
B = {3, 4, 5}

print("Unione:", A | B)
print("Intersezione:", A & B)
print("Differenza:", A - B)

print()


# ==============================================================
# 7. DIZIONARIO BASE
# ==============================================================

print("=== 7. Dizionario Base ===")

persona = {
    "nome": "Anna",
    "eta": 25,
    "citta": "Roma"
}

print(persona)

print("Nome:", persona["nome"])

print()


# ==============================================================
# 8. AGGIUNTA E MODIFICA
# ==============================================================

print("=== 8. Modifica ===")

persona["eta"] = 26
persona["lavoro"] = "Programmatrice"

print(persona)

print()


# ==============================================================
# 9. CICLO SULLE CHIAVI
# ==============================================================

print("=== 9. Chiavi ===")

for chiave in persona:
    print(chiave)

print()


# ==============================================================
# 10. CICLO SUI VALORI
# ==============================================================

print("=== 10. Valori ===")

for valore in persona.values():
    print(valore)

print()


# ==============================================================
# 11. CICLO CHIAVE-VALORE
# ==============================================================

print("=== 11. Chiave-Valore ===")

for chiave, valore in persona.items():
    print(chiave, "->", valore)

print()


# ==============================================================
# 12. DIZIONARIO CON LISTE
# ==============================================================

print("=== 12. Dizionario con Liste ===")

studente = {
    "nome": "Luca",
    "voti": [28, 30, 27, 29]
}

print(studente)

print("Lista voti:", studente["voti"])

print()


# ==============================================================
# 13. CICLO SU LISTA INTERNA
# ==============================================================

print("=== 13. Ciclo Lista Interna ===")

for voto in studente["voti"]:
    print(voto)

print()


# ==============================================================
# 14. MEDIA DEI VOTI
# ==============================================================

print("=== 14. Media Voti ===")

media = sum(studente["voti"]) / len(studente["voti"])

print("Media:", media)

print()


# ==============================================================
# 15. DIZIONARIO ANNIDATO
# ==============================================================

print("=== 15. Dizionario Annidato ===")

studenti = {
    "s1": {
        "nome": "Anna",
        "voti": [30, 28, 29]
    },
    "s2": {
        "nome": "Marco",
        "voti": [25, 27, 26]
    }
}

print(studenti)

print()


# ==============================================================
# 16. CICLO SU DIZIONARIO ANNIDATO
# ==============================================================

print("=== 16. Dizionario Annidato + Cicli ===")

for codice, dati in studenti.items():

    print("Codice:", codice)
    print("Nome:", dati["nome"])

    for voto in dati["voti"]:
        print("Voto:", voto)

    print()

print()


# ==============================================================
# 17. CALCOLO MEDIA PER OGNI STUDENTE
# ==============================================================

print("=== 17. Media per Studente ===")

for codice, dati in studenti.items():

    media = sum(dati["voti"]) / len(dati["voti"])

    print(dati["nome"], "->", media)

print()


# ==============================================================
# 18. DIZIONARIO DI SET
# ==============================================================

print("=== 18. Dizionario con Set ===")

classi = {
    "Python": {"Anna", "Luca", "Marco"},
    "Java": {"Luca", "Sara"}
}

for corso, iscritti in classi.items():

    print(corso)

    for persona in iscritti:
        print("-", persona)

print()


# ==============================================================
# 19. DIZIONARIO DI TUPLE
# ==============================================================

print("=== 19. Dizionario con Tuple ===")

citta = {
    "Roma": (41.90, 12.49),
    "Milano": (45.46, 9.19)
}

for nome, coordinate in citta.items():

    latitudine, longitudine = coordinate

    print(nome)
    print("Lat:", latitudine)
    print("Lon:", longitudine)

print()


# ==============================================================
# 20. ESEMPIO COMPLETO
# ==============================================================

print("=== 20. Registro Studenti ===")

registro = {
    "Anna": [30, 28, 29],
    "Luca": [25, 27, 30],
    "Marco": [22, 24, 26]
}

for nome, voti in registro.items():

    totale = sum(voti)
    media = totale / len(voti)

    print(nome)
    print("Voti:", voti)
    print("Totale:", totale)
    print("Media:", round(media, 2))
    print()

