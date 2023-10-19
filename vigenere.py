alphabet = dict() # un dictionnaire afin d'avoir un alphabet avec comme clé les lettres et comme valeur leur position dans l'alphabet
i = 0
for lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    alphabet[lettre] = i
    i += 1

def dechiffrement_vigenere(cle, texte):
    """
    Déchiffre un chiffrement de Vigenère avec une clé donnée.

    Args:
        cle (str): La clé utilisée pour déchiffrer le texte.
        texte (str): Le texte à déchiffrer.

    Returns:
        str: Le texte déchiffré.
    """
    global alphabet
    texte_decode = ""
    i = 0
    for lettre in texte:
        if lettre in alphabet.keys():
            nb = (alphabet.get(lettre) - alphabet.get(cle[i])) % 26
            for k in alphabet.keys():
                if alphabet[k] == nb:
                    texte_decode += k
            i += 1
            if i == len(cle):
                i = 0
        else:
            texte_decode += lettre
    return texte_decode

def dechiffrer_fichier_vigenere(fichier, fichier_sortie):
    """
    Cette fonction prend en entrée un fichier et affiche le texte déchiffré avec tous les décalages possibles.

    Args:
        fichier (str): Le nom du fichier à déchiffrer.
        cle (int): La clé utilisée pour déchiffrer le texte.
        fichier_sortie (str): Le nom du fichier de sortie.
    """
    with open(fichier, "r") as f:
        texte = f.read()
    texte_decode = dechiffrement_vigenere("PANGRAMME", texte)
    with open(fichier_sortie, "w") as f:
        f.write(texte_decode)

# Tests

premiere_ligne = "AE IOW ZQBLNR WASIXQ WJR YKJ KGYUJAGY UU OXSLN TXRCUQYM"
print(dechiffrement_vigenere("PANGRAMME", premiere_ligne))

dechiffrer_fichier_vigenere("indice2_chiffre.txt", "indice2_dechiffre.txt")