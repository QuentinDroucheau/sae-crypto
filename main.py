alphabet = dict()
i = 0
for lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    alphabet[lettre] = i
    i += 1

texte = "BDQE PG OTQYUZ EQ OMOTQ GZ FDQEAD MOODAOTQ M GZ MDNDQ FAGF DQOAGHQDF P AD ZQ ZQSXUSQ BME XM VQGZQ BAGOQ RQGUXXG SDMZP QEF EAZ EQODQF YMXSDQ EM FMUXXQ YQZGQ DAZPQE QF OAXADQQE EAZF XQE NMUQE CG'UX BADFQ MZUEQQE QF EGODQQE, XQGDE EMHQGDE EAZF RADFQE YMUE MFFQZFUAZ M ZQ BME XQE ODACGQD, YQYQ EU XM RMUY FUDMUXXQ FQE QZFDMUXXQE, QZ MGOGZ OME FG ZQ PAUE EGOOAYNQD"

def cesar(cle, texte):
    global alphabet
    texte_decode = ""
    for lettre in texte:
        if lettre in alphabet.keys():
            nb = (alphabet.get(lettre) + cle) % 26
            
            for k in alphabet.keys():
                if alphabet[k] == nb:
                    texte_decode += k
        else:
            texte_decode += " "
    return texte_decode


print(cesar(14, texte))
