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

def menu():
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

        if choice == "a" or choice =="A":
            print()
            text = input("Escribe mensaje: ")
            key = input("Letra de la llave: ")
            print ("Texto plano  : ", text )
            print ("Llave : ", str(key) )
            print ("Texto cifrado: ", caesar(text,key) )
            print()
        elif choice == "b" or choice =="B":
            pass
        elif choice == "c" or choice =="C":
            pass
        elif choice=="d" or choice=="D":
            pass
        elif choice=="q" or choice=="Q":
            return False
        else:
            print("Opción inválida, vuelve a intentar. \n")
            menu()
        cont = input("Continuar(y/n)? ")
        if cont == "y": pass
        else: return False      

def main():
    menu()
    
main()