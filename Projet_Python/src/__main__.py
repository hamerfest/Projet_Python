#-*- coding:Utf-8 -*-


import __saisie__
import __affichage__
import __premiere_partie_A__

#Menu Principal et gestion des choix
def Menu():
    print("********************************************************************************")
    print("                               MENU PRINCIPAL")
    print("********************************************************************************\n")
    print ("""
    A => Arbre des prefixes
    B => Recherche de motifs repetes
    C => Arbre des suffixes
    Q => Quitter
    """)
    while True:
        Choix=raw_input("Selectionner un menu : ")
        Choix=Choix.upper()
        print ("Valeur Saisie : "+Choix)
          
        # Séquence et entier k sans valeurs
        seq= None
        k= None
        
        # PARTIE A - ARBRE DES PREFIXES
        if Choix=="A":
            __affichage__.menu_arbre_pref()
            __affichage__.aff_seq(seq)
            __affichage__.aff_k(k)
            while True:
                Choix=raw_input("Sélectionner un menu : ")
                Choix=Choix.upper()
                print ("Valeur saisie : "+Choix)
                
                # Construction de l'arbre - Entrée des valeurs
                ## Choix A = saisie séquence
                if Choix=="A":
                    seq= __saisie__.SaisieADN()
                    if k !=None:
                        if len(seq)<k:
                            print ('Séquence trop courte par rapport à votre entier !')
                            seq= None
                            
                    __affichage__.menu_arbre_pref()
                    __affichage__.aff_seq(seq)
                    __affichage__.aff_k(k)
                    continue
                
                ## Choix A = saisie entier k
                elif Choix=="B":
                    k= __saisie__.SaisieIntPositif()
                    if seq !=None:
                        if k>len(seq):
                            print ('Entier k trop grand par rapport à votre séquence !')
                            k= None
                            
                    __affichage__.menu_arbre_pref()
                    __affichage__.aff_seq(seq)
                    __affichage__.aff_k(k)
                    continue
                    
                # Construction de l'arbe - Visualisation de l'arbre des préfixes
                ## Choix C = construction arbre
                elif Choix=="C":
#                    if (seq is None) | (k is None):
#                        print("Il vous manque un entier et/ou une séquence pour construire un arbre ! ")
#                        continue
#                    
#                    else:
                        A={}
                        seq=('atcg')
                        A=__premiere_partie_A__.insertion_arbre(A,seq)
                        __affichage__.aff_arbre(A)
                
                # Autres choix du menu
                elif Choix=="Q":
                    Menu()
                    break
                else:
                    print("Erreur de saisie!! RECOMMENCEZ ")
                    continue    
            
        elif Choix=="B":
            print("********************************************************************************")
            print("                         RECHERCHE DES MOTIFS REPETES")
            print("********************************************************************************\n") 

            from __premiere_partie_B__ import __Creation_des_tables__ , __Utilisation_des_tables__
            L,L1,H,M=__Creation_des_tables__()
            __Utilisation_des_tables__(L,L1,H,M)
            
        elif Choix=="C":
            print("********************************************************************************")
            print("                         ARBRE DES SUFFIXES")
            print("********************************************************************************\n")
            import __deuxieme_partie__
            __deuxieme_partie__.__construire_arbre__()
        elif Choix=="Q":
            print("Au revoir")    
            exit()
            break
        else:
            print("Erreur de saisie!! RECOMMENCEZ ")
            continue
    exit()
            
Menu()