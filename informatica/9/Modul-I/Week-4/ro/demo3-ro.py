'''
Cerință: Un taxi taxează o pornire fixă de $b$ lei și $a$ lei pentru fiecare kilometru parcurs. 
Un client a plătit la finalul cursei suma totală de $c$ lei. 

Să se scrie un program care calculează câți kilometri a parcurs clientul.
'''

# 1. DATE DE INTRARE
# Folosim float() pentru că sumele de bani și distanțele pot fi numere cu virgulă
b = float(input("Tariful de pornire (lei): "))
a = float(input("Tariful pe kilometru (lei): "))
c = float(input("Costul total al cursei (lei): "))

# 2. PRELUCRARE (Rezolvarea ecuației de gradul I)
# Extragem costul care corespunde doar distanței, scăzând pornirea
cost_distanta = c - b

# Aflăm distanța împărțind la tariful pe kilometru
x = cost_distanta / a

# 3. DATE DE IEȘIRE
print("Clientul a parcurs:", x, "kilometri.")