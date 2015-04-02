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
    
    if A=={}: # noeud vide => creer etiquette lettre
        if seq[0]=='$':
            #TODO traitement de fin de suffixe
            A['$']={}
            return A
        elif len(seq)==1 :#seq est de 1
            A[seq[0]]={} # cree etiquette
            return A #nd le plus profond
        else:#il reste des lettres autres que $
            A[seq[0]]={}           
            return __Insert_Noeud_Successeurs__(A[seq[0]], seq[1:])#on passe à la lettre suivante
    elif seq[0] in A  :# Il existe un etiquette de la premiere lettre
        if seq[0]=='$':# Fin de sequence
            #TODO traitement de fin de suffixe
            A['$']={}
            return A
        elif A[seq[0]]=={}:#etiquette existe vide
            #TODO creer etiquette
            if len(seq[1:])>0: # il reste des lettres après
                return __Insert_Noeud_Successeurs__(A[seq[0]], seq[1:])#on passe à la lettre suivante
            else:
                return A
        else: #etiquette existe non vide
            if len(seq[1:])>0: # il reste des lettres après
                return __Insert_Noeud_Successeurs__(A[seq[0]], seq[1:])
    else :# il n'existe pas d'etiquette
        if len(seq)==1 :#seq est de 1
            A[seq[0]]={} # cree etiquette
            return A #nd le plus profond
        elif len(seq)>1 and seq[0]!='$':#il reste des lettres autres que $
            A[seq[0]]={}           
            return __Insert_Noeud_Successeurs__(A[seq[0]], seq[1:])#on passe à la lettre suivante
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
    
def __Insert_Suffixe__(N0,seq):
    N=N0
    if 'suff' in N and seq[-1]!='$':
        Nprim=N['suff'] 
        Fils=N[seq[-1]]
        if 'suff' in Fils:
            print""
        else:
            if seq[-1] in Nprim:
                Filsprim=Nprim[seq[-1]]
            else:
                Nprim[seq[-1]]={}
                Filsprim=Nprim[seq[-1]]
            Fils['suff']=Filsprim
            N=Nprim
    else: # initialisation
        if len(seq)==1 and seq[0]!='$':
            N[seq[0]]={'suff':N}

def __Ajout_Dolar_Prefixe(A,seq):
    for i in range(len(seq)):
        #print seq[i:]
        print seq[i],
        print i
        if i+1<len(seq) and seq [i] in A and seq[i]!='$':
             __Ajout_Dolar_Prefixe(A, seq[i+1:])
            
        
        


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
    #N0 le noeud le plus profond
    N0=A
    
    for i in range(1,len(seq)+1):
        print seq[:i]
        N0=__Insert_Noeud_Successeurs__(A,seq[:i])
        __Insert_Suffixe__(N0,seq[:i])
    __Ajout_Dolar_Prefixe(A,seq)
    print A   
#    seq="attcg$"
#    for i in range(len(seq)+1):
#        if i ==0:
#            N0=__Insert_Noeud_Successeurs__(A,seq[i])
#            __Insert_Suffixe__(N0,seq)
#        else:
#            N0=__Insert_Noeud_Successeurs__(A,seq[0:i])
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
    return A