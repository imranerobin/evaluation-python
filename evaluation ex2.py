continuer=True
choix=0
durée=0
taillGO=0
taille_img=0

#while continuer =="true":

#continuer = input(f"Tapez 'o' pour continuer:  ")

print("Que voulez vous faire ? \n 1: Calculer la durée de stockage \n 2: Calculer l'espace de stockage \n 3: Quitter \n")
    
input(choix)

if choix==1:
    print("calcule de la durée de stockage : ")
    taillGO=input("Saisir la taille du disque dur en Go: ") 
    taille_img =input ("Saisir la taille de l'image en ko: ")
    durée={taillGO}*(1024*1024)/({taille_img}*25)
    print(f"la durée:  {durée}")

if choix==2:
    print("calcule de l'espace de stockage : ")
    durée =input("Saisir la durée en S: ")
    taille_img =input ("Saisir la taille de l'image en ko: ")
    taillGO =({taille_img}*25*{durée})/(1024*1024)
    print(f"l'espace:  {taillGO} Go")

if choix ==3:
      continuer=False
      print("Au revoir !")
else: 
    print("erreur veuillez resayer")
    


