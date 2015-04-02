#-*- coding:Utf-8 -*-

def menu_arbre_pref():
    print("********************************************************************************")
    print("                              ARBRE DES PREFIXES")
    print("********************************************************************************\n")
    print ("""
    A => Saisir une nouvelle s�quence (a,c,t,g)
    B => Saisir un nouveau entier k
    C => Construire et visualiser l'arbre des pr�fixes
    ....
    Q => Quitter
    """)

def aff_seq(seq):
    if seq is None:
        print("� S�quence : PAS DE SEQUENCE")
    else:
        print("� S�quence : "+seq)

def aff_k(k):
    if k is None:
        print("� Entier : PAS D'ENTIER")
    else:
        print("� Entier : "+str(k))
        

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

def aff_arbre_simple (A,i):
    #TODO ajouter des | pour voir mieux les noeud de m�me profondeur et de la m�me racine
    for lettre in A.keys():
        print " "
        if i!=0:
         print"\n"+" "*i+"|->",
        else :
            print"\n"
        print lettre+" (profondeur "+str(i)+")",
        aff_arbre_simple (A[lettre],i+1)
