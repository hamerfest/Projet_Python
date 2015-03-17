# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Gphy"
__date__ = "mars 2015"


#ChaineNettoyee(alphabet,mot): supprime les caracteres non compris dans l'alphabet
#puis retourne ce nouveau mot

def ChaineNettoyee(alphabet,mot):
    i = 0 #cpteur de mot
    j = 0 #cpteur de alphabet
    while i<len(mot):
        if mot[i]==alphabet[j]:
            #Lettre suivante
            i+=1
            #Reprise du début de l'alphabet
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
    print("==> Chaine nettoyée : "+str(mot))
    return mot

#Fonction qui vérifie si le mot est composé que des lettres de l'alphabet(=>liste)
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
                #Reprise du début de l'alphabetS
                j=0
            else:
                if j<len(alphabet)-1:
                    j+=1
                else:
                    #L'alphabet a été parcourue => Mauvaise lettre
                    print("\nErreur de saisie de "+str(mot)+" a la position "+str(i+1)+" selon l'alphabet "+str(alphabet)+" ")
                    Correct=False
                    while Correct == False:
                        res=input("Voulez-vous nettoyer toute la chaine de caractere ? (O/N) ")
                        res=res.upper()
                        if res=='O':
                            print("Chaine Non nettoyée : "+str(mot))
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

