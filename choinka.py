rozmiar_p = int(input("Podaj n: "))
rozmiar_p_back = rozmiar_p
ile_czensci = int(input("Ile części: "))
wienksze_p = ile_czensci
rozmiar = 1
wienksze = 0
while wienksze < ile_czensci:
    while rozmiar_p+wienksze > 0:
        print("  "*(rozmiar_p+wienksze)+"  "*(wienksze_p-1), " @"*(rozmiar))
        rozmiar_p=rozmiar_p-1
        rozmiar+=2
    rozmiar = 1
    rozmiar_p = rozmiar_p_back
    wienksze+=1
    wienksze_p=wienksze_p-1