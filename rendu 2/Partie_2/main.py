import time
from image_traitement import extraire_cle
import time

def fichier_to_texte(fichier):
    with open(fichier, 'r') as f:
        texte = f.read()
    return texte

def cryptage_aes(message, key):
    """
    Crypte le message spécifié avec la clé spécifiée en utilisant l'algorithme AES.

    Paramètres :
    - message (str) : Le message à crypter.
    - key (str) : La clé à utiliser pour le cryptage.

    Retourne :
    - str : Le message crypté.
    """

    # Initialiser la variable pour stocker le message crypté
    message_crypte = ""

    # Parcourir les caractères du message
    for i in range(len(message)):
        # Convertir le caractère en binaire
        caractere_binaire = format(ord(message[i]), '08b')

        # Parcourir les bits du caractère binaire
        for j in range(len(caractere_binaire)):
            # Crypter le bit du caractère avec le bit correspondant de la clé
            bit_crypte = str(int(caractere_binaire[j]) ^ int(key[j]))

            # Ajouter le bit crypté au message crypté
            message_crypte += bit_crypte

    # Retourner le message crypté
    return message_crypte


def decrytpage_aes(message,key):
    """
    Décrypte le message spécifié avec la clé spécifiée en utilisant l'algorithme AES.

    Paramètres :
    - message (str) : Le message à décrypter.
    - key (str) : La clé à utiliser pour le décryptage.

    Retourne :
    - str : Le message décrypté.
    """

    # Initialiser la variable pour stocker le message décrypté
    message_decrypte = ""

    # Parcourir les caractères du message
    for i in range(len(message) // 8):
        # Initialiser la variable pour stocker le caractère en binaire
        caractere_binaire = ""

        # Parcourir les bits du caractère
        for j in range(8):
            # Décrypter le bit du caractère avec le bit correspondant de la clé
            bit_decrypte = str(int(message[i * 8 + j]) ^ int(key[j]))

            # Ajouter le bit décrypté au caractère binaire
            caractere_binaire += bit_decrypte

        # Convertir le caractère binaire en caractère ASCII
        caractere_ascii = chr(int(caractere_binaire, 2))

        # Ajouter le caractère ASCII au message décrypté
        message_decrypte += caractere_ascii

    # Retourner le message décrypté
    return message_decrypte


key = extraire_cle("rossignol2.bmp")
print(key)

message = fichier_to_texte("../Partie1/arsene_lupin_extrait.txt")

start_time = time.time()
crypt = cryptage_aes(message, key)
end_time = time.time()
execution_time = end_time - start_time
print("Temps d'exécution pour le fichier arsene_lupin_extrait.txt :", execution_time, "secondes")
print(crypt)

start_time = time.time()
print(decrytpage_aes(crypt, key))
end_time = time.time()
execution_time = end_time - start_time
print("Temps d'exécution pour le décryptage du fichier arsene_lupin_extrait.txt :", execution_time, "secondes")

message = fichier_to_texte("../Partie1/arsene_lupin_extrait.txt")
start_time = time.time()
crypt = cryptage_aes(message, key)
end_time = time.time()
execution_time = end_time - start_time
print("Temps d'exécution pour le deuxième cryptage du fichier arsene_lupin_extrait.txt :", execution_time, "secondes")
print(crypt)

start_time = time.time()
print(decrytpage_aes(crypt, key))
end_time = time.time()
execution_time = end_time - start_time
print("Temps d'exécution pour le deuxième décryptage du fichier arsene_lupin_extrait.txt :", execution_time, "secondes")

message2 = fichier_to_texte("../Partie1/lettres_persanes.txt")
start_time = time.time()
crypt2 = cryptage_aes(message2, key)
end_time = time.time()
execution_time = end_time - start_time
print("Temps d'exécution pour le cryptage du fichier lettres_persanes.txt :", execution_time, "secondes")
print(crypt2)

start_time = time.time()
print(decrytpage_aes(crypt2, key))
end_time = time.time()
execution_time = end_time - start_time
print("Temps d'exécution pour le décryptage du fichier lettres_persanes.txt :", execution_time, "secondes")
