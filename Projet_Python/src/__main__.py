# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Gphy"
__date__ = "mars 2015"


#Menu Principal et gestion des choix
def menu():
    print("********************************************************************************")
    print("                                      MENU")
    print("********************************************************************************\n")
    print ("""
    A => Arbre des prefixes
    B => Recherche de motifs repetes
    ....
    Q => Quitter
    """)
    while True:
        Choix=raw_input("Selectionner un menu : ")
        Choix=Choix.upper()
        print ("Valeur Saisie : "+Choix)
        if Choix=="A":
            print("********************************************************************************")
            print("                              ARBRE DES PREFIXES")
            print("********************************************************************************\n")
            
        elif Choix=="B":
            print("********************************************************************************")
            print("                         RECHERCHE DES MOTIFS REPETES")
            print("********************************************************************************\n") 
        elif Choix=="Q":
            print("Au revoir")    
            exit()
            break
        else:
            print("Erreur de saisie!! RECOMMENCEZ ")
            continue
            
            
menu()