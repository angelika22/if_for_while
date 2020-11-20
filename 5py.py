a=int(input("dati anul format din patru cifre: "))
a=a-2000
if (a%12==1):
    print("esti anul sarpelui")
elif (a%12==2):
    print("esti anul calului")
elif (a%12==3):
    print("esti anul oaiei")
elif (a%12==4):
    print("esti anul maimutei")
elif (a%12==5):
    print("esti anul cocosului")
elif (a%12==6):
    print("esti anulciinelui")
elif (a%12==7):
    print("esti anul porcului") 
elif (a%12==8):
    print("esti anul sobolanului")
elif (a%12==9):
    print("esti anul boului")
elif (a%12==10):
    print("esti anul tigrului")
elif (a%12==11):
    print("esti anul iepurelui")
elif (a%12==0):
    print("esti anul dragonului")
else:
    print("eroare")