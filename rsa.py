from Crypto.Util.number import inverse

# Basiswerte
p = 17
q = 19
# 17 * 19 = 323
n = p * q
phi = (p - 1) * (q - 1)

# Schlüsselgenerierung
e = 5
d = inverse(e, phi)
print("Öffentlicher Schlüssel: ({:d},{:d})".format(e, n))
print("Privater Schlüssel: ({:d},{:d})".format(d, n))

# Nachricht
nachricht = int(input("Beliebige Zahl zwischen 0 und 221 eintippen: "))
print("Message: ", nachricht)

# Verschlüsseln
cypher = pow(nachricht, e, n)
print("Cypher: ", cypher)

# Entschlüsseln
print("Decrypted cypher", str(pow(cypher, d, n)))

# Signieren
signature = pow(nachricht, d, n)
print("Signature: ", signature)

# Verifizieren
print("Decrypted signature: ", str(pow(signature, e, n)))
