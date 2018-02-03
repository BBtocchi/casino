import os
import sys
from random import randrange
from math import ceil

cagnotte = 100 
cagnotte = int(cagnotte)#on commence avec 100$
print (" début de la partie ..." , "vous avez 100$")



continuer_partie = True
while continuer_partie == True:  #on crée une boucle

 pari= input("pariez sur un nombre entre 0 et 50 : ")
 pari = int(pari) #création d'une variable pari, le joueur va pouvoir parier sur un nombre
 if pari > 50:
    print("tu ne peux pas pariez sur plus grand que 50")
    continue

 mise =input("maintenant, misez la somme que vous voulez : ")
 mise = int(mise) #création d'une variable mise, le joueur va pouvoir miser la somme voulue
 if mise > cagnotte :
    print("tu ne peux pas miser plus que ce que tu n'as")
    continue

 lancer = randrange(50)#on lance une boule au hazard
 lancer = int(lancer)


 
 if pari is lancer :  #si le joueur a trouver le bon nombre, il gagne 3X sa mise
    cagnotte = mise * 3
    print("bravo, vous avez désormais ", cagnotte ,"$")
  

 elif pari%2 == lancer%2:   #si il a pas trouvé le bon nombre mais la bonne couleur, il gagne 50% de sa mise
    cagnotte = cagnotte + (mise / 2)
    print("vous avez misez sur la bonne couleur! vous gagnez 50% de votre mise", "vous avez désormais ", cagnotte ," $")
    
    
 else:   #si il perd perd, il perd sa mise :)
    cagnotte = cagnotte - mise
    print("dommage, vous perdez votre mise, vous avez désormais ", cagnotte , " $")
    
  
        
 if cagnotte <= 0:
    print ("vous n'avez plus assez d'argent pour continuer, vous avez perdu.")
    #si la cagnotte tombe a 0, la partie s'arrete
    sys.exit(1)



   

os.system ("pause")
