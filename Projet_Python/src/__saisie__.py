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
        ADN.lower()
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

#ChaineNettoyee(alphabet,mot): supprime les caracteres non compris dans l'alphabet
#puis retourne ce nouveau mot

def ChaineNettoyee(alphabet,mot):
    i = 0 #cpteur de mot
    j = 0 #cpteur de alphabet
    while i<len(mot):
        if mot[i]==alphabet[j]:
            #Lettre suivante
            i+=1
            #Reprise du debut de l'alphabet
            j=0
        else :
            if j<len(alphabet)-1:
                j+=1
            else:
                #Detection d'un mauvais caractere on remplace pour le mot
                mot=str(mot.replace(mot[i],'~'))
                #On passe au caractere suivant
                i+=1
                j=0
                #testprint('Nouveau Mot '+str(mot))
                

    mot=str(mot.replace('~',''))
    print("==> Chaine nettoyee : "+str(mot))
    return mot

#Fonction qui verifie si le mot est compose que des lettres de l'alphabet(=>liste)
#Si ok renvois le mot
#Sinon proposition de resaisie ou effacer les lettres non incluses dans l'alphabet ou sortie de l'algo
def SaisieMot(alphabet,mot) : #Case sensitive cf alphabet
    i = 0 #cpteur de mot
    j = 0 #cpteur de alphabet
    res=''
    mot=str(mot)
    while i <= len(mot)-1:
        if len(mot)==0:
            mot=str(input("Mot vide !! \nTapez Entree pour sortir du programme ou \nVeuillez saisir au moins un caractere selon l'alphabet "+str(alphabet)+" : "))
            i=0
            j=0
        else:
            Correct=True   
            if mot[i]==alphabet[j]:
                #Lettre suivante
                i+=1
                #Reprise du debut de l'alphabetS
                j=0
            else:
                if j<len(alphabet)-1:
                    j+=1
                else:
                    #L'alphabet a ete parcourue => Mauvaise lettre
                    print("\nErreur de saisie de "+str(mot)+" a la position "+str(i+1)+" selon l'alphabet "+str(alphabet)+" ")
                    Correct=False
                    while Correct == False:
                        res=input("Voulez-vous nettoyer toute la chaine de caractere ? (O/N) ")
                        res=res.upper()
                        if res=='O':
                            print("Chaine Non nettoyee : "+str(mot))
                            mot=str(ChaineNettoyee(alphabet,str(mot)))    
                            if len(mot)!=0 :
                                print("==> Mot correct suivant l'alphabet "+str(alphabet))
                                mot=str(mot)
                                return str(mot)
                                
                            else:
                                Correct =True
                                i=-1
                                j=0
                        else:
                            if res=='N':
                                print('==> Sortie du programme')
                                Correct=True
                                i=len(mot)+1
                                mot=str('')
                                break
                            
                            else:
                                print("==> Erreur de saisie recommencez")
                

        return str(mot)

def SaisieAlpha(chaine):# String => List ; Procedure case sensitive
    alphabet=[]
    while True:
        if len(chaine)==0:
            chaine= input("==> Liste vide veuillez saisir au moins un caractere \nSaisissez un alphabet : ")
        else:
            for i in chaine :
                alphabet.append(str(i))
            #Traitement sans doublons + transtypage en liste
            alphabet=list(set(alphabet))
            print("==> Alphabet saisie et sans doublons : "+ str(alphabet))
            return alphabet    

