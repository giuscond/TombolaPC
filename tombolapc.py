# !/usr/bin/python
#
# TombolaPC


import numpy as np
from numpy import random

m = np.zeros( (9,10) , dtype=int ) # Matrice del tombolone
numero = int(0) # Numero estratto
nestratti=[0,0,0,0,0] # Ultimi 5 numeri in memoria

# Funzione stampa a schermo il Tombolone
def stampa():
    for i in range(9):
        if i == 0 or i == 3 or i == 6:
            print("-----------------------------------")
        print(end="| ")  
        if i == 0: # If correttivo per le caselle a singola cifra (DA MIGLIORARE)
            for j in range(10):
                if j != 4:
                    if m[i][j] == 0:
                        print("__", end=" ")
                    else:
                        print("_", m[i][j], sep="", end=" ")
                elif j == 4:
                    if m[i][j] == 0:
                        print("__", end=" | ")
                    else:
                        print("_", m[i][j], sep="", end=" | ")
    # Stampa tutte le altre cifre
        else:
            for j in range(10):
                if j != 4:
                    if m[i][j] == 0:
                        print("__", end=" ")
                    else:
                        print(m[i][j], end=" ")
                elif j == 4:
                    if m[i][j] == 0:
                        print("__", end=" | ")
                    else:
                        print(m[i][j], end=" | ")
        print(end="|\n")
    print("-----------------------------------")


# Funzione numero immesso dall'utente. Se già presente il numero, rimuovilo
def estratto():
    # Aggiungi numero alla matrice
    global numero
    numero = input("Prossimo numero estratto: ")
    numero = int(numero)
    if numero>0 and numero<=90:
        if numero%10 == 0: # Calcola la posizione dei multipli di 10 nella matrice
            a=int(numero / 10)-1
            b=9
        else: # Calcola la posizione di tutti gli altri numeri
            a=int(numero / 10)
            b=(numero%10)-1
        # Controlla se il numero è presente, altrimenti rimuovilo
        if m[a][b]==0:
            m[a][b]=numero
        else:
            m[a][b]=0
    # Esci con 999
#     elif numero == 999:
#         exit(0)
    # Se il numero non è valido
    else: # Messaggio d'errore se il numero non è valido
        print("Numero non valido. Riprova.")
        estratto()

# Funzione che stampa e annota l'ultimo numero estretto
def ultimiestratti():  
    for i in range(4):
        nestratti[i]=nestratti[i+1]
    nestratti[4] = numero
    print("Ultimi numeri estratti:", nestratti, sep=" ", end="\n")

# Funzione che genera un numero casuale non ancora estratto
def rand():
    while True:
        global numero
        numero = random.randint(1,91)
        if numero%10 == 0: # Calcola la posizione dei multipli di 10 nella matrice
            a=int(numero / 10)-1
            b=9
        else: # Calcola la posizione di tutti gli altri numeri
            a=int(numero / 10)
            b=(numero%10)-1       
        if m[a][b]==0: # Controlla se il numero è presente, altrimenti ritenta
            m[a][b]=numero
            print("Estratto il numero: ", numero)
            break


# Modalita' 2: Il computer estrae un numero
def mod_estrazione():
    while True:
        stampa()
        ultimiestratti()
        print("Estratto il numero: ", numero)
        input("Premi INVIO per estranne un nuovo numero: ")
        rand()

# Modalita' 1: il numero estratto va immesso manualmente
def mod_tombolone():
    while True:
        stampa()
        ultimiestratti()
        estratto()

# Fine funzioni
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Inizio di TombolaPC

print("Benvenuto su TOMBOLAPC!\n Puoi scegliere due modalita' di gioco:")
print("- 1 Modalita' Tombolone: i numeri verranno inseriti manualmente;")
print("- 2 Modalita' Estrazione: i numeri saranno estratti dal programma.")
c = input ("\nDigita la modalità di gioco: ")
c = int(c)
if c == 1:
    mod_tombolone()
elif c == 2:
    mod_estrazione()







