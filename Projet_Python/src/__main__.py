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
          
        # S�quence et entier k sans valeurs
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
                        A=__premiere_partie_A__.construction_arbre(A,seq,k)
                        __affichage__.aff_seq(seq)
                        __affichage__.aff_k(k)
                        print('� Arbre de pr�fixes:')
                        __affichage__.aff_arbre(A,0)
                        print("********************************************************************************\n")
                    continue
                
                # Construction de l'arbre - Utilisation de l'arbre
                ## Choix D = liste des pr�fixes et leurs occurences d'un arbre
                elif Choix=="D":
                    if seq==None or k==None or A=={}:
                        print("Un arbre est n�cessaire pour extraire la liste des pr�fixes !")
                    else:
                        __affichage__.aff_seq(seq)
                        __affichage__.aff_k(k)
                        print('� Liste des pr�fixes et leurs occurences:')
                        __affichage__.aff_pref(A,'',k)
                        print("********************************************************************************\n")
                    continue
                
                ## Choix E = occurences d'un motif (<k) dans un arbre  pr�fixe
                elif Choix=="E":
                    if seq==None or k==None or A=={}:
                        print("Un arbre est n�cessaire pour extraire la liste des pr�fixes !")
                    else:
                        motif=__saisie__.SaisieADNBornee(0,k)
                        __affichage__.aff_seq(seq)
                        __affichage__.aff_k(k)
                        __affichage__.aff_motif(A,motif,k,'')
                        print("********************************************************************************\n")
                    continue 
                    
                # Autres choix du menu
                elif Choix=="Q":
                    Menu()
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
            print("""
    A => Constuire un arbre suffixe
    B => Saisir une cha�ne et d�terminer si c'est un motif ou un suffixe de X
    Q => Quitter
    """)
            while True:
                Choix=raw_input("S�lectionner un menu : ")
                Choix=Choix.upper()
                print ("Valeur saisie : "+Choix)
            
                from __deuxieme_partie__ import __Construire_Arbre__,is_motif
                from __saisie__ import SaisieADN,SaisieADNBornee

                if Choix=="A":
                        print "Saisissez une sequence nucleique : "
                        seq=SaisieADN()
                        seq=seq+"$"
                        A=__Construire_Arbre__(seq)
                        print(A)
                        continue
                ## Exploitation de l'arbre
                # Choix B = D�terminer si la cha�ne donn�e q est un motif de S ou un suffixe de S
                elif Choix=="B": 
                    if seq==None:
                        print "Il vous faut construire un arbre avant d'effectuer cette action."
                        continue
                    else:
                        print ("� S�quence enregistr�e :"+seq)
                        print "Saisissez une chaine : "
                        q=SaisieADNBornee(0,(len(seq)))
                        is_motif(A,q,'')
#                        if m>0 :
#                            print("� '"+q+"'  est un motif de S: '"+seq+"'")
#                            print("******c**************************************************************************\n")
#                        elif m<0:
#                            print("� '"+q+"'  n'est PAS un motif de S: '"+seq+"'")
#                            print("********************************************************************************\n")

                ## Autres choix du menu
                elif Choix=="Q":
                    Menu()
                    break
                else:
                    print("Erreur de saisie!! RECOMMENCEZ ")
                    continue 


        elif Choix=="Q":
            print("Au revoir")    
            exit()
            break
        else:
            print("Erreur de saisie!! RECOMMENCEZ ")
            continue
    exit()
            
Menu()
