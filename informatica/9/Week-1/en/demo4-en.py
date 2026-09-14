# Problema: Se citesc lungimea și lățimea unui dreptunghi. Să se afle aria și perimetrul.

# 1. DATE DE INTRARE
L = int(input("Introdu lungimea dreptunghiului: "))
l = int(input("Introdu lățimea dreptunghiului: "))

# 2. PRELUCRARE (Calcule)
aria = L * l
perimetrul = 2 * (L + l)

# 3. DATE DE IEȘIRE
print("Aria dreptunghiului este:", aria)
print("Perimetrul dreptunghiului este:", perimetrul)