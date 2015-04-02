#-*- coding:Utf-8 -*-

import __saisie__
import __affichage__
import __premiere_partie_A__

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
          
        # S�quence et entier k sans valeurs
        seq= None
        k= None
        
        # PARTIE A - ARBRE DES PREFIXES
        if Choix=="A":
            __affichage__.menu_arbre_pref()
            __affichage__.aff_seq(seq)
            __affichage__.aff_k(k)
            print("********************************************************************************\n")
            
            while True:
                Choix=raw_input("S�lectionner un menu : ")
                Choix=Choix.upper()
                print ("Valeur saisie : "+Choix)
                
                # Construction de l'arbre - Entr�e des valeurs
                ## Choix A = saisie s�quence
                if Choix=="A":
                    seq= __saisie__.SaisieADN()
                    if k !=None:
                        if len(seq)<k:
                            print ('S�quence trop courte par rapport � votre entier !')
                            seq= None
                            
                    __affichage__.menu_arbre_pref()
                    __affichage__.aff_seq(seq)
                    __affichage__.aff_k(k)
                    print("********************************************************************************\n")
                    continue
                
                ## Choix A = saisie entier k
                elif Choix=="B":
                    k= __saisie__.SaisieIntPositif()
                    if seq !=None:
                        if k>len(seq):
                            print ('Entier k trop grand par rapport � votre s�quence !')
                            k= None
                            
                    __affichage__.menu_arbre_pref()
                    __affichage__.aff_seq(seq)
                    __affichage__.aff_k(k)
                    print("********************************************************************************\n")
                    continue
                    
                # Construction de l'arbe - Visualisation de l'arbre des pr�fixes
                ## Choix C = construction arbre
                elif Choix=="C":
                    if seq==None or k==None:
                        print("Une s�quence et/ou un entier sont n�cessaires pour construire l'arbre !")
                    else:
                        A={}
                        __affichage__.menu_arbre_pref()
                        __affichage__.aff_seq(seq)
                        __affichage__.aff_k(k)
                        print('� Arbre de pr�fixes:')
                        __affichage__.aff_arbre(__premiere_partie_A__.construction_arbre(A,seq,k),0)
                        print("********************************************************************************\n")
                    continue
                
                # Construction de l'arbre - Utilisation de l'arbre
                ## Choix D = liste des pr�fixes et leurs occurences sur une sequence /!\ UTILISE A NOUVEAU LE PARCOUR PREFIXE /!\
                elif Choix=="D":
                    if seq==None or k==None:
                        print("Une s�quence et/ou un entier sont n�cessaires pour construire l'arbre !")
                    else:
                        A={}
                        __affichage__.menu_arbre_pref()
                        __affichage__.aff_seq(seq)
                        __affichage__.aff_k(k)
                        print('� Liste des pr�fixes et leurs occurences:')
                        __affichage__.aff_pre(__premiere_partie_A__.liste_pref(seq,k))
                        print("********************************************************************************\n")
                    continue    
                    
                # Autres choix du menu
                elif Choix=="Q":
                    menu()
                    break
                else:
                    print("Erreur de saisie!! RECOMMENCEZ ")
                    continue    
    
    # PARTIE B - RECHERCHE DE MOTIFS REPETES - INDEXATION PAR TABLE DE HACHAGE
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