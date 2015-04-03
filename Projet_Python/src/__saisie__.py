# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Gphy"
__date__ = "mars 2015"

def SaisieInt():
    """
    Saisie controlee d'un entier
    """
    while True:
        try:
            n=int(raw_input("Entrez un nombre : "))
            break
        except ValueError:
            print "Erreur de saisie, veuillez recommencer"
            continue
    return n

def SaisieIntPositif():
    """
    Saisie controlee d'un entier superieur a zero
    """
    while True:
        k=SaisieInt()
        if k>0:
            break
        else:
            print"Erreur de saisie, recommencez ."
            continue
    return k
            
def SaisieIntBorne(min,max):
    """
    Saisie controlee d'un entier borne entre min et max (inclus)
    """
    while True:
        k=SaisieInt()
        if k<=max and k>=min:
            break
        else:
            if min==max:
                print"Erreur de saisie! Le nombre doit etre egal a "+str(min)+" recommencez."
            else: 
                print"Erreur de saisie! Le nombre doit etre compris entre "+str(min)+" et "+str(max)+" recommencez."
            continue
    return k

def ValideADN(seq):
    """
    Retourne True si la sequence est valide (atcg uniquement), FAUX sinon
    """
    seq.lower()
    res=len(seq)!=0
    for lettre in seq:
        res=(res and True)\
            if (lettre=='a') or (lettre=='c') or (lettre=='g') or (lettre=='t')\
            else False
    return res

def SaisieADN():
    """
    Saisie controlee d'une chaine de caractere en ADN
    Ne contient que des atcg case non sensitive
    revoit la sequence correcte en minuscule
    """
    while True:
        ADN=raw_input("Entrer un sequence d'ADN (atgc) : ")
        ADN=ADN.lower()
        
        if ValideADN(ADN):
            print "Sequence saisie correcte"
            break
        else:
            print "Erreur de saisie, recommencez "
    return ADN

def SaisieADNBornee(min,max):
    """
    Saisie controlee d'une chaine de caractere en ADN d'une taille min et max attendue
    Ne contient que des atcg 
    case non sensitive
    revoit la sequence correcte en minuscule
    """
    while True:
        if min==max: 
            ADN=raw_input("Entrer un sequence d'ADN (atgc) de taille "+str(min)+" : ")
        else:
            ADN=raw_input("Entrer un sequence d'ADN (atgc) de taille compris entre "+str(min)+" et "+str(max)+" : ")
        ADN.lower()
        if ValideADN(ADN) and len(ADN)>=min and len(ADN)<=max:
            print "Sequence saisie correcte"
            break
        else:
            print "Erreur de saisie, recommencez "
    return ADN

