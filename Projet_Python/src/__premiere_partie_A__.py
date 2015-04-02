#-*- coding:Utf-8 -*-
#
# Arbre de préfixes de motifs de taille k ou < sur une seq. + affichage prefixe et occurences 
#

# Creation de l'arbre avec l'alphabet 'atcg'
def insertion_arbre (A,seq):
    if A=={}:
        A={'val':0,'a':{},'t':{}, 'c':{}, 'g':{}}
    Arbre_bis=A
    if len(seq)>0:
        if Arbre_bis[seq[0]]=={}:
            Arbre_bis[seq[0]]= {'val':0,'a':{},'t':{}, 'c':{}, 'g':{}}
            Arbre_bis[seq[0]]=insertion_arbre (Arbre_bis[seq[0]],seq[1:])
        else:
            Arbre_bis[seq[0]]=insertion_arbre (Arbre_bis[seq[0]],seq[1:])      
    else:
        # Rajoute une occurence à 'val' une fois toute la séquence lue
        Arbre_bis['val']+=1
    return Arbre_bis


# Parcour préfixe + Insertion dans l'arbre
def construction_arbre (A,seq,k):
    liste=[''] # Liste contenant successivement les différents préfixes jusqu'a la taille k (mot vide inclus)
    for l in seq: # Parcour de de la séquence par lettre 'l'
        liste_bis=[''] # Permet de constituer les differents motifs préfixes
        for v in liste: # Parcour les motifs pour leur ajouter un lettre
            if len(v) <= k:
                A=insertion_arbre(A,v)
                liste_bis.append(v+l)
        liste=liste_bis
    for v in liste:
        if len(v) <= k and v!='': #Insertion dans l'arbre pour les motifs inférieurs à k
            A=insertion_arbre(A,v)
    return (A)

    
# Parcour préfixe
def liste_pref(seq,k):
    liste=['']
    liste_pre=[]
    liste_occ=[]
    for l in seq:
        liste_bis=['']
        for v in liste:
            if len(v) < k:
                    liste_bis.append(v+l)
        liste=liste_bis
        liste_pre=liste_pre+liste #Stockage de tout les préfixes
        
    return (liste_pre)
  