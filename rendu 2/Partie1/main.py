from sdes import *

import time


"""
Simple SDES
"""
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

# key = 1011110101

# message = fichier_to_texte("texte.txt")
# chiffre = chiffre_message(message, key)
# # print(dechiffre_message(chiffre, key))

# print(cassage_brutal_simple(message, chiffre))

"""
Double SDES
"""

def chiffre_message_double(message, key1, key2):
    chiffre = ""
    for m in message:
        ascii = ord(m)
        crypt = encrypt(key1, encrypt(key2, ascii))
        chiffre += chr(crypt)
    return chiffre

def dechiffre_message_double(message, key1, key2):
    dechiffre = ""
    for m in message:
        ascii = ord(m)
        crypt = decrypt(key2, decrypt(key1, ascii))
        dechiffre += chr(crypt)
    return dechiffre

def cassage_brutal_double(message_clair, message_chiffre):
    start = time.time()
    for i in range(1024):
        key1 = bin(i)[2:].zfill(10)
        for j in range(1024):
            key2 = bin(j)[2:].zfill(10)
            texte_dechiffre = dechiffre_message_double(message_chiffre, int(key1), int(key2))
            if texte_dechiffre == message_clair:
                return True, time.time() - start
    return False, time.time() - start


def cassage_astucieux_double(message_clair, message_chiffre):
    start = time.time()
    for i in range(1024):
        key1 = bin(i)[2:].zfill(10)
        texte_dechiffre = dechiffre_message(message_chiffre, int(key1))
        for j in range(1024):
            key2 = bin(j)[2:].zfill(10)
            texte_dechiffre2 = dechiffre_message(texte_dechiffre, int(key2))
            if texte_dechiffre2 == message_clair:
                return True, time.time() - start
    return False, time.time() - start


message = fichier_to_texte("arsene_lupin_extrait.txt")
chiffre = chiffre_message_double(message, 1011110101, 1011110101)


print(cassage_astucieux_double(message, chiffre))