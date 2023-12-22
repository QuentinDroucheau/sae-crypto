from scapy.all import *


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


fichier_cap = rdpcap("trace_sae.cap")
key = b"1110011101101101001100010011111110010010101110011001000001001100" * 4


def decryptage_packet(packet):

    # Récupération du message
    message = packet[Raw].load

    # Décryptage du message
    message_decrypte = decrytpage_aes(message, key)

    # Affichage du message décrypté
    print(message_decrypte)
   

for packet in fichier_cap:
    decrytpage_aes(packet.show(), key)