alphabet = dict()
i = 0
for lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    alphabet[lettre] = i
    i += 1



def chiffrement_cesar(texte, decalage):
    """
    Cette fonction prend en entrée un texte et un décalage et retourne le texte chiffré
    selon le chiffrement de César avec le décalage donné.

    Args:
    texte (str): Le texte à chiffrer.
   decalage (int): Le décalage à utiliser pour le chiffrement.

    Returns:
         str: Le texte chiffré.

    """
    resultat = ""
    for char in texte:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            resultat += chr((ord(char) - ascii_offset + decalage) % 26 + ascii_offset)
        else:
            resultat += char
    return resultat


def test_tous_les_decalage(texte):
    """
    Cette fonction prend en entrée un texte et affiche le texte chiffré avec tous les décalages possibles.

    Args:
        texte (str): Le texte à chiffrer.
    """
    for decalage in range(26):
        print(f"Texte chiffré avec un décalage de {decalage} : {chiffrement_cesar(texte, decalage)}")


# Exemple d'utilisation :
text = "BDQE PG OTQYUZ EQ OMOTQ GZ FDQEAD MOODAOTQ M GZ MDNDQ FAGF DQOAGHQDF P AD ZQ ZQSXUSQ BME XM VQGZQ BAGOQ RQGUXXG SDMZP QEF EAZ EQODQF YMXSDQ EM FMUXXQ YQZGQ DAZPQE QF OAXADQQE EAZF XQE NMUQE CG'UX BADFQ MZUEQQE QF EGODQQE, XQGDE EMHQGDE EAZF RADFQE YMUE MFFQZFUAZ M ZQ BME XQE ODACGQD, YQYQ EU XM RMUY FUDMUXXQ FQE QZFDMUXXQE, QZ MGOGZ OME FG ZQ PAUE EGOOAYNQD"

mini_texte = "BDQE PG OTQYUZ EQ OMOTQ GZ FDQEAD"

decalage = 14
encrypted_text = chiffrement_cesar(text, decalage)
test_tous_les_decalage(mini_texte)
print(f"Texte chiffré : {encrypted_text}")
