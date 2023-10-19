def garde_premiere_appariton(texte):
    """
    Retourne une chaîne de caractères contenant les caractères uniques de la chaîne d'entrée, dans l'ordre de leur première apparition.

    Args:
    - texte (str): La chaîne d'entrée à partir de laquelle extraire les caractères uniques.

    Returns:
    - alphabet_substitution (str): Une chaîne de caractères contenant les caractères uniques de la chaîne d'entrée, dans l'ordre de leur première apparition.
    """

    deja_vu = set()

    alphabet_substitution = ""

    for i in range(len(texte)):
        if texte[i] != " " and texte[i] not in deja_vu:
            alphabet_substitution += texte[i]
            deja_vu.add(texte[i])

    return alphabet_substitution

def dico_alphabet_substitution(texte):
    """
    Cette fonction prend une chaîne de caractères en entrée et 
    renvoie un dictionnaire qui associe chaque caractère de la chaîne d'entrée 
    à un caractère correspondant dans l'alphabet.

    Args:
    - texte (str): La chaîne de caractères à associer à l'alphabet.

    Returns:
    - dico_alphabet (dict): Un dictionnaire qui associe chaque caractère 
    de la chaîne d'entrée à un caractère correspondant dans l'alphabet.
    """

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dico_alphabet = dict()

    for i in range(len(texte)):
        dico_alphabet[texte[i]] = alphabet[i]

    return dico_alphabet


def substitution(texte, alphabet_substitution):
    """
    Déchiffre un texte chiffré par substitution avec un alphabet de substitution donné.

    Args:
        texte (str): Le texte à déchiffrer.
        alphabet_substitution (str): L'alphabet de substitution utilisé pour déchiffrer le texte.

    Returns:
        str: Le texte déchiffré.
    """

    resultat = ""

    for lettre in texte:
        if lettre.isalpha():
            resultat += alphabet_substitution[lettre]
        else:
            resultat += lettre

    return resultat

pangramme = "LE VIF ZEPHYR JUBILE SUR LES KUMQUATS DU CLOWN GRACIEUX"
alphabet_substitution = garde_premiere_appariton(pangramme)
dico_substitution = dico_alphabet_substitution(alphabet_substitution)
message_dechiffre = "EALOK, OKCT LOFX PLPSF! UF VKIF L ZKCASYA FTD: FUYXFEFDH"

print(substitution(message_dechiffre, dico_substitution))

# Result
# BRAVO, VOUS AVEZ GAGNE! LE CODE A FOURNIR EST: ELIZEBETH