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
    Cree une etiquette si le lien n'existe pas
    depuis le noeud/racine A selon la sequence seq
    retourne le noeud le plus profond
    """
    #TODO vérifier qu'il a tout les cas possible et non des supperflus
    print" Sequence :"+seq
#    if A is None: #pas de noeud
#        print "¤ Creation de l'abre ..."
#        if len(seq)>0: # il reste des lettre
#            A= __Initialisation_Arbre()
#            __Insert_Noeud_Successeurs__(A, seq)
    if A=={}: # noeud vide => creer etiquette lettre
        if len(seq)==1 :#seq est de 1
            A[seq[0]]={} # cree etiquette
            return A #nd le plus profond
        elif len(seq)>1 and seq[0]!='$':#il reste des lettres autres que $
            A[seq[0]]={}           
            __Insert_Noeud_Successeurs__(A[seq[0]], seq[1:])#on passe à la lettre suivante
        elif seq[0]=='$':
            #TODO traitement de fin de suffixe
            A['$']={}
            return A

    elif seq[0] in A  :# Il existe un etiquette de la premiere lettre
        if seq[0]=='$':# Fin de sequence
            #TODO traitement de fin de suffixe
            A['$']={}
            return A
            print "¤ Arbre construit ."
        elif A[seq[0]]=={}:#etiquette existe vide
            #TODO creer etiquette
            if len(seq[1:])>0: # il reste des lettres après
                __Insert_Noeud_Successeurs__(A[seq[0]], seq[1:])#on passe à la lettre suivante
            else:
                return A
        else: #etiquette existe non vide
            if len(seq[1:])>0: # il reste des lettres après
                __Insert_Noeud_Successeurs__(A[seq[0]], seq[1:])
    else :# il n'existe pas d'etiquette
        if len(seq)==1 :#seq est de 1
            A[seq[0]]={} # cree etiquette
            return A #nd le plus profond
        elif len(seq)>1 and seq[0]!='$':#il reste des lettres autres que $
            A[seq[0]]={}           
            __Insert_Noeud_Successeurs__(A[seq[0]], seq[1:])#on passe à la lettre suivante
        else :
            #TODO traitement de fin de suffixe
            A['$']={}
            return A

def __Noeud_Profond__(A,seq):
    """
    Retourne le noeud le plus profond de seq -1 hors le $
    """
    # en gros moins la derniere lettre ==>seq[:-3]
    if len(seq)>2:
        return __Noeud_Profond__(A[seq[0]],seq[1:])
    else:
        return A
def __Is_Racine__(A):
    """
    Test si c'est une racine ==> return true sinon false
    """
    if 'succ' in A:
        return False
    else:
        return True
    
def __Insert_Suffixe__(A,seq):
    N0=__Noeud_Profond__(A,seq)
    #print N0
    Fils=N0['succ']
#    print Fils
    if seq[-2] in Fils:
        print " suffixe existe"
    else:
        print " suffixe n'existe pas"
        __Insert_Noeud_Successeurs__(Fils,seq[-2]+"$")
#    if 'succ' in Fils:
#     print Fils
#     print N0
#    if __Is_Racine__(N0)!=True:# il existe un lien successeur = ce n'est pas une racine
#       if len(seq)>1: # on est pas a la derniere lettre
#            return A
#       else:
#        return "poul"
#    return A


def __Construire_Arbre__():
    from __saisie__ import SaisieADN
    from __affichage__ import aff_arbre_simple , aff_suffixe
    """
    saisir une sequence S ecrite sur a,c,t et g
    ajoute un $
    construit l'arbre
    visualise l'arbre
    """
    print "Saisissez une sequence nucleique : "
    seq=SaisieADN()
    seq=seq+"$"
    #initialisation
    A=__Initialisation_Arbre()
    print A
    N0=A
    print N0
    print seq
    for i in range(len(seq)):
        print i
        if i ==0:
            N0=__Insert_Noeud_Successeurs__(A,seq[i])
        else:
            N0=__Insert_Noeud_Successeurs__(A,seq[0:i])
    #A=__Insert_Noeud_Successeurs__(A,"atcgt$")
#    aff_arbre_simple (A,0)
#    print""
#    print"\n" # retour à la ligne
#    print A
#    __Insert_Suffixe__(A, seq)
#    print A['a']
#    print"***"
#    print A['t']
#    print A
##    N0 =__Noeud_Profond__(A,seq)
##    print "\n"+str(prfd)
    print""
    aff_arbre_simple (A,0)
    print""
#    print __Is_Racine__(A['a'])
#    prf=__Noeud_Profond__(A,seq)
#    print prf
#    aff_suffixe(prf)
    print A