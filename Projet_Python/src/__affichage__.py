#-*- coding:Utf-8 -*-

def menu_arbre_pref():
    print("********************************************************************************")
    print("                              ARBRE DES PREFIXES")
    print("********************************************************************************\n")
    print ("""
    A => Saisir une nouvelle séquence (a,c,t,g)
    B => Saisir un nouveau entier k
    C => Construire et visualiser l'arbre des préfixes
    D => Liste des préfixes et leurs occurences
    E => Occurence d'un motif saisie dans l'arbre
    ....
    Q => Quitter
    """)


def aff_seq(seq):
    if seq is None:
        print("¤ Séquence : PAS DE SEQUENCE")
    else:
        print("¤ Séquence : "+seq)


def aff_k(k):
    if k is None:
        print("¤ Entier : PAS D'ENTIER")
    else:
        print("¤ Entier : "+str(k))
        
# Affiche l'arbe des préfixes, '--'= une profondeure
def aff_arbre (A,i):
    if A['val']!={}:
        print i*'--',A['val']
        if A['a']!={}:
            print 'a',
            aff_arbre(A['a'],i+1)
        if A['t']!={}:
            print 't',
            aff_arbre(A['t'],i+1)
        if A['c']!={}:
            print 'c',
            aff_arbre(A['c'],i+1)
        if A['g']!={}:
            print 'g',
            aff_arbre(A['g'],i+1)    


# Affihe la liste des préfixes d'un arbre limité par un entier k 
def aff_pref(A,motif,k):
    if A!={}:
            print "Motif '",motif,
            print "' -> occurences :",A['val']
            # Récursivité qui construit les motifs
            k-=1
            if A['a']!={}:
                aff_pref(A['a'],(motif+'a'),k)
            if A['t']!={}:
                aff_pref(A['t'],(motif+'t'),k)
            if A['c']!={}:
                aff_pref(A['c'],(motif+'c'),k)
            if A['g']!={}:
                aff_pref(A['g'],(motif+'g'),k)
           
                
 # Affihe le nombre d'occurences d'un motif (<k) préfixe dans un arbre 
def aff_motif(A,motif,k,motif_bis):
    if A!={}and k>=0:
        if motif!='' and motif==motif_bis:
            print "¤ Nombres d'occurences du motif '",motif,"' dans la séquence : ",A['val']
        # Récursivité qui construit les motifs
        k-=1
        if A['a']!={}:
            aff_motif(A['a'],motif,k,(motif_bis+'a'))
        if A['t']!={}:
            aff_motif(A['t'],motif,k,(motif_bis+'t'))
        if A['c']!={}:
            aff_motif(A['c'],motif,k,(motif_bis+'c'))
        if A['g']!={}:
            aff_motif(A['g'],motif,k,(motif_bis+'g'))      
            aff_arbre(A['g'],i+1)
            
# Affihe la liste des préfixes sur une séquence avec un entier k
def aff_pre(liste):
    j=0
    liste_pre=[]
    liste_occ=[]
    for n in liste:
            liste_pre.append(liste[j])
            liste_occ.append(liste_pre.count(liste[j]))
            
            print ("Motif: '"+liste_pre[j]+"'\n"+" Occurence : "+str(liste_occ[j])+"\n")
            j+=1

def aff_arbre_simple (A,i):
    """
    Affiche chaque noeud dispose dans l'arbre 
    avec la profondeur
    disposition en speudo arbre 
    exemple pour un arbre contenant tata et tati on a
    t
     ->a
       ->t
         ->a
       ->i
    """
    #TODO ajouter des | pour voir mieux les noeud de même profondeur et de la même racine
    for lettre in A.keys():
        if lettre!='suff':# cas si lien suffixe
            if i!=0:
             print"\n"+" "*i+"|->",
            else :
                print"\n"
            print lettre+" (profondeur "+str(i)+")",
            aff_arbre_simple (A[lettre],i+1)

def aff_suffixe (A):
    
    """
    Affiche lien 
    avec la profondeur
    disposition en speudo arbre 
    exemple pour un arbre contenant tata et tati on a
    t
     ->a
       ->t
         ->a
       ->i
    """
    #TODO ajouter des | pour voir mieux les noeud de même profondeur et de la même racine
    for lettre in A.keys():
        if lettre=='suff':# cas si lien suffixe
            print A['suff']
            print"***\n"
            aff_suffixe(A['suff'])
