#-*- coding:Utf-8 -*-

def menu_arbre_pref():
    print("********************************************************************************")
    print("                              ARBRE DES PREFIXES")
    print("********************************************************************************\n")
    print ("""
    A => Saisir une nouvelle séquence (a,c,t,g)
    B => Saisir un nouveau entier k
    C => Construire et visualiser l'arbre des préfixes
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
        print("********************************************************************************\n")
    else:
        print("¤ Entier : "+str(k))
        print("********************************************************************************\n")
        

def aff_arbre (A):
    if A['val']!={}:
        print(A['val'])
        if A['a']!={}:
            print 'a',
            aff_arbre(A['a'])
        if A['t']!={}:
            print 't',
            aff_arbre(A['t'])
        if A['c']!={}:
            print 'c',
            aff_arbre(A['c'])
        if A['g']!={}:
            print 'g',
            aff_arbre(A['g'])