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
    
    if A=={}: # noeud vide => creer etiquette lettre
        if seq[0]=='$':
            
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
            #traitement de fin de suffixe
            A['$']={}
            return A
        elif A[seq[0]]=={}:#etiquette existe vide
            # creer etiquette
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
            # traitement de fin de suffixe
            A['$']={}
            return A

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
    #TODO ne fonctionne pas erreur index range
    print " fonction ne fonctionne pas"
#    for i in range(1,len(seq)):
#        if seq[i] in A.keys() and i<len(seq):
#                
#            
#            if seq[0] in A:
#                __Ajout_Dolar_Prefixe(A[seq[0]], seq[1:])
#            else:
#            for lettre in A.key():
#                __Ajout_Dolar_Prefixe(A[lettre], seq[1:])
#    elif seq[0] in A:
#        A[seq[0]]={"$":{}}
        
        
            
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
    
    for i in range(1,len(seq)+1):
        N0=__Insert_Noeud_Successeurs__(A,seq[:i])
        __Insert_Suffixe__(N0,seq[:i])
    # ne fonctionne pas pour l'instant    
    __Ajout_Dolar_Prefixe(A,seq)

    print""
    aff_arbre_simple (A,0)
    print""

    
    
    
     # Affihe si le motif  appartient à l'arbre 

def is_motif(A,q,motif_bis):
    liste=[]
    test = q[len(motif_bis)]
    print test
    if len(q)==len(motif_bis):
        return true
    elif test not in A :
        if seq(motif_bis) !=0:
            motif_bis=""
        for lettre in A.key():
            print A[lettre]
            return is_motif(A[lettre], q, 'motif_bis') 
        return false
    else:
        print " on continue "+ test
        print A [test]
        return is_motif(A[test], q, 'motif_bis'+test)
    return false
        
        
#        if len(q)<len(motif_bis):
#            motif_bis=motif_bis[1:]
#                      
#            if 'a' in A:
#                is_motif(A,q,(motif_bis+'a'))
#            if 't' in A:
#                is_motif(A,q,(motif_bis+'t'))
#            if 'c' in A:
#                is_motif(A,q,(motif_bis+'c'))
#            if 'g' in A:
#                is_motif(A,q,(motif_bis+'g'))
#            
#        
#        elif len(q)>len(motif_bis):
#            if 'a' in A:
#                is_motif(A,q,(motif_bis+'a'))
#            if 't' in A:
#                is_motif(A,q,(motif_bis+'t'))
#            if 'c' in A:
#                is_motif(A,q,(motif_bis+'c'))
#            if 'g' in A:
#                is_motif(A,q,(motif_bis+'g'))
#                  
#        
#        
#        
#        if q==motif_bis:
#            print("Ok")  
#               

    
    
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
            
