# Rendu 2 : SAE CRYPTO

## Auteurs

Groupe : 1A
- Roshan GNANESWARAN
- Quentin DROUCHEAU


## Partie 1 : premières tentatives

### 1.1

Eve aura du mal à trouver la clé de chiffrement car nous sommes sur un chiffrement asymétrique ce qui garanti une sécurité plus importante. De plus, Eve ne peut pas intercepter les messages car ils sont chiffrés.

### 1.2

Il est peu sécurisé car selon la documentation il faudrait en moyenne 512 essai pour en arriver à bout. Ce qui est très court pour un ordinateur.

### 1.3

Il est un peu plus sécurisé que le précédent car il nécessite à Eve de connaitre une clé supplémentaire "k2". Cependant, il est toujours possible de le casser en 512 essais.


## Partie 2: Un peu d’aide

### 2.1

Passer de l'utilisation d'un algorithme de chiffrement comme DES à AES avec des clés de 256 bits est en effet une amélioration majeure en termes de sécurité. AES (Advanced Encryption Standard) est considéré comme très sécurisé et est largement utilisé dans de nombreux systèmes cryptographiques. L'augmentation de la taille de la clé de 56 bits (pour DES) à 256 bits (pour AES) offre une sécurité considérablement renforcée. En raison de sa robustesse et de sa résistance accrue aux attaques par force brute, le passage à AES est un progrès positif en matière de sécurité


### 2.2

Nous avions rencontrés un problème sur nos machines pour l'utilisation de la libraire Crypto.cypher la libriairie reliée à la librairie pycryptodome. Nous avons donc decidé de faires nos propres fonctions de chiffrement et de déchiffrement pour AES.

Lorsque nous comparons la vitesse d'exécution du dechiffrage et du chiffrement entre AES et SDES. On remarque que AES est beaucoup plus rapide que SDES. Cela est dû au fait que AES est un algorithme de chiffrement symétrique et SDES est un algorithme de chiffrement asymétrique.


En ce qui concerne l'estimation du temps de cassage d'AES sur mon ordinateur, voici un exemple d'estimation :

Configuration du Macbook Air 2020 :

CPU : M1 Apple Silicon (8 cœurs)
Pour l'estimation du temps de cassage d'AES-256 :

La complexité de temps pour casser AES-256 est de 2^256, ce qui est extrêmement élevé.
Supposons une vitesse de traitement de 2^40 (environ 1 téraopération par seconde) pour le cassage astucieux.
Calcul :
Temps nécessaire = (2^256) / (2^40) = 2^216 secondes

En convertissant cela en une unité de temps plus compréhensible :
2^216 secondes ≈ 7,4 x 10^49 années

Cette estimation montre que même avec une vitesse de calcul extrêmement rapide, le temps nécessaire pour casser AES-256 est bien au-delà de la durée de vie de l'univers observable. Cela confirme la robustesse extrême d'AES-256 contre les attaques par force brute.

### 2.3

Effectivement, en dehors des attaques par force brute, il existe plusieurs autres types d'attaques cryptographiques, dont voici quelques exemples :

Attaques par analyse de la fréquence : Cette méthode est couramment utilisée pour casser des systèmes de chiffrement par substitution, tels que le chiffre de César ou les chiffres mono-alphabétiques. Elle consiste à analyser la fréquence d'apparition des lettres ou des symboles dans un texte chiffré. Les lettres les plus fréquentes dans une langue donnée peuvent être utilisées pour déduire les correspondances avec les lettres les plus courantes de cette langue, permettant ainsi de deviner le message chiffré.


Par la suite nous avions eu deux images d'apparences identiques cependant en ayant remarqué l'extension  .bmp. Nous avions émis l'hypthèse que les deux images étaient différéntes de part leurs code hexa comme nous avions pu l'expermienter dans un autre projet. Nous avions donc utilisées la libraire Pillow afin de pouvoir lire les images et les comparer. Nous avions donc pu remarquer que les deux images étaient bien différentes. Lorsque nous nous basions sur le code binaire des couleurs RGB nous avions eu une différence dans la seconde image par rapport à la première. Nous avions donc ajoutés le dernier bit de la couleur RGB pour constituer une clée de 64 bits. 

Ce qui nous donne : b"1110011101101101001100010011111110010010101110011001000001001100"

et pour la passé d'une longueur de 64 bits à 256 bits nous avions juste à la multiplier par 4.

key = b"1110011101101101001100010011111110010010101110011001000001001100" * 4


## Partie 3: Analyse des messages

En utilisant les conseils de M Robot, nous avions pu parcourir le fichier cap grâce au moduel scapy. Nous avions pu remarquer que le fichier contenait 3 paquets. Nous avions donc pu extraire les données de ces paquets et les afficher en hexa. Nous avions pu remarquer que les données étaient chiffrées avec AES. Nous avions donc pu utiliser la clé que nous avions trouvé dans la partie précédente pour déchiffrer les données. 

Cependant nous n'avions pas réussi à identifier qui était Alice ou Bob. Donc nous n'avions pas pu trouver leurs messages dans la trame réseau.



## Partie 4: Un peu de recul

### 4.1

Utiliser toujours la meme clé n'est pas une bonne pratique, cela augmente le risque d'avoir une clé dévoilé, il faudrait plutot utiliser une clé qui est temporaire

### 4.2

Protocole inspiré de PlutotBonneConfidentialité : PlutotBonneConfidentialité peut être inspiré du protocole SSL/TLS, qui implémente un échange de clés asymétriques, notamment la partie de certification des clés absente dans PlutotBonneConfidentialité.

### 4.3

Utilisé un protocole aussi performant peut etre utilisé aussi pour sécuriser des données sensible tel que des transactions en ligne ou encore des communications gouvernementales

### 4.4

Dans les messageries utilisant le chiffrement de bout en bout on peut retrouver :
 - WhatsApp 
 - Signal 

 Les deux applications utilisent le protocole Signal qui permet de chiffrer de bout en bout des appels vocaux et video ainsi que des conversations par messagerie. Il utilise une paire de clés asymétriques et un échange de clés Diffie-Hellman

 sources : 
 https://faq.whatsapp.com/820124435853543/?locale=fr_FR
 https://fr.wikipedia.org/wiki/Signal_Protocol

### 4.5

Avoir la possibilité de déchiffrer les communications pour les fournisseurs de service numériques possèdent des avantages et des inconvénients: 

Avantage : 

- Permet aux forces de l'ordre d'enqueter plus facilement

Inconvénient:

- Avoir la possibilité de déchiffrer les communications peut causer des problèmes de sécurité car des personnes malveillantes peuvent essayer de déchiffrer les communications
- atteinte à la vie privée 



## Execution du code 

Dans ce zip vous retrouverez des dossiers correspondant à chaque partie du rendu. Dans ces fichiers nous avions un main.py qui permet d'executer le code.

## Répartition du travail

Partie 1 : Quentin DROUCHEAU / Roshan GNANESWARAN
Partie 2 : Roshan GNANESWARAN
Partie 3 : Quentin DROUCHEAU / Roshan GNANESWARAN
Partie 4 : Quentin DROUCHEAU

Confection du rapport : Quentin DROUCHEAU / Roshan GNANESWARAN