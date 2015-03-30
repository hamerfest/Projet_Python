#-*- coding:Utf-8 -*-
#
# Arbre de préfixes de motifs de taille k ou < sur une seq. + affichage prefixe et occurences 
#

def insertion_arbre (A,seq):
    if A=={}:
        A={'val':0,'a':{},'t':{}, 'c':{}, 'g':{}}
    Arbre_bis=A
    if len(seq)>0:
        if Arbre_bis[seq[0]]=={}:
            Arbre_bis[seq[0]]= {'val':0,'a':{},'t':{}, 'c':{}, 'g':{}}
            Arbre_bis==insertion_arbre (Arbre_bis[seq[0]],seq[1:])
        else:
            Arbre_bis==insertion_arbre (Arbre_bis[seq[0]],seq[1:])      
    else:
        Arbre_bis['val']+=1
    return Arbre_bis