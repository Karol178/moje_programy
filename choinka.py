wielkosc = int(input("Podaj n: "))
wielkosc_back = wielkosc
ile_czensci = int(input("Ile części: "))
choinka = 1
wienksze = 0
while wienksze < ile_czensci:
    while wielkosc > 0:
        print("  "*(wielkosc+wienksze), " @"*(choinka+wienksze))
        wielkosc=wielkosc-1
        choinka+=2
    choinka = 1
    wielkosc = wielkosc_back
    wienksze+=1  
