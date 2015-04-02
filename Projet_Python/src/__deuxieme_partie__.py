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
    
def __Insert_Suffixe__(N0,seq):
    print N0
    print seq
    if 'suff' in N0:
        Fils =N0
        N0=N0['suff']
        if seq[-1] in Fils:#t existe chez le pere
            print"hello"
    else:
        N0[seq[-1]]={"suff":N0}
        
            
        
#    #print N0
#    if 'succ'
##    print Fils
#    if seq[-2] in Fils:
#        print " suffixe existe"
#    else:
#        print " suffixe n'existe pas"
#        __Insert_Noeud_Successeurs__(Fils,seq[-2]+"$")
#    if 'succ' in Fils:
#     print Fils
#     print N0
#    if __Is_Racine__(N0)!=True:# il existe un lien successeur = ce n'est pas une racine
#       if len(seq)>1: # on est pas a la derniere lettre
#            return A
#       else:
#        return "poul"
#    return A

def __Construire_Arbre__(seq):
    from __saisie__ import SaisieADN
    from __affichage__ import aff_arbre_simple , aff_suffixe
    """
    saisir une sequence S ecrite sur a,c,t et g
    ajoute un $
    construit l'arbre
    visualise l'arbre
    """
    
    #initialisation
    A=__Initialisation_Arbre()
    #N0 le noeud le plus profond
    N0=A
    for i in range(len(seq)+1):
        if i ==0:
            N0=__Insert_Noeud_Successeurs__(A,seq[i])
            #print N0
            #__Insert_Suffixe__(N0,seq[i])
        else:
            N0=__Insert_Noeud_Successeurs__(A,seq[0:i])
            #print N0
            #__Insert_Suffixe__(N0,seq[0:i])
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
#    print A
    return(A)
    
    
    
     # Affihe si le motif  appartient à l'arbre 

def is_motif(A,q,motif_bis,isit):
    if A!={} and q!='': 
        if len(q)<len(motif_bis):
            motif_bis=motif_bis[1:]
            if A['a']!={}:
                is_motif(A['a'],q,(motif_bis+'a'),isit)
            if A['t']!={}:
                is_motif(A['t'],q,(motif_bis+'t'),isit)
            if A['c']!={}:
                is_motif(A['c'],q,(motif_bis+'c'),isit)
            if A['g']!={}:
                is_motif(A['g'],q,(motif_bis+'g'),isit) 
          
        if len(q)>len(motif_bis):
            if A['a']!={}:
                is_motif(A['a'],q,(motif_bis+'a'),isit)
            if A['t']!={}:
                is_motif(A['t'],q,(motif_bis+'t'),isit)
            if A['c']!={}:
                is_motif(A['c'],q,(motif_bis+'c'),isit)
            if A['g']!={}:
                is_motif(A['g'],q,(motif_bis+'g'),isit) 

            
        if q!='' and q==motif_bis:
            isit+=1
            
    return (isit)
    
    
#    if A!={}and k>=0:
#        if motif!='' and motif==motif_bis:
#            print "¤ Nombres d'occurences du motif '",motif,"' dans la séquence : ",A['val']
#        # Récursivité qui construit les motifs
#        k-=1
#        if A['a']!={}:
#            is_motif(A['a'],motif,k,(motif_bis+'a'))
#        if A['t']!={}:
#            is_motif(A['t'],motif,k,(motif_bis+'t'))
#        if A['c']!={}:
#            is_motif(A['c'],motif,k,(motif_bis+'c'))
#        if A['g']!={}:
#            is_motif(A['g'],motif,k,(motif_bis+'g'))      
            
