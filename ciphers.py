# Instituto Tecnológico de Estudios Superiores de Monterrey
# 
# Actividad 3:  Criptografía y Criptoanalisis
#
# Seguridad Informática 
#   
# Profesor: Dr. Jorge Rodríguez Ruiz
#
# Periodo Verano 2020
#  
# Jaime Solis                A00759756 
# Ruben Castillo Torres      A01610711
# Sebastián González Tafoya  A01233416
#                                        
# Fecha de entrega  13/07/2020.
#

import random, os
from collections import Counter

ALPHABET = "abcdefghijklmnopqrstuvwxyz "

#----------Cifrado del Cesar--------------------#
def caesar(text,key): 
    encripted = ""  
    keyShift = ALPHABET.find(key) # El indice de desplazamiento de la llave
    for c in text: 
        if c in ALPHABET:  #Solo cifrar caracteres del alfabeto
            index = ALPHABET.find(c) #Posicion del caracter plano
            index_shift = (index + keyShift) % len(ALPHABET) #Posicion del caracter dezplazado
            new_char = ALPHABET[index_shift] #Caracter encriptado
            encripted += new_char #Agregar caracter a la cadena
        else:
            encripted += c #Regresar caracter plano
    return encripted

#----------Cifrado de Vigenere--------------------#
def generateKey(text, key): 
    key = list(key) 
    text = ''.join([i for i in text if i in ALPHABET]) #Solo caracteres del alfabeto
    if len(text) == len(key): #Si el largo de la llave es igual al texto plano, regresar la llave tal cual
        return(key) 
    else: 
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)]) #Agregar a la secuencia de la llave caracter por caracter
    return("" . join(key)) 

def vigenere(text, key): 
    encripted = "" 
    j = 0 #index para la llave y no tener problema con caracteres fuera del alfabeto, el resto es igual al cifrado del cesar 
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
        key.append(chr(random.randint(97,122))) #agregar caracteres aleatorios a la secuencia de la llave
    return("" . join(key)) 

# Mandar llamar a la función vigenere

#---------Análisis de frecuencia----------------#
def frequenceCounter(text):
    topFrequence = int(input("Ver el top _ de los caracteres más frecuentes: "))
    counts=Counter(text) 
    for c, count in counts.most_common(topFrequence): #Contar la frecuencia de los n caracteres más repetidos
        print('%s: %d' % (c, count)) 

#---------Desencriptar texto con llave-------------------------#
def decrypt(key, text):
    key = ord(key) - 97 # ascii de la llave - desplazamiento
    decrypted = ""
    for c in text:
        if c in ALPHABET: 
            index = (ALPHABET.find(c) - key) % len(ALPHABET) #indice del caracter cifrado menos el dezplazamiento de la llave
            decrypted += ALPHABET[index] #agregar caracter al string descifrado
        else:
            decrypted += c 
    return decrypted

#---------Decifrar Cesar---------------------#
def getBagOfChars(decoded): #funcion auxiliar 
    bag = ""
    for i in range(len(decoded)):
        bag += decoded[i]
    return bag

def decryptCaesar(text):
    key = ""
    for i in range(len(ALPHABET)):# Por cada caracter en el alfabeto...
        decoded =decrypt(ALPHABET[i],text) #crear un string con texto descifrado 
        bag = getBagOfChars(decoded) #crear un auxiliar con los caracteres del texto descifrado
        mostFrequentChar = mostFrequent(bag) #calcular el caracter mas frecuente del bag
        if mostFrequentChar == " ": #si el caracter de espacio es el más frecuente, encontramos el shift o "la llave" correcta
            key += ALPHABET[i] #guardamos el caracter de la llave

    print("Caracter de la Llave = ", key)
    f= open("Llaves.txt","a+")
    f.write("Llave Caesar = %s\r\n" % key)
    decrypted = ""
    for i in range(len(text)):
         decrypted += decrypt(key, text[i]) #llamar la función decrypt y decifrar todos los caracteres
    f= open("cipher1_Descifrado.txt","w+")
    f.write("Texto plano: \n%s\r\n" % decrypted)
    return decrypted

#---------Decifrar Vigenere------------------#
def getNthChars(text, n): #Funcion auxiliar para crear subtextos con cada 4to caracter
    return text[n::4]

def mostFrequent(text): #Funcion auxiliar para encontrar el caracter más frecuente en un string
    counts=Counter(text) 
    for c, count in counts.most_common(1): 
        return c

def decryptVigenere(text): #Es los mismo solo que hay que dividir el texto cifrado en 4 subtextos ya que conocemos que la secuencia de la llave se repite cada 4 caracteres
    key = ""
    subtext1 = getNthChars(text,0) #creamos un subtexto empezando en el primer caracter y saltando de 4 en 4...
    subtext2 = getNthChars(text,1) #Empezando en el segundo...
    subtext3 = getNthChars(text,2) #En el tercero...
    subtext4 = getNthChars(text,3) #En el cuarto...

    subtextList = [subtext1, subtext2, subtext3, subtext4]

    for subtext in subtextList:     #Hacemos lo mismo que para decifrar cesar, solo que cada subtexto nos va a dar un caracter de la llave
        for i in range(len(ALPHABET)):
            decoded =decrypt(ALPHABET[i],subtext)
            bag = getBagOfChars(decoded)
            mostFrequentChar = mostFrequent(bag)
            if mostFrequentChar == " ":
                key += ALPHABET[i]

    print("Llave Vigenere = ", key)
    f= open("Llaves.txt","a+")
    f.write("Llave Vigenere = %s\r\n" % key)
    decrypted = ""
    for i in range(len(text)):
         decrypted += decrypt(key[i%4], text[i])
    f= open("cipher2_Descifrado.txt","w+")
    f.write("Texto plano: \n%s\r\n" % decrypted)
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