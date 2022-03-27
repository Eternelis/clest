#!/bin/python3


from tkinter import E


def tower():
    etages = int(input("Entrez le nombre d'étages : "))
    # Toit
    print('   ________')
    print('  /        \\')
    print(' /          \\')
    print('|____________|')
    for i in range(1, etages):
        print('|‾‾‾‾‾‾‾‾‾‾‾‾|')
        print('| |😀|  |😀| |')
        print('|____________|')
    # fondation

    print('|‾‾‾‾‾‾‾‾‾‾‾‾|')
    print('|____________|')


tower()
