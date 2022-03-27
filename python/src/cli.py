#!/bin/python3

from src.algo import *
from src.functions import *


def cli():
    name = ''
    while True:
        cmd = ask(name)
        if cmd == "exit":
            break
        elif cmd == "hello":
            hello()
        elif cmd == "settings":
            name = settings()
        elif cmd == "fibo":
            fibo()
        elif cmd == 'sieve':
            sieve()
        else:
            print("Commande inconnue")
