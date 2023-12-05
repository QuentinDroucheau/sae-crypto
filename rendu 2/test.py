from main import encrypt, decrypt

# Fonction pour chiffrer un texte
def chiffrer_texte(texte_clair, key):
    texte_ascii = [ord(c) for c in texte_clair]  # Conversion du texte en ASCII
    texte_chiffre = [encrypt(key, char) for char in texte_ascii]  # Chiffrement caractère par caractère
    return texte_chiffre

# Fonction pour déchiffrer un texte chiffré
def dechiffrer_texte(texte_chiffre, key):
    texte_dechiffre = [decrypt(key, char) for char in texte_chiffre]  # Déchiffrement caractère par caractère
    texte_clair = ''.join(chr(char) for char in texte_dechiffre)  # Conversion du texte ASCII déchiffré en texte
    return texte_clair

# Test de chiffrement et déchiffrement
def tester_chiffrement_dechiffrement():
    key = 0b1011110101  # Clé pour SDES
    texte = "Bonjour, ceci est un exemple de texte à chiffrer avec SDES."

    texte_chiffre = chiffrer_texte(texte, key)
    print("Texte chiffré:", texte_chiffre)

    texte_dechiffre = dechiffrer_texte(texte_chiffre, key)
    print("Texte déchiffré:", texte_dechiffre)

    # Vérification si le déchiffrement donne le texte clair original
    assert texte == texte_dechiffre, "Erreur : Le texte déchiffré ne correspond pas au texte clair original."

# Appel de la fonction de test
tester_chiffrement_dechiffrement()


# Convertir un fichier texte en une liste d'entiers ASCII
def convertir_fichier_ascii(fichier):
    with open(fichier, 'r') as f:
        texte = f.read()
    texte_ascii = [ord(c) for c in texte]
    return texte_ascii

# Convertir une liste d'entiers ASCII en texte
def ascii_to_texte(texte_ascii):
    texte = ''.join(chr(char) for char in texte_ascii)
    return texte

# Chiffrer un fichier texte
def chiffrer_fichier(fichier_source, fichier_destination, key):
    texte_ascii = convertir_fichier_ascii(fichier_source)
    texte_chiffre = [encrypt(key, char) for char in texte_ascii]

    with open(fichier_destination, 'w') as f:
        for char in texte_chiffre:
            f.write(chr(char))

# Déchiffrer un fichier texte chiffré
def dechiffrer_fichier(fichier_chiffre, fichier_destination, key):
    texte_chiffre = convertir_fichier_ascii(fichier_chiffre)
    texte_dechiffre = [decrypt(key, char) for char in texte_chiffre]

    with open(fichier_destination, 'w') as f:
        for char in texte_dechiffre:
            f.write(chr(char))

# Test de chiffrement et déchiffrement de fichiers
def tester_chiffrement_dechiffrement_fichiers():
    key = 0b1011110101  # Clé pour SDES
    fichier_source = "lettres_persanes.txt"
    fichier_chiffre = "lettres_persanes_chiffrer.txt"
    fichier_dechiffre = "lettres_persanes_dechiffrer.txt"

    # Chiffrement du fichier source
    chiffrer_fichier(fichier_source, fichier_chiffre, key)

    # Déchiffrement du fichier chiffré
    dechiffrer_fichier(fichier_chiffre, fichier_dechiffre, key)

   
# Appel de la fonction de test pour les fichiers
tester_chiffrement_dechiffrement_fichiers()
