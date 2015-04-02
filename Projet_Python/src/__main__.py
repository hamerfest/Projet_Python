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
        A={}
        
        # PARTIE A - ARBRE DES PREFIXES
        if Choix=="A":
            __affichage__.menu_arbre_pref()
            __affichage__.aff_seq(seq)
            __affichage__.aff_k(k)
            print("********************************************************************************\n")
            
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
                    print("********************************************************************************\n")
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
                    print("********************************************************************************\n")
                    continue
                    
                # Construction de l'arbe - Visualisation de l'arbre des préfixes
                ## Choix C = construction arbre
                elif Choix=="C":
                    if seq==None or k==None:
                        print("Une séquence et/ou un entier sont nécessaires pour construire l'arbre !")
                    else:
                        A=__premiere_partie_A__.construction_arbre(A,seq,k)
                        __affichage__.menu_arbre_pref()
                        __affichage__.aff_seq(seq)
                        __affichage__.aff_k(k)
                        print('¤ Arbre de préfixes:')
                        __affichage__.aff_arbre(A,0)
                        print("********************************************************************************\n")
                    continue
                
                # Construction de l'arbre - Utilisation de l'arbre
                ## Choix D = liste des préfixes et leurs occurences d'un arbre
                elif Choix=="D":
                    if seq==None or k==None or A=={}:
                        print("Un arbre est nécessaire pour extraire la liste des préfixes !")
                    else:
                        __affichage__.menu_arbre_pref()
                        __affichage__.aff_seq(seq)
                        __affichage__.aff_k(k)
                        print('¤ Liste des préfixes et leurs occurences:')
                        __affichage__.aff_pref(A,'',k)
                        print("********************************************************************************\n")
                    continue
                
                ## Choix E = occurences d'un motif (<k) dans un arbre  préfixe
                elif Choix=="E":
                    if seq==None or k==None or A=={}:
                        print("Un arbre est nécessaire pour extraire la liste des préfixes !")
                    else:
                        motif=__saisie__.SaisieADNBornee(0,k)
                        __affichage__.menu_arbre_pref()
                        __affichage__.aff_seq(seq)
                        __affichage__.aff_k(k)
                        __affichage__.aff_motif(A,motif,k,'')
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
