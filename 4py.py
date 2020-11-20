from fractions import Fraction
l=int(input("numaratorul primei fractii "))
m=int(input("numitorul primei fractii "))
n=int(input("numaratorul la a doua fractie "))
o=int(input("numitorul la a 2 fractie "))
s=Fraction(l, m) + Fraction(n, o)
p=Fraction(l, m) * Fraction(n, o)
print(f"l) suma este {s}, m) produsul este {p}")
