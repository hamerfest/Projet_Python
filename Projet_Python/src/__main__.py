# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.



#Menu Principal et gestion des choix
def Menu():
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
#            #sequence test
#            seq="accaccaccag"
#            #taille test
#            k=3
            import __premiere_partie_B__
#            #Creation L + Affichage
#            L = __premiere_partie_B__.__Creation_Liste_Taille__(seq,k)
#            L1=__premiere_partie_B__.__Creation_Liste_Taille_Base10__(L)
#            M=__premiere_partie_B__.__Initialisation_Table_M_(L1)
#            H=__premiere_partie_B__.__Initialisation_Table_H_(L)
#            H,M=__premiere_partie_B__.__Remplissage_M_H__(L1,H,M)
#            print M
#            print H
            L,L1,H,M=__premiere_partie_B__.__Creation_des_tables__()
            __premiere_partie_B__.__Utilisation_des_tables__(L,L1,H,M)
        elif Choix=="Q":
            print("Au revoir")    
            exit()
            break
        else:
            print("Erreur de saisie!! RECOMMENCEZ ")
            continue
            
            
Menu()