#
#  ciphers.py
#
#  Created by Jaime Solis on 07/11/20.
#  Copyright © 2020 personal. All rights reserved.
#

import random, os
from collections import Counter

ALPHABET = "abcdefghijklmnopqrstuvwxyz "

#----------Cifrado del Cesar--------------------#
def caesar(text,key): 
    encripted = "" 
    keyShift = ALPHABET.find(key)
    for c in text: 
        if c in ALPHABET:
            index = ALPHABET.find(c)
            index_shift = (index + keyShift) % len(ALPHABET)
            new_char = ALPHABET[index_shift]
            encripted += new_char
        else:
            encripted += c
    return encripted

#----------Cifrado de Vigenere--------------------#
def generateKey(text, key): 
    key = list(key) 
    text = ''.join([i for i in text if i in ALPHABET]) #Solo caracteres del alfabeto
    if len(text) == len(key): 
        return(key) 
    else: 
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)]) 
    return("" . join(key)) 

def vigenere(text, key): 
    encripted = "" 
    j = 0 #index para la llave y no tener problema con caracteres fuera del alfabeto 
    for c in text: 
        if c in ALPHABET:
            keyShift = ALPHABET.find(key[j])
            index = ALPHABET.find(c)
            index_shift = (index + keyShift) % len(ALPHABET)
            new_char = ALPHABET[index_shift]
            encripted += new_char
            j+=1
        else: 
            encripted += c
    return encripted  

#----------One time pad --------------------#
def generateRandomKey(text): 
    key = list() 
    text = ''.join([i for i in text if i in ALPHABET]) #Solo caracteres del alfabeto
    for i in range(len(text)):
        key.append(chr(random.randint(97,122))) 
    return("" . join(key)) 
#Usar Vigenere function

#---------Análisis de frecuencia----------------#
def frequenceCounter(text):
    topFrequence = int(input("Ver el top _ de los caracteres más frecuentes: "))
    counts=Counter(text) 
    for c, count in counts.most_common(topFrequence): 
        print('%s: %d' % (c, count)) 

#---------Decifrar-------------------------#
def decrypt(key, text):
    key = ord(key) - 97 # ascii de la llave - desplazamiento
    decrypted = ""

    for c in text:
        if c in ALPHABET: 
            index = (ALPHABET.find(c) - key) % len(ALPHABET)
            decrypted += ALPHABET[index]
        else:
            decrypted += c
    return decrypted

#---------Decifrar Cesar---------------------#
def decryptCaesar(text):
    key = ""

    for i in range(len(ALPHABET)):
        decoded =decrypt(ALPHABET[i],text)
        bag = getBagOfChars(decoded)
        mostFrequentChar = mostFrequent(bag)
        if mostFrequentChar == " ":
            key += ALPHABET[i]

    print("Caracter de la Llave = ", key)
    decrypted = ""
    for i in range(len(text)):
         decrypted += decrypt(key, text[i])
    return decrypted

#---------Decifrar Vigenere------------------#
def getNthChars(text, n): 
    return text[n::4]

def getBagOfChars(decoded):
    bag = ""
    for i in range(len(decoded)):
        bag += decoded[i]
    return bag

def mostFrequent(text):
    counts=Counter(text) 
    for c, count in counts.most_common(1): 
        return c

def decryptVigenere(text):
    key = ""
    subtext1 = getNthChars(text,0)
    subtext2 = getNthChars(text,1)
    subtext3 = getNthChars(text,2)
    subtext4 = getNthChars(text,3)

    subtextList = [subtext1, subtext2, subtext3, subtext4]

    for subtext in subtextList: 
        for i in range(len(ALPHABET)):
            decoded =decrypt(ALPHABET[i],subtext)
            bag = getBagOfChars(decoded)
            mostFrequentChar = mostFrequent(bag)
            if mostFrequentChar == " ":
                key += ALPHABET[i]

    print("Secuencia de la llave = ", key)
    decrypted = ""
    for i in range(len(text)):
         decrypted += decrypt(key[i%4], text[i])
    return decrypted

def main():
    while True:
        os.system('clear')
        print("************Ciphers**************")
        choice = input("""
        a: Cifrado del cesar
        b: Cifrado de Vigenere 
        c: One Time Pad 
        d: Descifrar cesar Brute Force
        e: Descifrar cesar 
        f: Descifrar vigenere
        q: Terminar 
        Elegir una opción: """)
        print()
        if choice == "a": 
            print("************ Cifrado del cesar **************")
            text = input("Escribe mensaje: ")
            key = input("Letra de la llave: ")
            print()
            print ("Texto plano:   ", text)
            print ("Llave:          ", end= "")
            for i in range(len(text)):
                if text[i] in ALPHABET: print (str(key), end="")
                else: print(" ", end="")
            print ("\nTexto cifrado: ", caesar(text,key))
            print()
        elif choice == "b":
            print("************ Cifrado de Vigenere **************")
            text = input("Escribe mensaje: ")
            keySequence = input("Secuencia de la llave: ")
            print()
            key = generateKey(text, keySequence) 
            print ("Texto plano:   ", text)
            print ("Llave:          ", end= "")
            j = 0
            for i in range(len(text)):
                if text[i] in ALPHABET: print (str(key[j]), end=""); j+=1
                else: print(" ", end=""); 
            print ("\nTexto cifrado: ", vigenere(text,key))
        elif choice == "c": 
            print("************ Cifrado One time Pad **************")
            text = input("Escribe mensaje: ")
            print()
            key = generateRandomKey(text) 
            print ("Texto plano:   ", text)
            print ("Llave:          ", end= "")
            j = 0
            for i in range(len(text)):
                if text[i] in ALPHABET: print (str(key[j]), end=""); j+=1
                else: print(" ", end=""); 
            print ("\nTexto cifrado: ", vigenere(text,key))
        elif choice=="d": 
            print("************ Rompiendo el algoritmo del cesar por 'fuerza bruta' **************")
            file = open("cipher1.txt")
            text = file.read().replace("\n", " ")
            file.close()
            prinText = input("Imprimir texto cifrado(y/n)?")
            if prinText == "y":
                print(text)
                input("Presiona enter para continuar...")
            print()
            frequenceCounter(text)
            while True:
                key = input("Ingresa la posible llave: ")
                print ("Texto decifrado: \n", decrypt(key, text))
                correct = input("Intentar con otra llave(y/n)? ")
                if correct == "y": pass
                else: break  
        elif choice=="e": 
            print("************ Rompiendo el algoritmo del cesar **************")
            file = open("cipher1.txt")
            text = file.read().replace("\n", " ")
            file.close()
            prinText = input("Imprimir texto cifrado(y/n)?")
            if prinText == "y":
                print(text)
                input("Presiona enter para continuar...")
            print()
            print ("Texto decifrado: \n", decryptCaesar(text))
        elif choice=="f": 
            print("************ Rompiendo el algoritmo de Vigenere **************")
            file = open("cipher2.txt")
            text = file.read().replace("\n", " ")
            file.close()
            prinText = input("Imprimir texto cifrado(y/n)?")
            if prinText == "y":
                print(text)
                input("Presiona enter para continuar...")
            print()
            print ("Texto decifrado: \n", decryptVigenere(text))
        elif choice=="q":return False
        else:
            print("Opción inválida, vuelve a intentar. \n")
            main()
        print()
        cont = input("Volver al menu(y/n)? ")
        if cont == "y": pass
        else: return False    

main()