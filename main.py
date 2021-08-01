import os
from fonction import dictionnaire, mystere


motmystere = dictionnaire()
motcache = mystere(motmystere)
motmystere = list(motmystere)
motcache = list(motcache)
taille = len(motmystere)
occurence = 0
essai = 7
fin = True

print(motmystere)
print(motcache)

while fin == True:
    saisie = input("\nVeuillez saisie une lettre : ")
    occurence = 0
    
    for i in range(taille):
        j = i
        if saisie == motmystere[i] :
            motcache[j] = saisie
            occurence = occurence + 1
        else: 
            pass

    if occurence == 0:
        print ("raté\n")
        essai = essai - 1 
    else:
        pass

    if essai > 0
        pass
    elif essai == 0:
        print("tu as perdu !")
        fin == False
        
    print(f"\nil te reste {essai} essais.\n")
    print(str(motcache))
