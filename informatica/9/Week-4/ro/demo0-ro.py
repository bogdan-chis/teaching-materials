# Citirea unui text
nume = input("Cum te cheamă? ")
print("Salut,", nume, "!")

# Citirea unui număr întreg (necesită conversie cu int)
an_nastere_str = input("În ce an te-ai născut? ")
an_nastere = int(an_nastere_str) 

# Varianta scurtă, folosită cel mai des (citire + conversie pe aceeași linie)
clasa = int(input("În ce clasă ești? "))

varsta_estimata = 2026 - an_nastere
print("Ai aproximativ", varsta_estimata, "ani și ești în clasa a", clasa)