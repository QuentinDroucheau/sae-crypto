from image_traitement import extraire_cle

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

message = "Bonjour, ceci est un message secret."
print(message)

encrypted_message = cryptage_aes(message, key)
print(encrypted_message)

decrypted_message = decrytpage_aes(encrypted_message, key)
print(decrypted_message)