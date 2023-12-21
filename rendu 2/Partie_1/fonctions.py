from main import *

def convertir_fichier_ascii(fichier):

    with open(fichier, 'r') as f:
        texte = f.read()
    texte_ascii = []
    for i in range(len(texte)):
            texte_ascii.append(ord(texte[i]))
    return texte_ascii

# print(convertir_texte_ascii("lettres_persanes.txt"))

def texte_to_ascii(texte):
    texte_ascii = []
    for i in range(len(texte)):
        texte_ascii.append(ord(texte[i]))
    return texte_ascii

def ascii_to_texte(texte_ascii):
    texte = []
    for i in range(len(texte_ascii)):
        texte.append(chr(texte_ascii[i]))
    return texte

# print(ascii_to_texte(convertir_texte_ascii("lettres_persanes.txt")))

def ascii_to_binaire(texte_ascii):
    texte_binaire = []
    for i in range(len(texte_ascii)):
        texte_binaire.append(bin(texte_ascii[i])[2:].zfill(8))
    return texte_binaire

# print(ascii_to_binaire(convertir_texte_ascii("lettres_persanes.txt")))

def binaire_to_ascii(texte_binaire):
    texte_ascii = []
    for i in range(len(texte_binaire)):
        texte_ascii.append(int(texte_binaire[i],2))
    return texte_ascii

# print(binaire_to_ascii(ascii_to_binaire(convertir_texte_ascii("lettres_persanes.txt"))))

# print(ascii_to_texte(binaire_to_ascii(ascii_to_binaire(convertir_texte_ascii("lettres_persanes.txt")))))







key = 1011110101

def chiffrer_fichier(fichier, key):
    texte_ascii = convertir_fichier_ascii(fichier)
    texte_binaire = ascii_to_binaire(texte_ascii)
    texte_chiffre = []
    for i in range(len(texte_binaire)):
        texte_chiffre.append(encrypt(key, int(texte_binaire[i])))
    return ascii_to_texte(texte_chiffre)



def chiffrer_texte(texte, key):
    texte_ascii = texte_to_ascii(texte)
    texte_binaire = ascii_to_binaire(texte_ascii)

    texte_chiffre = []
    for i in range(len(texte_binaire)):
        texte_chiffre.append(encrypt(key, int(texte_binaire[i])))

    return texte_chiffre

text_chiffre = chiffrer_texte("Bonjour", key)


def dechiffrer_texte(texte_chiffre, key):

    texte_binaire = ascii_to_binaire(text_chiffre)
    texte_dechiffre = []
    for i in range(len(texte_binaire)):
        texte_dechiffre.append(decrypt(key, int(texte_binaire[i])))
    return texte_dechiffre

print(dechiffrer_texte(text_chiffre, key))
print(ascii_to_texte(dechiffrer_texte(text_chiffre, key)))


def fichier_chiffre(fichier_source, key, fichier_destination):
    texte_chiffre = chiffrer_fichier(fichier_source, key)
    with open(fichier_destination, 'w') as f:
        f.write(texte_chiffre)


# fichier_chiffre("lettres_persanes.txt", key, "lettres_persanes_chiffre.txt")

def dechiffrer_fichier(texte_chiffre, key):
    """
    Déchiffre un texte chiffré à l'aide d'une clé donnée.

    Args:
        texte_chiffre (str): Le texte chiffré à déchiffrer.
        key (int): La clé de déchiffrement.

    Returns:
        str: Le texte déchiffré.
    """
    texte_ascii = convertir_fichier_ascii(texte_chiffre)
    texte_binaire = ascii_to_binaire(texte_ascii)
    texte_dechiffre = []
    for i in range(len(texte_binaire)):
        texte_dechiffre.append(decrypt(key, int(texte_binaire[i])))
    return ascii_to_texte(texte_dechiffre)



# texte = chiffrer_fichier("lettres_persanes.txt", key)
# print(texte)
# print(dechiffrer_fichier("lettres_persanes_chiffre.txt", key))
