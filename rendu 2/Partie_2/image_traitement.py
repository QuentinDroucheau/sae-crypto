import cv2

def extraire_cle(chemin_image):
    """
    Extrait une clé à partir de l'image spécifiée.

    Paramètres :
    - chemin_image (str) : Le chemin vers l'image à traiter.

    Retourne :
    - str : La clé extraite sous forme de chaîne binaire.
    """
    # Charger l'image
    image = cv2.imread(chemin_image)
    # Convertir l'image en mode RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Extraire la première ligne de l'image
    premiere_ligne = image[0]
    # Liste pour stocker les bits de la clé
    bits_cle = []

    # Parcourir les valeurs des pixels de la première ligne
    for valeur_pixel in premiere_ligne[:64]:
        # Convertir la valeur du pixel en binaire
        pixel_binaire = format(valeur_pixel[0], '08b') + format(valeur_pixel[1], '08b') + format(valeur_pixel[2], '08b')

        # Ajouter le dernier bit du pixel à la liste des bits de la clé
        bits_cle.append(pixel_binaire[-1])

    # Convertir la liste des bits de la clé en une chaîne binaire
    cle = ''.join(bits_cle)

    # Retourner la clé extraite
    return cle

