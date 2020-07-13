import random
from collections import Counter

#----------Cifrado del Cesar--------------------#
def caesar(text,key): 
    encripted = "" 
    key = ord(key) # ascii de la llave
    for i in range(len(text)): 
        c = text[i] # cada caracter
        if c.isalpha(): #si el caracter es una letra hacemos la transposicion, si no, regresamos el caracter
            if (ord(c) + key - 97) > 122: # si la operación da igual a +123, se reinicia el alfabeto  
                encripted += chr((ord(c) + key - 97 )-26) 
            else: encripted += chr((ord(c) + key - 97 )) #ascii del caracter del mensaje + ascii de la llave - 97(ascii de 'a')
        else: encripted += c
    return encripted  

#----------Cifrado de Vigenere--------------------#
def generateKey(text, key): 
    key = list(key) 
    text = ''.join([i for i in text if i.isalpha()]) #Solo caracteres en el texto plano
    if len(text) == len(key): 
        return(key) 
    else: 
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)]) 
    return("" . join(key)) 

def vigenere(text, key): 
    encripted = "" 
    j = 0 #index para la llave 
    for i in range(len(text)): 
        c = text[i] # cada caracter
        if c.isalpha(): #si el caracter es una letra hacemos la transposicion, si no, regresamos el caracter
            if (ord(c) + ord(key[j]) - 97) > 122: # si la operación da igual a +123, se reinicia el alfabeto  
                encripted += chr((ord(c) + ord(key[j]) - 97 )-26) 
            else: encripted += chr((ord(c) + ord(key[j]) - 97 )) #ascii del caracter del mensaje + ascii de la llave - 97(ascii de 'a') 
        else: 
            encripted += c
            j-=1
        j+=1
    return encripted  

#----------One time pad --------------------#
def generateRandomKey(text): 
    key = list() 
    text = ''.join([i for i in text if i.isalpha()]) #Solo caracteres en el texto plano
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
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    decrypted = ""

    for c in text:
        if c in alphabet: 
            index = (alphabet.find(c) - key) % len(alphabet)
            decrypted += alphabet[index]
        else:
            decrypted += c
    return decrypted

#---------Decifrar Cesar---------------------#
def decryptCaesar(text):
    key = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz "

    for i in range(len(alphabet)):
        decoded =decrypt(alphabet[i],text)
        bag = getBagOfChars(decoded)
        mostFrequentChar = mostFrequent(bag)
        if mostFrequentChar == " ":
            key += alphabet[i]

    print("Llave = ", key)
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
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    subtext1 = getNthChars(text,0)
    subtext2 = getNthChars(text,1)
    subtext3 = getNthChars(text,2)
    subtext4 = getNthChars(text,3)

    subtextList = [subtext1, subtext2, subtext3, subtext4]

    for subtext in subtextList: 
        for i in range(len(alphabet)):
            decoded =decrypt(alphabet[i],subtext)
            bag = getBagOfChars(decoded)
            mostFrequentChar = mostFrequent(bag)
            if mostFrequentChar == " ":
                key += alphabet[i]

    print("Llave = ", key)
    decrypted = ""
    for i in range(len(text)):
         decrypted += decrypt(key[i%4], text[i])
    return decrypted

def main():
    while True:
        print("************Ciphers**************")
        print()
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
            text = input("Escribe mensaje: ")
            key = input("Letra de la llave: ")
            print()
            print ("Texto plano:   ", text)
            print ("Llave:         ", str(key))
            print ("Texto cifrado: ", caesar(text,key))
            print()
        elif choice == "b":
            text = input("Escribe mensaje: ")
            keySequence = input("Secuencia de la llave: ")
            print()
            key = generateKey(text, keySequence) 
            print ("Texto plano:   ", text)
            print ("Llave:         ", str(key))
            print ("Texto cifrado: ", vigenere(text,key))
        elif choice == "c": 
            text = input("Escribe mensaje: ")
            print()
            key = generateRandomKey(text) 
            print ("Texto plano:   ", text)
            print ("Llave:         ", str(key))
            print ("Texto cifrado: ", vigenere(text,key))
        elif choice=="d": 
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
                if correct == "y": 
                    pass
                else: 
                    break  
        elif choice=="e": 
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
            file = open("cipher2.txt")
            text = file.read().replace("\n", " ")
            file.close()
            prinText = input("Imprimir texto cifrado(y/n)?")
            if prinText == "y":
                print(text)
            input("Presiona enter para continuar...")
            print()
            print ("Texto decifrado: \n", decryptVigenere(text))
        elif choice=="q":
            return False
        else:
            print("Opción inválida, vuelve a intentar. \n")
            main()
        print()
        cont = input("Volver al menu(y/n)? ")
        if cont == "y": pass
        else: return False      
    
main()