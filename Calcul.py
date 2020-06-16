import numpy as np

def produitVectoriel(u,v):
    w=np.cross(u,v)
    return w


def norme(u):
    return np.linalg.norm(u)


def translation(axe,matriceCoord,translation):#axe : 0=x; 1=y; 2=z
    for i in range(len(matriceCoord)):#on parcout les lignes de la matrice
        matriceCoord[i][0][axe]+=translation
        matriceCoord[i][1][axe]+=translation
        matriceCoord[i][2][axe]+=translation


def calculVecteur(A,B):#deux points avec trois coords sous forme de matrice
    vecteur=(B[0]-A[0],B[1]-A[1],B[2]-A[2])
    return vecteur


def calculeHauteurFacette(A,B,C): # trois points sous forme de matrice avec 3 coords
    hauteur=(A[2]+B[2]+C[2])/3
    return hauteur


def CalculForce(a,normale,hauteur,Rho,masse):
    F_Archimede=0
    g=9.81
    Stot=0
    """ajustement de la hauteur de la coque """
    translation(2,a,hauteur)

    for n in range(0,len(a)): #on parcour pour le nombre de facettes

        """Calcule de la surface total et de chaque facette"""
        U=calculVecteur(a[n][0],a[n][1])
        V=calculVecteur(a[n][0],a[n][2])
        Ds=norme(produitVectoriel(U,V))
        Stot+=Ds #surface totale de la coque
        DsVec=Ds*normale[n]

        """Calcule de la hauteur d'une facette """
        Zfk=calculeHauteurFacette(a[n][0],a[n][1],a[n][2])

        """condition pour que une facette soit compté comme immergé """
        if Zfk <0:
            F_Archimede+=Rho*g*Zfk*DsVec
        else : F_Archimede+=0

    """On remet la hauteur de la coque"""
    translation(2,a,-hauteur)

    """calcule du poid de la coque selon l'axe Oz"""


    F_Poid=(0,0,-1*masse*g)

    """On determine la norme de la resultante du poid plus d'archimède"""

    normeArchimede=np.linalg.norm(F_Archimede)
    print("archi ",F_Archimede)
    print("poid ",F_Poid)
    normePoid=np.linalg.norm(F_Poid)

    difference= normeArchimede-normePoid #Si <0 alors Poid < Archimede sinon >0 alors Poid > Archimede

    return difference


def Dichotomie(Haut,Bas,Precision,a,normale,Rho,masse):
    #print('test',Haut,Bas,Precision,a,normale,Rho,masse)
    if Haut == 0 :
        Bas=-4
        Haut=4
    ecart=Bas-Haut
    #print(ecart)
    while abs(ecart)>Precision:
        Zmilieu=(Haut+Bas)/2
        #print("ecart ",ecart," haut ",Haut," bas ",Bas," Zmilieu ",Zmilieu)
        difference=CalculForce(a,normale,Zmilieu,Rho,masse)
        #print("diff ",difference)
        if difference<0 :
            Haut=Zmilieu

        else : Bas=Zmilieu
        ecart=Haut-Bas

    return Zmilieu
