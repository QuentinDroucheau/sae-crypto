alphabet = dict()
i = 0
for lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    alphabet[lettre] = i
    i += 1

texte = "BDQE PG OTQYUZ EQ OMOTQ GZ FDQEAD MOODAOTQ M GZ MDNDQ FAGF DQOAGHQDF P AD ZQ ZQSXUSQ BME XM VQGZQ BAGOQ RQGUXXG SDMZP QEF EAZ EQODQF YMXSDQ EM FMUXXQ YQZGQ DAZPQE QF OAXADQQE EAZF XQE NMUQE CG'UX BADFQ MZUEQQE QF EGODQQE, XQGDE EMHQGDE EAZF RADFQE YMUE MFFQZFUAZ M ZQ BME XQE ODACGQD, YQYQ EU XM RMUY FUDMUXXQ FQE QZFDMUXXQE, QZ MGOGZ OME FG ZQ PAUE EGOOAYNQD"
mini_texte = "BDQE PG OTQYUZ EQ OMOTQ GZ FDQEAD MOODAOTQ M"

def dechiffrement_cesar(cle, texte):
    """
    Déchiffre un chiffrement de César avec une clé donnée.

    Args:
        cle (int): La clé utilisée pour déchiffrer le texte.
        texte (str): Le texte à déchiffrer.

    Returns:
        str: Le texte déchiffré.
    """
    global alphabet  
    texte_decode = ""  
    for lettre in texte:
        if lettre in alphabet.keys():
            nb = (alphabet.get(lettre) + cle) % 26
            
            for k in alphabet.keys():
                if alphabet[k] == nb:
                    texte_decode += k
        else:
            texte_decode += lettre
    return texte_decode

def test_tous_les_decalage(texte):
    """
    Cette fonction prend en entrée un texte et affiche le texte chiffré avec tous les décalages possibles.

    Args:
        texte (str): Le texte à chiffrer.
    """
    for decalage in range(26):
        print(f"Texte chiffré avec un décalage de {decalage} : {dechiffrement_cesar(decalage, texte)}")

# test_tous_les_decalage(mini_texte)
# print("\n\n")
# print(dechiffrement_cesar(14, texte))


def dechiffrer_fichier_cesar(fichier, cle, fichier_sortie):
    """
    Cette fonction prend en entrée un fichier et affiche le texte déchiffré avec tous les décalages possibles.

    Args:
        fichier (str): Le nom du fichier à déchiffrer.
        cle (int): La clé utilisée pour déchiffrer le texte.
        fichier_sortie (str): Le nom du fichier de sortie.
    """
    with open(fichier, "r") as f:
        texte = f.read()
    texte_decode = dechiffrement_cesar(cle, texte)
    with open(fichier_sortie, "w") as f:
        f.write(texte_decode)


#dechiffrer_fichier_cesar("indice1_chiffre.txt", 14, "indice1_dechiffre.txt")


nouveau_message = "AE IOW ZQBLXR WASIXQ WJR YKJ KGYUJAGY UU OXSLN TXRCUQYM IY IRCTQ HPNF RR RQBIIIGOFN XQ WTCEKK DQ OIH MHXDUDQW BAYNVUDQYM NR MRRPQD SU CXVMUQV HOHLWLQ CYT LRY GRQYMTRRY RPBMVXTVUES QF EXNFO UEHAMAEM RV MQEWPGR IRCTQ HTREOVRQ XE HUOYKIFGXXOA"

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


print(dechiffrement_vigenere("PANGRAMME", nouveau_message))