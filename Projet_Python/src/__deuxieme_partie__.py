#-*- coding:Utf-8 -*-
#
# Arbre de suffixes
#

def __Initialisation_Arbre():
    """
    Initialisation de l'arbre a une seule racine
    est toujours marquee
    """
    A={}
    return A

def __Insert_Noeud_Successeurs__(A,seq):
    """
    Cree les liens succeseurs 
    depuis le noeud/racine A selon la sequence seq
    seq doit finir par $
    """
    if A is None: #pas de noeud
        print "¤ Creation de l'abre ..."
        if len(seq)>0: # il reste des lettre
            A= __Initialisation_Arbre()
            __Insert_Noeud_Successeurs__(A, seq)
            
    elif A=={}: # noeud vide => creer etiquette lettre
        if len(seq)>0 and seq[0]!='$':#il reste des lettres autres que $
            A[seq[0]]={}
            # print str(A[seq[0]])+" :"+str(seq[0])+"reste =>"+str(seq[1:])
            __Insert_Noeud_Successeurs__(A[seq[0]], seq[1:])#on passe à la lettre suivante
        elif seq[0]=='$':
            #TODO traitement de fin de suffixe
            A['$']={}
            print "¤ Arbre construit. "
    elif seq[0] in A  :# Il existe un etiquette "lettre"
        if seq[0]=='$':# Fin de sequence
            #TODO traitement de fin de suffixe
            print "¤ Arbre construit ."
        elif A[seq[0]]=={}:#etiquette existe vide
            #TODO creer etiquette
            if len(seq[1:])>0: # il reste des lettres après
                __Insert_Noeud_Successeurs__(A[seq[0]], seq[1:])
        else: #etiquette existe non vide
            if len(seq[1:])>0: # il reste des lettres après
                __Insert_Noeud_Successeurs__(A[seq[0]], seq[1:])
    else :# il n'existe pas d'etiquette
        A[seq[0]]={}
        __Insert_Noeud_Successeurs__(A, seq)
    return A
def __Noeud_Profond(A): 
    return A
def __Construire_Arbre__():
    from __saisie__ import SaisieADN
    from __affichage__ import aff_arbre_simple
    """
    saisir une sequence S ecrite sur a,c,t et g
    ajoute un $
    construit l'arbre
    visualise l'arbre
    """
    print "Saisissez une sequence nucleique : "
    seq=SaisieADN()
    seq=seq+"$"
    A=__Insert_Noeud_Successeurs__(None,seq)
    aff_arbre_simple (A,0)

    aff_arbre_simple (A,0)
    
