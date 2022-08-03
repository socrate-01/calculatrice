from curses.ascii import isdigit


nom = input("Veuiller entrer vôtre prénom: ")
print("Bienvenu : "+nom.capitalize())
print("les opérations possibles sont: + , - , * , / ")

nombre_1 = input("Veuiller entrer un premier nombre : ")
if(nombre_1.isdigit()):
    nombre_1 = int(nombre_1)
else:
    print("Vous n'avez pas renseigné de nombre")

nombre_2 = input("Veuiller entrer un deuxième nombre : ")
if(nombre_2.isdigit()):
    nombre_2 = int(nombre_2)
else:
    print("Vous n'avez pas renseigné de nombre")


operation = input("Quelle opération voulez vous effectuer? ")
if (operation=="+"):
    resultat = nombre_1+nombre_2
    print(nombre_1," + ",nombre_2," = ",resultat)

if (operation=="-"):
    resultat = nombre_1-nombre_2
    print(nombre_1," - ",nombre_2," = ",resultat)

if (operation=="*"):
    resultat = nombre_1*nombre_2
    print(nombre_1," * ",nombre_2," = ",resultat)

if (operation=="/"):
    if(nombre_2!=0):
         resultat = nombre_1/nombre_2
         print(nombre_1," / ",nombre_2," = ",resultat)
    else:
        print("Impossible de diviser un nombre par zéro...")
   
