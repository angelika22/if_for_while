a=int(input("dati numarul a "))
b=int(input("dati numarul b "))
while a%b==0:
    a=a//b
if a==1:
    print("a este puterea lui b")
else:
    print("a nu este puterea lui b")