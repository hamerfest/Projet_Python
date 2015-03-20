# 
# Recherche des motifs repetes - Indexation par table de hachage
# 

#sequence test
seq="accaccaccag"
#taille test
k=3

def __Creation_Liste_Taille__(sequence,taille):
    """
    Creation liste L de motif de 'sequence' de taille 'taille' avec chevauchement
    """
    #initialisation L
    L = list() # liste vide
    for i in range(len(sequence)): # Parcours de la chaine
        #print lettre
        if len(sequence[i:])>=taille: # sortie si il reste moins de 3 lettresb
           L.append(sequence[i:i+taille])
        else :
            break
    return L
     
def __Lettre_Base_4__(motif):
    """
    transformation d'un motif en base 4 
    a==>0
    c==>1
    t==>2
    g==>3
    """
    ADN=["a","c","t","g"]
    base4=""
    for lettre in motif:
       base4=base4+str(ADN.index(lettre))
    return base4

def __Base_4_En_Base_10__(base4):
    """
    tranformation d'un entier en base 4 en base 10
    base4 : string
    base10: int
    """
    k=len(base4) #taille du motif
    base4= base4[::-1] # string reverse
    resultat=0
    pos=0 #position dans base4
    for chiffre in base4:
        resultat=resultat+int(chiffre)*(4**pos)
        pos+=1
    return resultat

def __Creation_Liste_Taille_Base10__(L):
    """
    Creation liste L1 associe a L contenant les entiers correspondant aux motifs presents dans L
    """
    #initialisation L1
    L1 = list() # liste vide
    for item in L:
        L1.append(__Base_4_En_Base_10__(__Lettre_Base_4__(item)))
    return L1

def __Initialisation_Table_M_(L1):
    
    #initialisation M 
    M=list()
    # M de meme taille que L1 rempli de 0
    for i in range(1,len(L1)+1):# de 1 a "taille de L1"
        M.append(0)
    return M

def __Initialisation_Table_H_(L):
    
    # H de meme taille que 4**k rempli de 0 avec k la taille des motifs contenu dans L
    #initialisation H 
    H=list()
    
    k=len(L[0])
    for i in range(4**k): # de 0 a 4**k-1
        H.append(0)
    return H

def __Remplissage_M_H__(L1,H,M):
    # de 1 a taille de L1
    for i in range(len(L1)): # de 0 a taille L1-1 
    # test : i va de 0 a 8
        n=L1[i]
        if H[n]==0:
            H[n]=i+1
        else :
            M[i]=H[n]
            H[n]=i+1
    return H,M



def __Creation_des_tables__():
    """
    Programme qui permet de saisir une sequence nucleique
    puis creer les listes L et L1 et les tables H et M associes
    et les affiche
    """
    seq=raw_input("Saisissez une sequence nucleique : \n")
    L =__Creation_Liste_Taille__(seq,3)
    L1=__Creation_Liste_Taille_Base10__(L)
    M=__Initialisation_Table_M_(L1)
    H=__Initialisation_Table_H_(L)
    H,M=__Remplissage_M_H__(L1,H,M)
    print "Liste cree L :"
    print L
    print "Liste cree L1 :"
    print L1
    print "Table associe M :"
    print M
    print "Table associe H :"
    print H
    return L,L1,H,M

def __Utilisation_des_tables__(L,L1,H,M):
    motif=raw_input("Saissez un motif de taille 3 : \n")
    #transformation du motif en score type L1
    score=__Base_4_En_Base_10__(__Lettre_Base_4__(motif))
    res=H[score]
    #
    if res>0:
        print "Le motif "+motif+" apparait en position "+str(H[score])
        
        while M[res-1]>0:
            print "Le motif "+motif+" apparait en position "+str(M[res-1])
            res=M[res-1]
        