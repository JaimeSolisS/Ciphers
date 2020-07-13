import random

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


def main():
    while True:
        print("************Ciphers**************")
        print()
        choice = input("""
        a: Cifrado del cesar
        b: Vigenere 
        c: One Time Pad 
        d: Descifrar cesar 
        e: Descifrar vigenere
        q: Terminar 
        Elegir una opción: """)

        if choice == "a":
            print()
            text = input("Escribe mensaje: ")
            key = input("Letra de la llave: ")
            print ("Texto plano:   ", text)
            print ("Llave:         ", str(key))
            print ("Texto cifrado: ", caesar(text,key))
            print()
        elif choice == "b":
            text = input("Escribe mensaje: ")
            keySequence = input("Secuencia de la llave: ")
            key = generateKey(text, keySequence) 
            print ("Texto plano:   ", text)
            print ("Llave:         ", str(key))
            print ("Texto cifrado: ", vigenere(text,key))
        elif choice == "c":
            text = input("Escribe mensaje: ")
            #keySequence = input("Secuencia de la llave: ")
            print()
            key = generateRandomKey(text) 
            print ("Texto plano:   ", text)
            print ("Llave:         ", str(key))
            print ("Texto cifrado: ", vigenere(text,key))
        elif choice=="d" or choice=="D":
            pass
        elif choice=="q" or choice=="Q":
            return False
        else:
            print("Opción inválida, vuelve a intentar. \n")
            main()
        cont = input("Continuar(y/n)? ")
        if cont == "y": pass
        else: return False      
    
main()