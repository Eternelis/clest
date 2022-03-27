#!/bin/python3

from math import sqrt


def fibo():
    Fuser = int(input('Veuillez entrer un nombre : '))
    print(fibo_r(Fuser))


def fibo_r(Fuser):
    if Fuser <= 1:
        return Fuser
    return fibo_r(Fuser - 1) + fibo_r(Fuser - 2)


def sieve():
    nb_sieve = int(input('Veuillez enter un nombre : '))
    liste = ['placeholder', 'placeholder2']
    for i in range(2, nb_sieve):
        liste.append(True)
    for i in range(2, int(sqrt(nb_sieve)) + 1):
        if liste[i] == True:
            for j in range(i*i, nb_sieve, i):
                liste[j] = False
    for i in range(2, nb_sieve):
        if liste[i] == True:
            print(i)
    return
