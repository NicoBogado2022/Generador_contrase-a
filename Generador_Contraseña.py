import random


def generador_pass(largo=8, capital=False, numeros=False, simbolos=False):

        caracteres = list(range(97, 123))

        if capital:
            caracteres += list(range(65, 91))
        if numeros:
            caracteres += list(range(49, 58))
        if simbolos:
            caracteres += list(range(33, 48))

        password = ""

        largo_total = 8 if largo < 8 else 16 if largo > 16 else largo

        while len(password) < largo_total:
            password += chr(random.choice(caracteres))

        return password
print(generador_pass())
