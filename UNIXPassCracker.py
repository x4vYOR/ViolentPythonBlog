import crypt

def testPass(cryptPass): #recibe una contrasena cifrada
    salt = cryptPass[0:2] #obtiene los dos primeros caracteres
    dictFile = open('dictionary.txt','r') #Abre nuestro diccionario de palabras
    for word in dictFile.readlines():
        word = word.strip('\n') #
        cryptWord = crypt.crypt(word,salt) #Cifrara cada palabra usando el salt
                                            #que obtuvimos.
        if (cryptWord == cryptPass): #Compara nuestra palabra cifrada con la contraseña
            print "[+] Found Password: "+word+"\n"
            return
    print "[-] Password Not Found. \n"
    return

def main():
    passFile = open('passwords.txt','r') #Abre el archivo con los pass cifrados.
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0] #separa el nombre de usuario
            cryptPass = line.split(':')[1].strip(' ')  # y el hash
            print "[*] Cracking Password For: "+user
            testPass(cryptPass) #envia el hash para compararlo

if __name__ == '__main__':
main()
