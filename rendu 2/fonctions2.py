from main import *

def fichier_to_texte(fichier):
    with open(fichier, 'r') as f:
        texte = f.read()
    return texte

def chiffre_message(message, key):
    chiffre = ""
    for m in message:
        ascii = ord(m)
        crypt = encrypt(key, encrypt(key, ascii))
        chiffre += chr(crypt)
    return chiffre

def dechiffre_message(message, key):
    dechiffre = ""
    for m in message:
        ascii = ord(m)
        crypt = decrypt(key, decrypt(key, ascii))
        dechiffre += chr(crypt)
    return dechiffre

def cassage_brutal_simple(message_clair, message_chiffre):
    for i in range(1024):
        key = bin(i)[2:].zfill(10)
        texte_dechiffre = dechiffre_message(message_chiffre, int(key))
        if texte_dechiffre == message_clair:
            return key
    return None

key = 1011110101

message = fichier_to_texte("texte.txt")
chiffre = chiffre_message(message, key)
# print(dechiffre_message(chiffre, key))

print(cassage_brutal_simple(message, chiffre))