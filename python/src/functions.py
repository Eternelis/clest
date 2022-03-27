#!/bin/python3

def hello():
    liste = ['A', 'B', 'C']
    print("Bonjour")
    for arg in liste:
        print(arg)


def settings():
    name = input('Veuillez entrer votre nom : ')
    print(name)
    return name


def ask(name):
    if name != '':
        print('Entrez une commande,', name, ': ')
        cmd = input()
    else:
        cmd = input('Veuillez entrer une commande : ')
    return cmd
