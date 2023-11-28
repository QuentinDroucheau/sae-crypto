from main import *

def convertir_texte_ascii(fichier):

    with open(fichier, 'r') as f:
        texte = f.read()
    texte_ascii = []
    for i in range(len(texte)):
        if texte[i] == ' ':
            texte_ascii.append(0)
        else :
            texte_ascii.append(ord(texte[i]))
    return texte_ascii

convertir_texte_ascii("lettres_persanes.txt")

def ascii_to_texte(texte_ascii):
    texte = ""
    for i in range(len(texte_ascii)):
        if texte_ascii[i] == 0:
            texte += " "
        else :
            texte += chr(texte_ascii[i])
    return texte

print(ascii_to_texte(convertir_texte_ascii("lettres_persanes.txt")))

def ascii_to_binaire(texte_ascii):
    texte_binaire = []
    for i in range(len(texte_ascii)):
        texte_binaire.append(bin(texte_ascii[i])[2:].zfill(8))
    return texte_binaire

print(ascii_to_binaire(convertir_texte_ascii("lettres_persanes.txt")))

def binaire_to_ascii(texte_binaire):
    texte_ascii = []
    for i in range(len(texte_binaire)):
        texte_ascii.append(int(texte_binaire[i],2))
    return texte_ascii

print(binaire_to_ascii(ascii_to_binaire(convertir_texte_ascii("lettres_persanes.txt"))))

print(ascii_to_texte(binaire_to_ascii(ascii_to_binaire(convertir_texte_ascii("lettres_persanes.txt")))))